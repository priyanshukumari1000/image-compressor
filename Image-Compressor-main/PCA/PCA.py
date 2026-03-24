from sklearn.decomposition import PCA
import numpy as np
from matplotlib import image as mpimg
#image compression using PCA
def compress_image_pca(img, n=2):
    if img.max() <= 1:
        img = (img * 255).astype(np.uint8)

    if len(img.shape) == 2:
        img = np.stack([img] * 3, axis=-1) 

    pixels = img.reshape(-1, 3)

    pca = PCA()
    pca.fit(pixels)
    cumsum = np.cumsum(pca.explained_variance_ratio_)
    d = np.argmax(cumsum >= 0.95) + 1
    print(f"Number of components to retain 95% variance: {d}")
    pc2 = PCA(n_components=d)
    pixels_reduced = pc2.fit_transform(pixels)
    # Inverse transform to get the compressed image
    compressed_pixels = pc2.inverse_transform(pixels_reduced)
    compressed_img = compressed_pixels.reshape(img.shape).astype(np.uint8)
    compressed_img_path = "compressed_image.png"
    mpimg.imsave(compressed_img_path, compressed_img)
    return compressed_img