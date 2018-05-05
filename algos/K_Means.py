import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from scipy.io import loadmat

def find_closest_centroids(data, centroids):
    rows = data.shape[0]     # data is 300x2
    k = centroids.shape[0]   # how many clusters
    idx = np.zeros(rows)
    for i in range(rows):   # sample numbers
        min_dist = 1000000   # minimum distance
        for j in range(k):   # cluster numbers
            dist = np.sum((data[i,:] - centroids[j,:]) ** 2)   # distance from sample to cluster centers
            if dist < min_dist:
                # change to the min distance
                min_dist = dist
                # record the index
                idx[i] = j
    return idx

def compute_centroids(data, idx, k):
    rows, cols = data.shape
    centroids = np.zeros((k, cols))
    for i in range(k):
        indices = np.where(idx == i)
        # average the values of all the samples belong to this cluster and set the average value to new center
        centroids[i,:] = (np.sum(data[indices,:], axis=1) / len(indices[0])).ravel()
    return centroids

def run_k_means(data, initial_centroids, max_iters):
    rows, cols = data.shape
    k = initial_centroids.shape[0]
    idx = np.zeros(rows)
    centroids = initial_centroids
    for i in range(max_iters):
        idx = find_closest_centroids(data, centroids)
        centroids = compute_centroids(data, idx, k)
    return idx, centroids

# randomly select samples as the init centers
def init_centroids(data, k):
    rows, cols = data.shape
    centroids = np.zeros((k, cols)) # init cluster centers
    idx = np.random.randint(0, rows, k) # return values between 0 and rows with size k
    for i in range(k):
       centroids[i,:] = data[idx[i],:]
    return centroids

data = loadmat('K-Means-data.mat')
data = data['X']
initial_centers=init_centroids(data, 3)
idx, centroids = run_k_means(data, initial_centers, 1000)
cluster1 = data[np.where(idx == 0)[0],:]
cluster2 = data[np.where(idx == 1)[0],:]
cluster3 = data[np.where(idx == 2)[0],:]
fig, ax = plt.subplots(figsize=(12,8))
ax.scatter(cluster1[:,0], cluster1[:,1], s=30, color='r', label='Cluster 1')
ax.scatter(cluster2[:,0], cluster2[:,1], s=30, color='g', label='Cluster 2')
ax.scatter(cluster3[:,0], cluster3[:,1], s=30, color='b', label='Cluster 3')
ax.legend()
plt.show()