import numpy as np
import pandas as pd
import math
import matplotlib
import cv2 as cv
from src import stats
from src import ImageProcessing
matplotlib.use('tkAgg')
import matplotlib.pyplot as plt
import statistics as stat
from skimage import feature
import time
import multiprocessing
import random
from scipy import signal
import multiprocessing
from joblib import Parallel, delayed
from tqdm import tqdm

class getStripe:
    def __init__(self, unbalLib, resol, minH, maxW, canny, all_chromnames, chromnames, all_chromsizes, chromsizes, core):
        self.unbalLib = unbalLib
        self.resol = resol
        self.minH = minH
        self.maxW = maxW
        self.canny = canny
        self.all_chromnames = all_chromnames
        self.all_chromsizes = all_chromsizes
        self.chromnames = chromnames
        self.chromsizes = chromsizes
        self.core = core
        self.chromnames2sizes={}
        for i in range(len(self.all_chromnames)):
            self.chromnames2sizes[self.all_chromnames[i]] = self.all_chromsizes[i]

    def nulldist(self):
        np.seterr(divide='ignore', invalid='ignore')
        t_background_start = time.time()

        #tableft = [[0 for j in range(1000)] for i in range(400)]
        #tabcenter = [[0 for j in range(1000)] for i in range(400)]
        #tabright = [[0 for j in range(1000)] for i in range(400)]

        samplesize = (self.all_chromsizes / np.sum(self.all_chromsizes)) * 1000
        samplesize = np.uint64(samplesize)
        dif = 1000 - np.sum(samplesize)
        notzero = np.where(samplesize != 0)
        chromnames2 = [self.all_chromnames[i] for i in notzero[0]]
        samplesize[0] += dif

        def available_cols(chr):
            np.seterr(divide='ignore', invalid='ignore')
            chr = str(chr)
            chrsize = self.chromnames2sizes[chr]
            itera = min(chrsize/self.resol/500, 25)
            itera = np.uint64(itera)
            unitsize = np.floor(chrsize/self.resol/itera)
            unitsize = np.uint64(unitsize)
            poolsum = 0
            for it in range(itera):
                test_region_start = np.uint64(unitsize * self.resol * it+1)
                test_region_end = np.uint64(unitsize * self.resol * (it+1))
                if test_region_start > test_region_end:
                    a = test_region_start
                    test_region_start = test_region_end
                    test_region_end = a
                position = str(chr) + ":" + str(test_region_start) + "-" + str(test_region_end)
                mat = self.unbalLib.fetch(position, position)
                mat = nantozero(mat)
                mat = np.round(mat, 1)
                matsum = np.sum(mat, axis=1)
                zeroindex = np.where(matsum == 0)
                poolsum += (len(matsum) - len(zeroindex[0]))

            return poolsum

        print('1. Calculating the number of available columns ... \n')
        n_available_col = Parallel(n_jobs=self.core)(delayed(available_cols)(chr) for chr in tqdm(chromnames2))

        samplesize = (n_available_col/ np.sum(n_available_col)) * 1000
        samplesize = np.uint64(samplesize)
        dif = 1000 - np.sum(samplesize)
        notzero = np.where(samplesize != 0)
        chromnames2 = [chromnames2[i] for i in notzero[0]]
        samplesize[0] += dif

        def main_null_calc(chr):
            background_size = 50000/self.resol
            background_up = np.floor(background_size / 2)
            background_down = background_size - background_up
            background_up = int(background_up)
            background_down = int(background_down)
            background_size = int(background_size)
            chr = str(chr)
            np.seterr(divide='ignore', invalid='ignore')
            #c = np.where(chromnames2 == chr)[0]
            c = chromnames2.index(chr)

            # Modified in Dec 11 2020
            ss = samplesize[c]
            chrsize = self.chromnames2sizes[chr]
            itera = min(chrsize/self.resol/500, 25)
            itera = np.uint64(itera)
            unitsize = np.floor(chrsize/self.resol/itera)
            unitsize = np.uint64(unitsize)

            bgleft = np.zeros((400, 0))
            bgright = np.zeros((400, 0))

            n_pool = []

            for it in range(itera):
                sss = np.uint64(ss/itera)
                test_region_start1 = np.uint64(unitsize * self.resol * it+1)
                test_region_end1 = np.uint64(unitsize * self.resol * (it+1))
                test_region_start2 = np.uint64(unitsize * self.resol * it+1)
                test_region_end2 = np.uint64(unitsize * self.resol * (it+1)+(400*self.resol))
                if test_region_end2 > chrsize:
                    test_region_end2 = chrsize-1
                if test_region_end1 > chrsize - 400*self.resol:
                    test_region_end1 = chrsize - 400*self.resol

                position1 = str(chr) + ":" + str(test_region_start1) + "-" + str(test_region_end1)
                position2 = str(chr) + ":" + str(test_region_start2) + "-" + str(test_region_end2)
                mat = self.unbalLib.fetch(position2, position1)
                mat = nantozero(mat)
                mat = np.round(mat, 1)
                nrow = mat.shape[0]
                matsum = np.sum(mat, axis=1)
                zeroindex = np.where(matsum == 0)
                pool = [x for x in list(range(nrow)) if x not in zeroindex[0].tolist()]
                n_pool.append(len(pool))
                if len(pool) == 0:
                    del mat
                elif len(pool) < sss:
                    randval = random.choices(pool, k=len(pool))
                    tableft = np.zeros((400, len(pool)))
                    tabcenter = np.zeros((400, len(pool)))
                    tabright = np.zeros((400, len(pool)))

                    for i in range(len(pool)):
                        x = randval[i]
                        for j in range(0,400):
                            y = x + j
                            tableft[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x - background_up-background_size):(x - background_up)])
                            tabcenter[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x - background_up):(x + background_down)])
                            tabright[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x + background_down):(x + background_down+background_size)])
                    bgleft_temp = np.subtract(tabcenter, tableft)
                    bgright_temp = np.subtract(tabcenter, tabright)
                    bgleft = np.column_stack((bgleft, bgleft_temp))
                    bgright = np.column_stack((bgright, bgright_temp))
                    del mat
                else:
                    randval = random.choices(pool, k=sss)
                    tableft = np.zeros((400, sss))
                    tabcenter = np.zeros((400, sss))
                    tabright = np.zeros((400, sss))

                    for i in range(sss):
                        x = randval[i]
                        for j in range(0, 400):
                            y = x + j
                            tableft[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x - background_up - background_size):(x - background_up)])
                            tabcenter[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x - background_up):(x + background_down)])
                            tabright[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x + background_down):(x + background_down+background_size)])
                    bgleft_temp = np.subtract(tabcenter, tableft)
                    bgright_temp = np.subtract(tabcenter, tabright)
                    del mat
                    bgleft = np.column_stack((bgleft, bgleft_temp))
                    bgright = np.column_stack((bgright, bgright_temp))

            depl = np.uint64(ss - bgleft.shape[1])
            if depl > 0:
                rich = np.argmax(n_pool)
                test_region_start1 = np.uint64(unitsize * self.resol * rich+1)
                test_region_end1 = np.uint64(unitsize * self.resol * (rich+1))
                test_region_start2 = np.uint64(unitsize * self.resol * rich+1)
                test_region_end2 = np.uint64(unitsize * self.resol * (rich+1)+(400*self.resol))
                if test_region_end2 > chrsize:
                    test_region_end2 = chrsize-1
                if test_region_end1 > chrsize - 400*self.resol:
                    test_region_end1 = chrsize - 400*self.resol

                position1 = str(chr) + ":" + str(test_region_start1) + "-" + str(test_region_end1)
                position2 = str(chr) + ":" + str(test_region_start2) + "-" + str(test_region_end2)
                mat = self.unbalLib.fetch(position2, position1)
                mat = nantozero(mat)
                mat = np.round(mat, 1)
                nrow = mat.shape[0]
                matsum = np.sum(mat, axis=1)
                zeroindex = np.where(matsum == 0)
                pool = [x for x in list(range(nrow)) if x not in zeroindex[0].tolist()]
                randval = random.choices(pool, k=depl)
                tableft = np.zeros((400, depl))
                tabcenter = np.zeros((400, depl))
                tabright = np.zeros((400, depl))

                for i in range(depl):
                    x = randval[i]
                    for j in range(0, 400):
                        y = x + j
                        tableft[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x - background_up - background_size):(x - background_up)])
                        tabcenter[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x - background_up):(x + background_down)])
                        tabright[j, i] = np.mean(mat[(y - background_up):(y + background_down), (x + background_down):(x + background_down+background_size)])
                bgleft_temp = np.subtract(tabcenter, tableft)
                bgright_temp = np.subtract(tabcenter, tabright)
                del mat
                bgleft = np.column_stack((bgleft, bgleft_temp))
                bgright = np.column_stack((bgright, bgright_temp))

                return bgleft, bgright
        # apply parallel.
        print('2. Constituting background ... \n')
        result = Parallel(n_jobs=self.core)(delayed(main_null_calc)(chr) for chr in tqdm(chromnames2))
        bgleft = np.zeros((400,0))
        bgright = np.zeros((400,0))
        for i in range(len(result)):
            if(type(result[i]) == type(None)):
                continue
            else:
                bl,br = result[i]
                bgleft=np.column_stack((bgleft,bl))
                bgright=np.column_stack((bgright,br))

        print('Elapsed time for background estimation: ' + str(np.round((time.time() - t_background_start) / 60, 3)) + ' min')
        return bgleft, bgright


    def pvalue(self, bgleft, bgright, df):
        np.seterr(divide='ignore', invalid='ignore')
        PVAL = []
        dfsize = len(df)
        for i in range(dfsize):
            chr = df['chr'].iloc[i]
            chr = str(chr)
            chrLen = self.chromnames2sizes[chr]
            pos1 = df['pos1'].iloc[i]
            pos2 = df['pos2'].iloc[i]
            pos3 = df['pos3'].iloc[i]
            pos4 = df['pos4'].iloc[i]
            leftmost = pos1 - 5 * self.resol
            rightmost = pos2 + 5 * self.resol
            if leftmost < 1:
                leftmost = 1
            if rightmost > chrLen:
                rightmost = chrLen
            cd1 = chr + ":" + str(leftmost) + "-" + str(rightmost)
            cd2 = chr + ":" + str(pos3) + "-" + str(pos4)
            mat = self.unbalLib.fetch(cd2, cd1)
            mat_center = mat[:, 5:-5]
            mat_left = mat[:, :5]
            mat_right = mat[:, -5:]

            mat_center = nantozero(mat_center)
            mat_left = nantozero(mat_left)
            mat_right = nantozero(mat_right)

            center = np.mean(mat_center, axis=1)
            left = np.mean(mat_left, axis=1)
            right = np.mean(mat_right, axis=1)

            left_diff = np.subtract(center, left)
            right_diff = np.subtract(center, right)

            pvalues = []

            x1 = (pos1 - 1) / self.resol
            x2 = pos2 / self.resol
            y1 = (pos3 - 1) / self.resol
            y2 = pos4 / self.resol

            for j in range(len(center)):
                if x1 == y1:  # downward stripe
                    difference = j
                elif x2 == y2:  # upward stripe
                    difference = y2 - y1 - j
                if difference >= 400:
                    difference = 399
                difference = int(difference)
                bleft = bgleft[difference, :]
                bright = bgright[difference, :]
                p1 = len(np.where(bleft >= left_diff[j])[0]) / len(bleft)
                p2 = len(np.where(bright >= right_diff[j])[0]) / len(bright)
                pval = max(p1, p2)
                if pval == 0:
                    pval = 1/len(bleft)
                pvalues.append(pval)
            PVAL.append(np.median(pvalues))
        return PVAL

    def pvalue_test(self, bgleft, bgright, df):
        np.seterr(divide='ignore', invalid='ignore')
        PVAL = []
        dfsize = len(df)
        for i in range(dfsize):
            chr = df['chr'].iloc[i]
            pos1 = df['pos1'].iloc[i]
            pos2 = df['pos2'].iloc[i]
            pos3 = df['pos3'].iloc[i]
            pos4 = df['pos4'].iloc[i]
            medpixel = df['medpixel'].iloc[i]
            cd1 = chr + ":" + str(pos1 - 5 * self.resol) + "-" + str(pos2 + 5 * self.resol)
            cd2 = chr + ":" + str(pos3) + "-" + str(pos4)
            mat = self.unbalLib.fetch(cd2, cd1)
            mat_center = mat[:, 5:-5]
            mat_left = mat[:, :5]
            mat_right = mat[:, -5:]

            mat_center = nantozero(mat_center)
            mat_left = nantozero(mat_left)
            mat_right = nantozero(mat_right)

            center = np.mean(mat_center, axis=1)
            left = np.mean(mat_left, axis=1)
            right = np.mean(mat_right, axis=1)

            center = signal.medfilt(center, 3)
            left = signal.medfilt(left, 3)
            right = signal.medfilt(right, 3)

            left_diff = np.subtract(center, left)
            right_diff = np.subtract(center, right)

            pcrit = []
            pvalues = []
            nomore = 0

            x1 = (pos1 - 1) / self.resol
            x2 = pos2 / self.resol
            y1 = (pos3 - 1) / self.resol
            y2 = pos4 / self.resol

            for j in range(len(center)):
                if x1 == y1:  # downward stripe
                    difference = j
                elif x2 == y2:  # upward stripe
                    difference = y2 - y1 - j
                difference = int(difference)
                bleft = bgleft[difference, :]
                bright = bgright[difference, :]
                p1 = len(np.where(bleft >= left_diff[j])[0]) / len(bleft)
                p2 = len(np.where(bright >= right_diff[j])[0]) / len(bright)
                pval = max(p1, p2)
                if pval == 0:
                    pval = 0.001
                pvalues.append(pval)
            pvalues_flip = pvalues[::-1]
            pvalue_smooth = signal.medfilt(pvalues, 3)
            pvalues_flip_smooth = signal.medfilt(pvalues_flip, 3)
            N = len(pvalue_smooth)
            for j in range(len(center)):
                if x1 == y1:
                    k = j
                elif x2 == y2:
                    k = N - j - 1
                if center[k] > medpixel and pvalue_smooth[k] < 0.5:
                    pcrit.append(1)
                elif center[k] > medpixel and pvalue_smooth[k] >= 0.5:
                    if nomore != 0:
                        pcrit.append(0)
                    else:
                        pcrit.append(1)
                elif center[k] < medpixel:
                    if nomore == 0:
                        nomore = 1
                    pcrit.append(0)

            zeros = [i for i in range(len(pcrit)) if pcrit[i] == 0]

            PVAL.append(np.median(pvalues))
        return PVAL

    def scoringstripes(self, df, mask='0'):
        background_size = 50000/self.resol
        background_size = int(background_size)

        if mask != '0':
            mask = mask.split(':')
            mask_chr = mask[0]
            mask_start = int(mask[1].split('-')[0])
            mask_end = int(mask[1].split('-')[1])

        def iterate_idx(i,is_mask):
            np.seterr(divide='ignore', invalid='ignore')
            x_start_index = int((df['pos1'].iloc[i] - 1) / self.resol)
            x_end_index = int(df['pos2'].iloc[i] / self.resol)
            if is_mask:
                mask_x_start = int(mask_start / self.resol)
                mask_x_end = int(mask_end / self.resol)
            y_start_index = int((df['pos3'].iloc[i] - 1) / self.resol)
            y_end_index = int(df['pos4'].iloc[i] / self.resol)

            leftmost = x_start_index - background_size
            rightmost = x_end_index + background_size
            if leftmost < 1:
                leftmost = 1
            if rightmost > normmat.shape[0]:
                rightmost = normmat.shape[0]-1

            if not is_mask:
                center = extract_from_matrix(normmat, x_start_index, x_end_index, y_start_index, y_end_index)
            else:
                center = extract_from_matrix(normmat, x_start_index, x_end_index, y_start_index, y_end_index, mask_x_start, mask_x_end)
            left = extract_from_matrix(normmat, leftmost, x_start_index, y_start_index, y_end_index)
            right = extract_from_matrix(normmat, x_end_index, rightmost, y_start_index, y_end_index)

            centerm = np.nanmean(center, axis=1)
            leftm = np.nanmean(left, axis=1)
            rightm = np.nanmean(right, axis=1)

            g_xl = stats.elementwise_product_sum(K_xl, leftm, centerm)
            g_xr = stats.elementwise_product_sum(K_xr, centerm, rightm)
            g_y = stats.elementwise_product_sum(K_y, leftm, centerm, rightm)
            g_x = np.minimum(g_xl, g_xr)
            diff = [a - b for a, b in zip(g_x, g_y)]
            avgdiff = np.nanmean(diff)
            g = np.nanmedian(centerm) * avgdiff
            return i,g

        # Scoring
        ### Sobel-like operators
        listg = [0 for x in range(df.shape[0])]
        K_xl = np.array([[-1, 1], [-2, 2], [-1, 1]])
        K_xr = np.array([[1, -1], [2, -2], [1, -1]])
        K_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        chrset = list(set(df['chr']))
        for c in chrset:
            is_mask = False
            if mask!='0':
                is_mask = mask_chr == c
            t0 = time.time()
            idx = np.where(df['chr'] == c)[0].tolist()
            mat = self.unbalLib.fetch(str(c))
            mat = nantozero(mat)
            mat = np.round(mat,1)
            print('Time for loading '+str(c)+' matrix: '+str(np.round(time.time()-t0, 3)) + 's.')

            t0 = time.time()
            normmat = stats.observed_over_expected(mat)
            normmat = normmat[0]
            del mat
            print('Time for distance decay-normalization: ' + str(np.round(time.time() - t0, 3)) + 's.')
            result = Parallel(n_jobs=self.core)(delayed(iterate_idx)(i,is_mask) for i in tqdm(idx))
            del normmat
            for r in range(len(result)):
                i,g = result[r]
                listg[i] = g
        return listg

    def extract(self, mp, bgleft, bgright):
        np.seterr(divide='ignore', invalid='ignore')
        def search_frame(idx):
            start = idx * 200 - 100
            end = (idx + 1) * 200 + 99
            if end >= rowsize:
                end = rowsize - 1
            if idx == 0:
                start = 0

            framesize = end - start + 1
            start_array = [(start + j) * self.resol + 1 for j in range(framesize)]
            end_array = [s + self.resol - 1 for s in start_array]
            last = end_array[-1]
            if last >= self.chromsizes[chridx]:
                end_array[-1] = self.chromsizes[chridx]
            locus = chr + str(":") + str(start_array[0]) + str('-') + str(end_array[-1])
            D = self.unbalLib.fetch(locus, locus)
            D = nantozero(D)

            # Remove rows and columns containing only zero.
            colsum = np.sum(D, axis=0)
            # rowsum = np.sum(D, axis=1) # rowsum == colsum
            nonzero_idx = np.where(colsum != 0)  # data type: tuple
            nonzero_idx = nonzero_idx[0]
            framesize = len(nonzero_idx)
            if framesize > 10:
                D = D[np.ix_(nonzero_idx, nonzero_idx)]
                start_array = [start_array[s] for s in nonzero_idx]
                end_array = [end_array[s] for s in nonzero_idx]
                temp_res = self.StripeSearch(D, idx, start, end, M, mp, chr, framesize, start_array, end_array)
                return(temp_res)
            else:
                return 0

        result = pd.DataFrame(columns=['chr', 'pos1', 'pos2', 'chr2', 'pos3', 'pos4', 'length', 'width', 'total', 'Mean',
                     'maxpixel', 'num', 'start', 'end', 'x', 'y', 'h', 'w', 'medpixel'])
        for chridx in range(len(self.chromnames)):
            t_chr_search = time.time()
            chr = self.chromnames[chridx]
            print('Chromosome: ' + str(chr) + " / Maximum pixel: " + str(round(mp*100,3))+"%")
            cfm = self.unbalLib.fetch(chr)  # cfm : contact frequency matrix
            cfm = np.round(cfm,1)
            M = np.quantile(a=cfm[cfm > 0], q=mp, interpolation='linear')
            rowsize = cfm.shape[0]
            del cfm

            nframes = math.ceil(rowsize / 200)

            results = Parallel(n_jobs = self.core)(delayed(search_frame)(i) for i in tqdm(range(nframes)))

            for n in range(len(results)):
                if type(results[n]) == int:
                    pass
                else:
                    result = result.append(results[n])

        res = self.RemoveRedundant(result, 'size')
        res = res.reset_index(drop=True)

        # Stripe filtering and scoring
        # res2 = self.scoringstripes(res)
        p = self.pvalue(bgleft, bgright, res)
        #s = self.scoringstripes(res)
        res = res.assign(pvalue=pd.Series(p))
        #res = res.assign(Stripiness=pd.Series(s[5]))

        return res

    def StripeSearch(self, submat, num, start, end, M, mp, chr, framesize, start_array, end_array):
        np.seterr(divide='ignore', invalid='ignore')
        res_chr = [];
        res_pos1 = [];
        res_pos2 = [];
        res_pos3 = [];
        res_pos4 = [];
        res_length = [];
        res_width = [];
        res_total = [];
        res_Mean = [];
        res_maxpixel = [];
        res_num = [];
        res_start = [];
        res_end = [];
        res_x = [];
        res_y = [];
        res_h = [];
        res_w = [];
        res_medpixel = []
        medpixel = np.quantile(a=submat[submat > 0], q=0.5)
        st = start
        en = end
        S = framesize
        red = np.ones((framesize, framesize)) * 255
        blue = 255 * (M - submat) / M
        blue[np.where(blue < 0)] = 0
        green = blue

        img = cv.merge((red / 255, green / 255, blue / 255))
        img = np.clip(img, a_min=0, a_max=1)
        # plt.subplot(111),plt.imshow(img),plt.title('original'), plt.show()

        for b in np.arange(0.5, 1.01, 0.1):  # b: brightness parameter
            test_column = []
            end_points = []
            start_points = []
            updown = []  # up = 1, down = 2
            adj = ImageProcessing.imBrightness3D(img, In=([0.0, 0.0, 0.0], [1.0, b, b]),
                                                 Out=([0.0, 0.0, 0.0], [1.0, 1.0, 1.0]))
            # plt.subplot(111), plt.imshow(adj), plt.title('Brightened'), plt.show()
            kernel = np.ones((3, 3)) / 9
            blur = cv.filter2D(adj, -1, kernel)
            blur = np.clip(blur, a_min=0, a_max=1)
            # plt.subplot(111), plt.imshow(blur), plt.title('Blurry'), plt.show()
            gray = cv.cvtColor(np.float32(blur), cv.COLOR_RGB2GRAY)
            # gray = np.uint8(gray*255)
            # edges = ImageProcessing.Canny(gray, threshold = 0.3)
            edges = feature.canny(gray, sigma=self.canny)
            # plt.subplot(111), plt.imshow(edges, cmap='gray'), plt.title('Canny edge detection'), plt.show()
            vert = ImageProcessing.verticalLine(edges, L=60, H=120)
            # plt.subplot(111), plt.imshow(vert, cmap='gray'), plt.title('Vertical line detection'), plt.show()
            LL = []
            for c in range(S):
                # t1 = time.time()
                line_length, END = ImageProcessing.block(vert, c)
                # print(time.time()-t1)
                LL.append(line_length)
                above = min(c, END)
                bottom = max(c, END)
                seq = list(range(above, bottom + 1, 1))

                if line_length > self.minH and sum(vert[seq, c]) != 0:
                    test_column.append(c)
                    end_points.append(END)
                    start_points.append(c)
                    if END > c:
                        updown.append(2)
                    else:
                        updown.append(1)

            Pair = []
            MIN_vec = []
            MAX_vec = []
            for ud in [1, 2]:
                testmat = np.zeros((S, S), dtype=np.uint8)
                udidx = [i for i in range(len(updown)) if updown[i] == ud]
                for c in udidx:
                    st = test_column[c]
                    en = end_points[c]
                    if ud == 1:
                        en_temp = st
                        st = en
                        en = en_temp
                    testmat[st:en, test_column[c]] = 1
                # line refinement
                for r in range(S):
                    vec = testmat[r, :]
                    K1 = vec[1:S] > vec[0:(S - 1)]
                    K2 = vec[1:S] < vec[0:(S - 1)]
                    st = [i + 1 for i in range(len(K1)) if K1[i]]
                    en = [i for i in range(len(K2)) if K2[i]]
                    if vec[0] == 1:
                        st.insert(0, 0)
                    if vec[S - 1] == 1:
                        en.insert(len(en), S - 1)

                    nLines = len(st)

                    for L in range(nLines):
                        origLine = edges[r, list(range(st[L], en[L] + 1, 1))]
                        SUM = sum(origLine)
                        if SUM > 0:
                            testmat[r, st[L]:en[L]] = vert[r, st[L]:en[L]]
                        else:
                            MED = int(np.round(stat.median([st[L] + en[L]]) / 2))
                            testmat[r, st[L]:en[L]] = 0
                            testmat[r, MED] = 1
                fused_image = np.dstack((edges, testmat, testmat))

                [_, Y] = np.where(testmat == 1)
                uniqueCols = list(set(Y))
                ps = pd.Series(Y)
                counts = ps.value_counts().sort_index()
                counts = counts.to_frame(name='length')
                start_points_ud = [start_points[i] for i in udidx]
                end_points_ud = [end_points[i] for i in udidx]
                intersectidx = [i for i in range(len(start_points_ud)) if start_points_ud[i] in uniqueCols]
                start_points_ud = [start_points_ud[i] for i in intersectidx]
                end_points_ud = [end_points_ud[i] for i in intersectidx]

                counts['end_points'] = end_points_ud

                counts = counts[counts['length'] >= 3]
                nrow = counts.shape[0]
                meanX = []
                Continuous = []
                isContinue = False
                Len = []

                for c in range(nrow - 1):
                    Current = counts.index[c]
                    Next = counts.index[c + 1]

                    if Next - Current == 1 and isContinue:
                        Continuous.append(Next)
                        Len.append(counts.iloc[c + 1]['length'])
                    elif Next - Current == 1 and not isContinue:
                        Continuous = [Current, Next]
                        Len = [counts.iloc[c]['length'], counts.iloc[c + 1]['length']]
                        isContinue = True
                    elif Next - Current != 1 and not isContinue:
                        Continuous = [Current]
                        Len = [counts.iloc[c]['length']]
                        Len = [a / sum(Len) for a in Len]
                        isContinue = False
                        temp = sum([a * b for a, b in zip(Continuous, Len)])
                        meanX.append(np.round(temp))
                    else:
                        Len = [a / sum(Len) for a in Len]
                        temp = sum([a * b for a, b in zip(Continuous, Len)])
                        meanX.append(np.round(temp))
                        Continuous = [Current]
                        Len = [counts.iloc[c]['length']]
                        isContinue = False
                Len = [a / sum(Len) for a in Len]
                temp = sum([a * b for a, b in zip(Continuous, Len)])
                meanX.append(np.round(temp))

                X = list(set(meanX))
                X.sort()
                Xsize = len(X)

                for c in range(Xsize - 1):
                    n = int(X[c])
                    m = int(X[c + 1])
                    st1 = np.where(testmat[:, n] == 1)[0]
                    en1 = st1.max()
                    st1 = st1.min()
                    st2 = np.where(testmat[:, m] == 1)[0]
                    en2 = st2.max()
                    st2 = st2.min()
                    '''
                    max_width_dist1.append(abs(m - n))
                    if c == 0:
                        max_width_dist2.append(abs(m - n))
                    else:
                        l = int(X[c - 1])
                        minw = min(abs(m - n), abs(n - l))
                        if max_width_dist2[-1] == minw:
                            continue
                        else:
                            max_width_dist2.append(minw)
                    '''
                    if abs(m - n) > 1 and abs(m - n) <= self.maxW:
                        Pair.append((n, m))
                        [a1, _] = np.where(testmat[:, range(max(0, n - 1), min(n + 2, S), 1)] == 1)
                        MIN1 = a1.min()
                        MAX1 = a1.max()
                        [a2, _] = np.where(testmat[:, range(max(0, m - 1), min(m + 2, S), 1)] == 1)
                        MIN2 = a2.min()
                        MAX2 = a2.max()

                        MIN = min(MIN1, MIN2)
                        MAX = max(MAX1, MAX2)

                        if ud == 1:
                            MAX = X[c + 1]
                        else:
                            MIN = X[c]
                        MIN_vec.append(MIN)
                        MAX_vec.append(MAX)
            PairSize = len(Pair)

            for c in range(PairSize):
                x = Pair[c][0]
                y = int(MIN_vec[c])
                w = int(Pair[c][1] - Pair[c][0] + 1)
                h = int(MAX_vec[c] - MIN_vec[c] + 1)

                res_chr.append(chr)
                res_pos1.append(start_array[x])
                res_pos2.append(end_array[x + w - 1])
                res_pos3.append(start_array[y])
                res_pos4.append(end_array[y + h - 1])
                res_length.append(end_array[y + h - 1] - start_array[y] + 1)
                res_width.append(end_array[x + w - 1] - start_array[x] + 1)
                res_total.append(submat[y:(y + h), x:(x + w)].sum())
                res_Mean.append(submat[y:(y + h), x:(x + w)].sum() / h / w)
                res_maxpixel.append(str(mp * 100) + '%')
                res_num.append(num)
                res_start.append(start)
                res_end.append(end)
                res_x.append(x)
                res_y.append(y)
                res_h.append(h)
                res_w.append(w)
                res_medpixel.append(medpixel)

        result = pd.DataFrame(
            {'chr': res_chr, 'pos1': res_pos1, 'pos2': res_pos2, 'chr2': res_chr, 'pos3': res_pos3, 'pos4': res_pos4,
             'length': res_length, 'width': res_width, 'total': res_total, 'Mean': res_Mean,
             'maxpixel': res_maxpixel, 'num': res_num, 'start': res_start, 'end': res_end,
             'x': res_x, 'y': res_y, 'h': res_h, 'w': res_w, 'medpixel': res_medpixel})

        result = self.RemoveRedundant(result, 'size')

        return result

    def RemoveRedundant(self, df, by):
        def clean(n):
            delidx=[]
            n_idx = np.where(subdf['num'] == n)[0]
            n2_idx = np.where(subdf['num'] == n + 1)[0]
            n_idx = np.concatenate((n_idx, n2_idx))
            n_idx.sort()
            L = len(n_idx)
            for i in range(L - 1):
                for j in range(i + 1, L):
                    ii = c_idx[n_idx][i]
                    jj = c_idx[n_idx][j]

                    A_x_start = list_pos1[ii]
                    A_x_end = list_pos2[ii]
                    A_y_start = list_pos3[ii]
                    A_y_end = list_pos4[ii]

                    B_x_start = list_pos1[jj]
                    B_x_end = list_pos2[jj]
                    B_y_start = list_pos3[jj]
                    B_y_end = list_pos4[jj]

                    int_x = range(max(A_x_start, B_x_start), min(A_x_end, B_x_end) + 1)
                    int_y = range(max(A_y_start, B_y_start), min(A_y_end, B_y_end) + 1)

                    s_x = len(int_x) / min(A_x_end - A_x_start, B_x_end - B_x_start)
                    s_y = len(int_y) / min(A_y_end - A_y_start, B_y_end - B_y_start)

                    if s_x > 0.2 and s_y > 0.2:
                        if by == 'size':
                            if list_h[ii] * list_w[ii] <= list_h[jj] * list_w[jj]:
                                delidx.append(ii)
                            else:
                                delidx.append(jj)
                        elif by == 'score':
                            if list_stri[ii] <= list_stri[jj]:
                                delidx.append(ii)
                            else:
                                delidx.append(jj)
                        else:
                            if list_pval[ii] > list_pval[jj]:
                                delidx.append(ii)
                            else:
                                delidx.append(jj)
            return delidx

        if by != 'size' and by != 'score' and by != 'pvalue':
            raise ValueError('"by" should be one of "size", "pvalue" and "score"')
        df_size = df.shape
        row_size = df_size[0]
        if row_size == 0:
            return df
        else:
            delobj = [True for i in range(row_size)]
            list_chr = df['chr']
            list_pos1 = df['pos1'].tolist()
            list_pos2 = df['pos2'].tolist()
            list_pos3 = df['pos3'].tolist()
            list_pos4 = df['pos4'].tolist()
            list_h = df['h'].tolist()
            list_w = df['w'].tolist()
            if by == 'score':
                list_stri = df['Stripiness'].tolist()
            if by == 'pvalue':
                list_pval = df['pvalue'].tolist()
            unique_chr = list(set(list_chr))

            for c in unique_chr:
                c_idx = np.where(list_chr == c)[0]
                subdf = df.iloc[c_idx]
                unique_num = list(set(subdf['num']))
                unique_num.sort()
                res = Parallel(n_jobs=self.core)(delayed(clean)(n) for n in unique_num)
                for i in range(len(res)):
                    for j in res[i]:
                        delobj[j] = False

        idx = [a for a in range(row_size) if delobj[a]]
        result = df.iloc[idx]
        return result

    def selectColumn(self, df):
        list_chr = df['chr']
        list_pos1 = df['pos1'].tolist()
        list_pos2 = df['pos2'].tolist()
        list_pos3 = df['pos3'].tolist()
        list_pos4 = df['pos4'].tolist()

        if str(list_chr[0])[0] != 'c':
            if self.chromnames[0][0] == 'c':
                list_chr = ['chr'+str(x) for x in list_chr]
        MAX_POS=[]
        nrow = df.shape[0]
        for i in range(nrow):
            chr = list_chr[i]
            pos1 = list_pos1[i]
            pos2 = list_pos2[i]
            pos3 = list_pos3[i]
            pos4 = list_pos4[i]

            x_str = str(chr)+':'+str(pos1)+'-'+str(pos2)
            y_str = str(chr)+':'+str(pos3)+'-'+str(pos4)
            mat = self.unbalLib.fetch(x_str,y_str)
            average = np.mean(mat,axis=1)
            which_max = np.argmax(average)
            max_pos = pos1 + self.resol * which_max
            MAX_POS.append(max_pos)


        return MAX_POS


def nantozero(nparray):
    where_are_nans = np.isnan(nparray)
    nparray[where_are_nans] = 0
    return nparray


def extract_from_matrix(matrix, x_start, x_end, y_start, y_end, mask_x_start = 0, mask_x_end = 0):
    x = list(range(x_start, x_end))
    x_mask = list(range(mask_x_start, mask_x_end))
    x = [i for i in x if i not in x_mask]
    xlen = len(x)
    y = list(range(y_start, y_end))
    y = [i for i in y if i not in x_mask]
    ylen = len(y)
    result = np.empty((ylen, xlen), dtype=float)
    for i in range(ylen):
        for j in range(xlen):
            result[i][j] = matrix[y[i]][x[j]]


    return result
