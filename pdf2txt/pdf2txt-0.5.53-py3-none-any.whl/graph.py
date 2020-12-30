from pdf2txt.utils import cluster_objects, get_type, get_partially_overlapping_objects, intersecting_edges, \
    parse_value, is_ovarlaping_with_objects, get_widthin_BoundingBox
from statistics import mean
from pdf2txt.utils import BoundingBox, get_widthin_BoundingBox, get_BoundingBox_from_objects, contains_objects
import pandas as pd
from pdf2txt.core.paragraph import extract
from copy import deepcopy

class Graph(BoundingBox):

    def __init__(self, left, top, right, bottom, graph_type, page, **kwargs):
        super().__init__(left, top, right, bottom, **kwargs)
        self.page=page
        self.graph_type=graph_type
        self.MAX_NB_DATAPOINTS=10

    def extract_chart_data(self):

        words=get_widthin_BoundingBox(self.page.tokens, self)
        if self.graph_type=='h':
            return self.extract_chart_data_horizontal(words)
        elif self.graph_type=='v':
            return self.extract_chart_data_vertical(words)

    def extract_chart_data_horizontal(self,  words):
        # parse graph data
        #suposes all values are positive
        data = []
        labels = []
        if len(words)==0 or len(self.components)==0:
            return {'dataframe': None,
                    'text': []}

        extra_words=[w for w in words if w.bottom <self.components[0].top or w.top >self.components[-1].bottom]
        for component in self.components:
            bbox = BoundingBox(left=component.left, right=component.right+10, top=component.top, bottom=component.bottom)
            value = get_partially_overlapping_objects(bbox, words)
            if len(value) > 0:
                value_t = value[0].Text
                data.append(parse_value(value_t.strip('%')))
            bbox = BoundingBox(left=self.left, right=component.right, top=component.top, bottom=component.bottom)
            value = get_partially_overlapping_objects(bbox, words)
            if len(value) > 0:
                labels.append(value[0].Text)
            else:
                labels.append("")

        df = pd.DataFrame(list(zip(labels, data)),
                          columns=['label', 'value'])
        if df.empty:
            df = None
        return {'dataframe': df,
                'text': extra_words}

    def extract_chart_data_vertical(self,  words):
        # parse graph data
        data = []
        labels = []
        for component in self.components:
            bbox = BoundingBox(left=component.left, right=component.right, top=component.top, bottom=component.bottom + 10)
            all_values = 0
            values = get_partially_overlapping_objects(bbox, words)
            for value in values:
                value_t = value.Text
                value_f = parse_value(value_t.strip('%'))
                if get_type(value_f)=="Numeric":
                    data.append(value_f)
                else:
                    labels.append(value_t)

            if len(values) < 2:
                bbox = BoundingBox(left=component.left, right=component.right, top=component.top - 10,
                                   bottom=component.bottom)
                value = get_partially_overlapping_objects(bbox, words)
                if len(value) > 0:
                    value_t = value[0].Text
                    value_f = parse_value(value_t.strip('%'))
                    if get_type(value_f) =="Numeric":
                        data.append(value_t)
                    else:
                        labels.append(value_t)

        df = pd.DataFrame(list(zip(labels, data)),
                          columns=['label', 'value'])
        return df
def extract_graphs(page, rect_threshold=4):

    rectangles_=page.rects+[c for c in page.curves if c.width<100 and c.height<100]
    #sometimes there are duplicates in regtangle list due to pdf objects defined twice
    rectangles=[]
    for r in rectangles_:
        if not contains_objects(r, rectangles):
            rectangles.append(r)
    rect_for_graphs = sorted(
        [rect for rect in rectangles if
         rect.fill and (200 > rect.width > 0.5 and 200 > rect.height > 0.5)], key=lambda l: l.top)

    edges = rects_to_edges(rect_for_graphs, page.tokens, rect_threshold=rect_threshold)

    graphs=[]
    for e in edges['v']: #horizontal graphs
        chart_area=extract_chart_area(e, page, rect_for_graphs,graph_type='h')
        #sometimes several horizontal graphs can be identified as one graph area.
        #they are typically separated by titles. these titles will not at the same height as the bars
        #identifying them will help separate different charts
        tokens = get_widthin_BoundingBox(page.tokens, chart_area)
        doctop_clusters = cluster_objects(tokens, "bottom", tokens[0].font_size/3)

        text_lines = [line for line in doctop_clusters]

        groups=extract(text_lines)
        for g in groups:
            bbox_g=get_BoundingBox_from_objects([t[0] for t in g])
            sub_e=deepcopy(e)
            sub_e["axis"].top=bbox_g.top
            sub_e["axis"].bottom=bbox_g.bottom
            sub_e["bbox"].top=bbox_g.top
            sub_e["bbox"].bottom=bbox_g.bottom


            sub_e["components"]=[c for c in sub_e["components"] if c.top> bbox_g.top and c.bottom<bbox_g.bottom]
            graphs.append(extract_chart_area(sub_e, page,rect_for_graphs, graph_type='h'))
    for e in  edges['h']:
        graphs.append(extract_chart_area(e, page, rect_for_graphs, graph_type='v'))

    return graphs


def rects_to_edges(rectangles, words, rect_threshold=4):
    """
    Find (imaginary) vertical lines that connect the left, right, or
    center of at least `word_threshold` words.
    """
    # Find words that share the same left, right, or centerpoints
    by_left = cluster_objects(rectangles, "left", 2)
    by_bottom = cluster_objects(rectangles, "bottom", 2)
    by_top = cluster_objects(rectangles, "top", 2)
    if by_top:
        by_bottom+=by_top
    edges = {}
    # Find the points that align with the most words
    if by_left is None:
        by_left = []
    if by_bottom is None:
        by_bottom = []

    by_left = list(filter(lambda x: len(x) >= rect_threshold, by_left))
    by_bottom = list(filter(lambda x: len(x) >= rect_threshold, by_bottom))


    by_left2=[]
    for left in by_left:
        heights=set(int(r.bottom-r.top) for r in left)
        widhs = set(int(r.right - r.left) for r in left)
        if len(heights)<2 and len(widhs)>=rect_threshold-1:
            by_left2.append(left)

    by_bottom2=[]
    for bottom in by_bottom:
        heights=set(int(r.bottom-r.top) for r in bottom)
        widths = set(int(r.right - r.left) for r in bottom)
        if len(widths)<2 and len(heights)>=rect_threshold-1:
            by_bottom2.append(bottom)

    edge = {}
    by_bottom=by_bottom2
    by_left=by_left2
    edges['h'] = []
    for rects in by_bottom:
        edge = build_axis_from_edges(rects, rectangles, 'h')
        heights = set([int(r.bottom - r.top) for r in edge['components']])
        average_width = mean([(r.right - r.left) for r in edge['components']])
        if len(heights) > 3 and average_width < 30:
            edges['h'].append(edge)

    edges['v'] = []
    for rects in by_left:
        edge = build_axis_from_edges(rects, rectangles, 'v')

        heights = set([int(r.right - r.left) for r in edge['components']])
        if len(heights) > 3:
            edges['v'].append(edge)

    intersection_text = intersecting_edges([e['axis'] for e in edges['v']], words, x_tolerance=-1, y_tolerance=1)

    # if the edge intersect text we typically crossed to an other chart or rectangle. We split and recompute
    for k, v in intersection_text.items():
        vertical = v['v'][0]
        top = k[1]
        for edge in edges['v']:
            if edge['axis'] == vertical:
                top_components = [c for c in edge['components'] if c.bottom < top]
                remaining_components = edge['components'] = [c for c in edge['components'] if c.top > top]
                if len(top_components) >= 3:
                    edge1 = build_axis_from_components(top_components, 'v')
                    if edge in edges['h']:
                        edges['h'].remove(edge)
                    edges['h'].append(edge1)
                if len(remaining_components) >= 3:  # create new edge
                    edge2 = build_axis_from_components(remaining_components, direction='v')
                    edges['v'].append(edge2)

    # Do the same on the horisental graphs

    intersection_text = intersecting_edges(words, [e['axis'] for e in edges['h']], x_tolerance=-1, y_tolerance=1)

    # if the edge intersect text we typically crossed to an other chart or rectangle. We split and recompute
    for k, v in intersection_text.items():
        vertical = v['h'][0]
        left = k[0]
        for edge in edges['h']:
            if edge['axis'] == vertical:
                top_components = [c for c in edge['components'] if c.left < left]
                remaining_components = edge['components'] = [c for c in edge['components'] if c.left > left]
                if len(top_components) >= 3:
                    edge1 = build_axis_from_components(top_components, direction='h')
                    edges['h'].remove(edge)
                    edges['h'].append(edge1)
                if len(remaining_components) >= 3:  # create new edge
                    edge2 = build_axis_from_components(remaining_components, 'h')
                    edges['h'].append(edge2)

    intersection_data = intersecting_edges([e['axis'] for e in edges['v']], [e['axis'] for e in edges['h']],
                                           x_tolerance=-1, y_tolerance=1)
    intersections = set(
        [v['v'][0] for k, v in intersection_data.items()] + [v['h'][0] for k, v in intersection_data.items()])

    edges['v'] = [e for e in edges['v'] if e['axis'] not in intersections and e["bbox"].bottom-e["bbox"].top >60]
    edges['h'] = [e for e in edges['h'] if e['axis'] not in intersections and e["bbox"].right-e["bbox"].left >60]

    return edges


def build_axis_from_edges(edge_rects, all_rectangles, direction='h'):
    edge = {}

    if direction == 'h':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in edge_rects),
                                   right=max(rect.right for rect in edge_rects),
                                   top=min(rect.bottom for rect in edge_rects),
                                   bottom=min(rect.bottom for rect in edge_rects))
        edge['direction'] = 'h'
    elif direction == 'v':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in edge_rects),
                                   right=min(rect.left for rect in edge_rects),
                                   top=min(rect.top for rect in edge_rects),
                                   bottom=max(rect.bottom for rect in edge_rects))
        edge['direction'] = 'v'
    else:
        raise Exception("wrong direction. Should be either 'h' for horizontal  or 'v' for vertical")
    edge['components'] = get_partially_overlapping_objects(edge['axis'], all_rectangles)
    edge['bbox'] = BoundingBox(left=min(rect.left for rect in edge['components']),
                               right=max(rect.right for rect in edge['components']) + 5,
                               top=min(rect.top for rect in edge['components']) - 10,
                               bottom=max(rect.bottom for rect in edge['components']))

    return edge


def build_axis_from_components(componenets, direction='h'):
    edge = {}

    if direction == 'h':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in componenets),
                                   right=max(rect.right for rect in componenets),
                                   top=min(rect.bottom for rect in componenets),
                                   bottom=min(rect.bottom for rect in componenets))
        edge['direction'] = 'h'
    elif direction == 'v':
        edge['axis'] = BoundingBox(left=min(rect.left for rect in componenets),
                                   right=min(rect.left for rect in componenets),
                                   top=min(rect.top for rect in componenets),
                                   bottom=max(rect.bottom for rect in componenets))
        edge['direction'] = 'v'

    edge['components'] = componenets
    edge['bbox'] = BoundingBox(left=min(rect.left for rect in edge['components']),
                               right=max(rect.right for rect in edge['components']),
                               top=min(rect.top for rect in edge['components']),
                               bottom=max(rect.bottom for rect in edge['components']))

    return edge



def extract_chart_area(edge, page, rectangles, graph_type):
    # parse graph data
    NB_POINTS = 10

    bbox = edge['bbox']
    bbox_left = BoundingBox(left=bbox.left, top=bbox.top, right=bbox.left, bottom=bbox.bottom)
    bbox_right = BoundingBox(left=bbox.right, top=bbox.top, right=bbox.right, bottom=bbox.bottom)
    bbox_top = BoundingBox(left=bbox.left, top=bbox.top, right=bbox.right, bottom=bbox.top)
    bbox_bottom = BoundingBox(left=bbox.left, top=bbox.bottom, right=bbox.right, bottom=bbox.bottom)

    # move left until we meet left axis text within max distance of 20 points
    i = 0
    while not is_ovarlaping_with_objects(bbox_left, page.tokens) and i < NB_POINTS:
        edge['bbox'].left -= 1
        bbox_left.left -= 1
        bbox_left.right -= 1
        i += 1

    if i == NB_POINTS:
        # we did not find any text redude the area by 10
        edge['bbox'].left += NB_POINTS
    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_left, page.tokens):
            edge['bbox'].left -= 1
            bbox_left.left -= 1
            bbox_left.right -= 1

    i = 0
    while not is_ovarlaping_with_objects(bbox_top, page.tokens) and i < NB_POINTS:
        edge['bbox'].top -= 1
        bbox_top.top -= 1
        bbox_top.bottom -= 1
        i += 1

    if i == NB_POINTS:
        # we did not find any text redude the area by 10
        edge['bbox'].top += NB_POINTS
    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_top, page.tokens):
            edge['bbox'].top -= 1
            bbox_top.top -= 1
            bbox_top.bottom -= 1

    i = 0
    while not is_ovarlaping_with_objects(bbox_right, page.tokens) and i < int(NB_POINTS / 2):
        edge['bbox'].right += 1
        bbox_right.right += 1
        bbox_right.left += 1

        i += 1

    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_right, page.tokens):
            edge['bbox'].right += 1
            bbox_right.left += 1
            bbox_right.right += 1

    i = 0
    while not is_ovarlaping_with_objects(bbox_bottom, page.tokens) and i < NB_POINTS:
        edge['bbox'].bottom += 1
        bbox_bottom.bottom += 1
        bbox_bottom.top += 1
        i += 1
    if i == NB_POINTS:
        # we did not find any text redude the area by 10
        edge['bbox'].bottom -= NB_POINTS/4
    if i == 0:
        edge['bbox'].bottom += NB_POINTS/4
        bbox_bottom.bottom += NB_POINTS/4
        bbox_bottom.top += NB_POINTS/4
    if i < NB_POINTS:
        # once you touch text continue until you passed it

        while is_ovarlaping_with_objects(bbox_bottom, page.tokens):
            edge['bbox'].bottom += 1
            bbox_bottom.bottom += 1
            bbox_bottom.top += 1

    while is_ovarlaping_with_objects(
            BoundingBox(left=edge['bbox'].right, top=edge['bbox'].top, right=edge['bbox'].right,
                        bottom=edge['bbox'].bottom), page.tokens):
        edge['bbox'].right += 1
        bbox_bottom.right += 1
        bbox_bottom.left += 1

    edge['axis'].top=edge['bbox'].top
    edge['axis'].bottom=edge['bbox'].bottom

#    edge['components']=get_partially_overlapping_objects(edge['bbox'], rectangles)
    return Graph(left=edge['bbox'].left, right=edge['bbox'].right, top=edge['bbox'].top, bottom=edge['bbox'].bottom, page=page, graph_type=graph_type, **edge)
