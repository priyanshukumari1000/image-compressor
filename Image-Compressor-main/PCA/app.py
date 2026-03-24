
import streamlit as st
import numpy as np
import matplotlib.image as mpimg
import os
from PCA import compress_image_pca as compress_image_

st.title("Image Compression using KMeans")
st.write("Upload an image to compress it using KMeans clustering.")


uploaded_file = st.file_uploader("Choose an image...")
if uploaded_file is not None:
    # Read the image file
    img = mpimg.imread(uploaded_file)
    compressed_img=compress_image_(img)
    compressed_img_path='compressed_image.png'

    #preview images

    st.image(img, caption='Original Image', use_column_width=True)
    st.image(compressed_img, caption='Compressed Image', use_column_width=True)

    #download compressed file
    with open(compressed_img_path, "rb") as f:
        st.download_button(
            label="Download Compressed Image",
            data=f,
            file_name="compressed_image.png",
            mime="image/png"
        )
    os.remove(compressed_img_path)

