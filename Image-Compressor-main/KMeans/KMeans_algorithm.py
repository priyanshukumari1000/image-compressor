import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

class KMeans:
    def __init__(self, k,max_iter=100):
        self.k = k
        self.max_iter = max_iter

    #initialize centroids randomly from the data points
    def centroid_init(self,X):
        random_indices = np.random.choice(X.shape[0], self.k, replace=False)
        return X[random_indices]
    
    #initialize centroids using k-means method

    def fit(self, X):
        self.cluster_centers_ = self.centroid_init(X)

        for _ in range(self.max_iter):
            distances=[]
            for point in X:
                d=[]
                for center in self.cluster_centers_:
                    d.append(np.sqrt(np.sum((point-center)**2)))
                distances.append(d)
            labels=[]
            for d in distances:
                labels.append(np.argmin(d))
            labels = np.array(labels)

            new_centroids=[]
            for i in range(self.k):
                points = X[labels == i]
                if len(points) > 0:
                    new_centroids.append(np.mean(points, axis=0))
                else:
                    new_centroids.append(self.cluster_centers_[i])
            new_centroids = np.array(new_centroids)

            if np.all(new_centroids == self.cluster_centers_):
                break
            self.cluster_centers_ = new_centroids
        self.labels_= labels
    
    #for predicting the labels of new data points
    def predict(self, X):
        labels=[]
        for point in X:
            d=[]
            for center in self.cluster_centers_:
                d.append(np.sqrt(np.sum((point-center)**2)))
            labels.append(np.argmin(d))
        return np.array(labels)



