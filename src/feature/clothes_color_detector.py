from sklearn.cluster import KMeans
import numpy as np


class ClothesColorDetector:
    def __init__(self):
        pass

    @staticmethod
    def detect_clothes_color(frame, region):
        x, y, w, h = region
        region_image = frame[y:y + h, x:x + w]
        height, width, dim = region_image.shape
        center_image = region_image[int(height / 4):int(3 * height / 4), int(width / 4):int(3 * width / 4), :]
        height, width, dim = center_image.shape

        img_vec = np.reshape(center_image, [height * width, dim])

        kmeans = KMeans(n_clusters=3)
        kmeans.fit(img_vec)
        unique_l, counts_l = np.unique(kmeans.labels_, return_counts=True)
        sort_ix = np.argsort(counts_l)
        sort_ix = sort_ix[::-1]

        color_s = []
        for cluster_center in kmeans.cluster_centers_[sort_ix]:
            color_s.append((int(cluster_center[0]), int(cluster_center[1]), int(cluster_center[2])))
        return color_s
