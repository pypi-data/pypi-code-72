import numpy as np
import cv2
from scipy import ndimage
from pdf2txt.core.tree import Node
from pdf2txt.settings import DEFAULT_X_SEPARATOR_WIDTH, DEFAULT_Y_SEPARATOR_HEIGHT, MIN_AREA_HIEGHT, MIN_AREA_WIDTH
from pdf2txt.utils import BoundingBox, is_ovarlaping_with_objects, cluster_objects



class SpaceRegionExtractor:
    h_separator_width = DEFAULT_X_SEPARATOR_WIDTH
    v_separator_height = DEFAULT_Y_SEPARATOR_HEIGHT

    def __init__(self, min_area_height=MIN_AREA_HIEGHT, min_area_width=MIN_AREA_WIDTH):

        self.min_area_height = min_area_height
        self.min_area_width = min_area_width
        self.objects = None

    def sanitize_objects(self, page):
        """
        Removes some objects that hinder the region detection: large rectangles, large vertical lines top large horizental line and bottom large horisental line
        """

        #these are graphical lines that span the page from side to side. However, they
        self.horizontal_separators = sorted([line for line in page.lines if (line.right - line.left) >= 0.98 * (page.content_width)], key=lambda l: l.top)
        #we also filter out large vertical lines as we will noy use them a region separators
        lines = sorted([line for line in page.lines if ((line.right - line.left) < 0.98 * (page.content_width) and line.height < 0.65 * (page.bottom_margin-page.top_margin))], key=lambda l: l.top)
        #we fitler out large rectangles surrouning the content. They get in the way a a generic algorithm


        rects = sorted([rect for rect in page.rects if (
                            (rect.width < 0.98 * (page.content_width)) and (
                                rect.height < 0.65 * (page.bottom_margin - page.top_margin)))],
                key=lambda l: (l.left, l.top))

        clustered=cluster_objects(rects, "left", 2)
        if clustered:
            for cluster in clustered:
                joined=[cluster[0]]
                for r in cluster:
                    if r.top<=joined[-1].bottom:
                        joined.append(r)

                if joined[-1].bottom-joined[0].top> 0.65 * (page.bottom_margin - page.top_margin):
                    for r in cluster:
                        rects.remove(r)


        self.objects=lines+rects+page.graphs+page.tokens+page.tables

    def extract_regions_from_objects(self, page):
        from pdf2txt.core.page import Region

        self.parent_right=page.right
        self.parent_bottom=page.bottom

        statistics=page.font_statistics
        h=max(statistics['interline'], 2)
        self.sanitize_objects(page)
        regions = self.regions_from_spaces(page, page, horizental_separator_width=h,
                                                     vertical_separator_width=2, method='objects')


        return regions


    def extract_regions_from_image(self, image, algoithm='global', threshold=200):

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # blur = cv2.GaussianBlur(gray, (9,9), 0)
        if algoithm=='global':
            _, thresh = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)
        else:
            thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

        page = BoundingBox(top=0, left=0, right=thresh.shape[1], bottom=thresh.shape[0])
        regions = self.regions_from_spaces(thresh, page, method='pixels')

        return regions

    def regions_from_spaces(self, page, bbox, vertical_separator_width=None, horizental_separator_width=None,
                            split_direction='all', method='pixels'):

        if vertical_separator_width:
            self.v_separator_height = vertical_separator_width
        if horizental_separator_width:
            self.h_separator_width = horizental_separator_width

        area_tree = self.split_tree_of_rectangles(page=page, bbox=bbox, split_direction=split_direction, method=method )

        return area_tree.get_leaf_nodes()

    def split_tree_of_rectangles(self, page, bbox, split_direction='all',method='pixels', step=0):
        # possible values for split_direction: 'all',  'horizental', 'vertical'
        tree = Node(bbox)

        split_vertical = False
        split_horizental = False

        if split_direction == 'all':
            split_vertical = True
            split_horizental = True
        elif split_direction in ['vertical', 'v']:
            split_vertical = True
        elif split_direction in ['horizental', 'h']:
            split_horizental = True
        else:
            raise Exception("split_direction have to be either 'all', 'vertical' , 'v  'horizental' or 'h'")
        split = (None, None)
        if split_vertical:
            split = self._split_region_vertical(page, area=bbox, method=method)

        if split == (None, None):
            if split_horizental:
                min_area_height = self.min_area_height
                if step > 1:
                    min_area_height = 2 * self.min_area_height
                split = self._split_region_horizental(page, area=bbox, min_height=min_area_height, method=method)

        if split != (None, None):
            if split[0]:
                tree.left = self.split_tree_of_rectangles(page, split[0], split_direction,method, step + 1)
            if split[1]:
                tree.right = self.split_tree_of_rectangles(page, split[1], split_direction,method, step + 1)
        return tree

    def _compute_pixel_count(self, page, region, axis=1, method='pixels'):
        if method=='pixels':
            region = page[region.top:region.bottom, region.left:region.right]
            return np.sum(region, axis=axis)
        elif method=='objects':
            nb_overlaps=[]
            if axis==1:
                for top in range(int(region.top), int(region.bottom)):
                    separator = BoundingBox(left=region.left, right=region.right, top=top, bottom=top+1)
                    nb_overlaps.append(is_ovarlaping_with_objects(separator, self.objects))
            elif axis==0:
                for left in range(int(region.left), int(region.right)):
                    right = left + 1
                    separator = BoundingBox(left=left, right=right, top=region.top, bottom=region.bottom)
                    nb_overlaps.append(is_ovarlaping_with_objects(separator, self.objects))

            return np.array([int(val) for val in nb_overlaps])
        else:
            raise Exception("Split method should be either 'pixels' or 'objects ")

    def _split_region_horizental(self, page, area, min_height, method='pixels'):

        from pdf2txt.core.page import Region
        r1 = None
        r2 = None

        pixel_counts = self._compute_pixel_count(page, area, axis=1, method=method)

        i=1
        while pixel_counts[-i] == 0:
            pixel_counts[-i] = 1
            i+=1
        i=0
        while pixel_counts[i] == 0:
            pixel_counts[i] = 1
            i+=1

        split_indices, labels, s = self.get_gaps_by_largest(pixel_counts)
        if len(split_indices) > 0:
            indices = np.where(labels == split_indices[0] + 1)
            if len(indices[0]) > self.h_separator_width:
                split_y = indices[0][int(len(indices[0]) / 2)]
                i = 1
                min_height=min(min_height, page.bottom-area.top-split_y)

                while (split_y < min_height or abs(area.bottom - area.top - split_y) < min_height or  len(indices[0]) < self.h_separator_width) and i < len(split_indices):
                    indices = np.where(labels == split_indices[i] + 1)
                    split_y = indices[0][int(len(indices[0]) / 2)]
                    i += 1
                if abs(area.top + split_y - area.top) >= min_height and abs(area.bottom - area.top - split_y) >= min_height and len(
                        indices[0]) >= self.h_separator_width:
                    r1 = Region(area, BoundingBox(top=area.top, left=area.left, right=area.right, bottom=area.top + split_y))
                    r2 = Region(area, BoundingBox(top=area.top + split_y, left=area.left, right=area.right, bottom=area.bottom))
        return r1, r2

    def _split_region_vertical(self, page, area, method='pixels'):
        from pdf2txt.core.page import Region

        r1 = None
        r2 = None

        pixel_counts = self._compute_pixel_count(page, area, axis=0, method=method)

        i=1
        while pixel_counts[-i] == 0:
            pixel_counts[-i] = 1
            i+=1
        i=0
        while pixel_counts[i] == 0:
            pixel_counts[i] = 1
            i+=1


        split_indices, labels, s = self.get_gaps_by_largest(pixel_counts)
        if len(split_indices) > 0:
            indices = np.where(labels == split_indices[0] + 1)
            if len(indices[0]) > self.v_separator_height:
                split_x = indices[0][int(len(indices[0]) / 2)]
                i = 1
                while (abs(split_x) < self.min_area_width or abs(area.right-area.left - split_x) < self.min_area_width or len( indices[0]) < self.v_separator_height) and i < len(split_indices):
                    indices = np.where(labels == split_indices[i] + 1)
                    split_x = indices[0][int(len(indices[0]) / 2)]
                    i += 1

                if abs(split_x) >= self.min_area_width and abs(area.right-area.left - split_x) >= self.min_area_width and len( indices[0]) >= self.v_separator_height:
                    r1 = Region(area, BoundingBox(top=area.top, left=area.left, right=area.left + split_x, bottom=area.bottom))
                    r2 = Region(area, BoundingBox(top=area.top, left=area.left + split_x, right=area.right, bottom=area.bottom))
        # if r1:
        #     plot_page([r1, r2], page.width, page.height)
        return r1, r2

    def get_gaps_by_largest(self, arr):
        labels, num_label = ndimage.label(arr == 0)
        sizes = np.bincount(labels.ravel())
        biggest_labels = (-sizes[1:]).argsort()
        return biggest_labels, labels, sizes
