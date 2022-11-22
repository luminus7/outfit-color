from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import cv2
from os import path


class ClothesColorDetector:
    def __init__(self):
        pass

    @staticmethod
    def detect_clothes_color(image):
        height, width, dim = image.shape
        img = image[int(height / 4):int(3 * height / 4), int(width / 4):int(3 * width / 4), :]
        height, width, dim = img.shape

        img_vec = np.reshape(img, [height * width, dim])

        kmeans = KMeans(n_clusters=3)
        kmeans.fit(img_vec)
        unique_l, counts_l = np.unique(kmeans.labels_, return_counts=True)
        sort_ix = np.argsort(counts_l)
        sort_ix = sort_ix[::-1]

        color_s = []
        for cluster_center in kmeans.cluster_centers_[sort_ix]:
            color_s.append((int(cluster_center[2]), int(cluster_center[1]), int(cluster_center[0])))
        ClothesColorDetector.show_colors_through_graph(color_s)
        return color_s

    @staticmethod
    def show_colors_through_graph(color_s):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        x_from = 0.05
        for color in color_s:
            ax.add_patch(patches.Rectangle((x_from, 0.05), 0.29, 0.9, alpha=None,
                                           facecolor='#%02x%02x%02x' % (
                                               int(color[2]), int(color[1]),
                                               int(color[0]))))
            x_from = x_from + 0.31

        plt.show()
