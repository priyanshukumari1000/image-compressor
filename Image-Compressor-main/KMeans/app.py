
import streamlit as st
import matplotlib.image as mpimg
import os
from Compressor import compress_image

st.title("Image Compression using KMeans")


st.write("Select number of color clusters for compression:")
st.write("Higher number of clusters results in better quality but larger file size.")
slider_value = st.slider('Select a number with a slider', min_value=0, max_value=50, value=16)


uploaded_file = st.file_uploader("Choose an image...")
if uploaded_file is not None:
    # Read the image file
    img = mpimg.imread(uploaded_file)
    compressed_img,size=compress_image(img,slider_value)
    compressed_img_path='compressed_image.png'
    original_size_kb = len(uploaded_file.getbuffer()) / 1024
    

    #preview images

    st.image(img, caption='Original Image', use_container_width =True)
    st.write(f"Original Image Size: {round(original_size_kb, 2)} KB")

    st.image(compressed_img, caption='Compressed Image', use_container_width =True)
    st.write(f"Compressed Image Size: {size} KB")

    #compression ratio
    compression_ratio = round(original_size_kb / size, 2)


    #download compressed file
    with open(compressed_img_path, "rb") as f:
        st.download_button(
            label="Download Compressed Image",
            data=f,
            file_name="compressed_image.png",
            mime="image/png"
        )
    os.remove(compressed_img_path)

