import numpy as np
from matplotlib import image as mpimg
from sklearn.cluster import KMeans
import os

def compress_image(img,k):
    
    if img.max() <= 1:
        img = (img * 255).astype(np.uint8)

    # Check if the image is grayscale
    if len(img.shape) == 2:
        img = np.stack([img] * 3, axis=-1)  # Convert grayscale to RGB


    pixels = img.reshape(-1, 3)


    kmeans = KMeans(n_clusters=k, random_state=42, max_iter=1000)
    kmeans.fit(pixels)


    print("Cluster centers:\n", kmeans.cluster_centers_)
    print("Labels:\n", kmeans.labels_)

    # Assign the new colors to the pixels
    new_pixels = kmeans.cluster_centers_[kmeans.labels_]

    # Reshape back to the original image shape
    compressed_img = new_pixels.reshape(img.shape).astype(np.uint8)
    compressed_img_path = "compressed_image.png"
    mpimg.imsave(compressed_img_path, compressed_img)

    file_size_kb = os.path.getsize(compressed_img_path) / 1024
    return compressed_img,  round(file_size_kb, 2)
