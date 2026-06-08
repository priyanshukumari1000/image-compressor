# 📸 Image Compression Using PCA & K-Means Clustering

## 📖 Overview

This project implements an image compression system using **Principal Component Analysis (PCA)** and **K-Means Clustering**. The objective is to reduce image size while preserving as much visual information as possible.

Traditional images often contain redundant information that increases storage requirements. This project explores two machine learning techniques that efficiently compress images:

- **PCA (Principal Component Analysis):** Reduces image dimensionality while retaining the most important features.
- **K-Means Clustering:** Reduces the number of unique colors in an image through color quantization.

The project demonstrates how unsupervised learning techniques can be applied to real-world image processing tasks.

---

# ✨ Features

- Image compression using PCA.
- Image compression using K-Means Clustering.
- Preservation of important visual features.
- Color quantization for storage reduction.
- Side-by-side comparison of original and compressed images.
- Adjustable compression parameters.
- Visualization of compression results.

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| NumPy | Numerical Operations |
| OpenCV | Image Processing |
| Scikit-learn | PCA and K-Means Algorithms |
| Matplotlib | Visualization and Result Comparison |

---

# 🔬 Compression Techniques

## 1. Principal Component Analysis (PCA)

PCA is a dimensionality reduction technique that transforms image data into a lower-dimensional space while preserving maximum variance.

### Working

1. Convert image into matrix representation.
2. Compute principal components.
3. Retain only the most significant components.
4. Reconstruct the image using reduced dimensions.

### Benefits

- Reduces storage requirements.
- Preserves important image structures.
- Minimizes information loss.

---

## 2. K-Means Clustering

K-Means is an unsupervised learning algorithm used for color quantization.

### Working

1. Treat each pixel as a data point.
2. Group similar colors into K clusters.
3. Replace pixel values with cluster centroids.
4. Reconstruct image using reduced color palette.

### Benefits

- Reduces number of colors.
- Decreases memory usage.
- Maintains visual similarity.

---

# 🏗️ Project Architecture

```text
                    Input Image
                          │
                          ▼
                 Image Preprocessing
                          │
            ┌─────────────┴─────────────┐
            ▼                           ▼
      PCA Compression          K-Means Compression
            │                           │
            ▼                           ▼
    Compressed Image          Compressed Image
            └─────────────┬─────────────┘
                          ▼
                Result Visualization
                          ▼
                   Performance Analysis
```

---

# 📂 Project Structure

```text
Image-Compressor/
│
├── images/
│   ├── input/
│   └── output/
│
├── src/
│   ├── pca_compression.py
│   ├── kmeans_compression.py
│   ├── image_utils.py
│   └── visualization.py
│
├── requirements.txt
├── README.md
└── main.py
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/image-compressor.git
cd image-compressor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Usage

### Run PCA Compression

```bash
python pca_compression.py
```

### Run K-Means Compression

```bash
python kmeans_compression.py
```

### Run Complete Project

```bash
python main.py
```

---

# 📊 Example Parameters

### PCA

```python
n_components = 50
```

- Higher value → Better quality
- Lower value → Higher compression

### K-Means

```python
n_clusters = 16
```

- More clusters → Better quality
- Fewer clusters → Higher compression

---

# 📈 Results

| Method | Compression Strategy | Outcome |
|----------|---------------------|----------|
| PCA | Dimensionality Reduction | Preserves major image features |
| K-Means | Color Quantization | Reduces color diversity |
| PCA + K-Means | Hybrid Compression | Improved compression efficiency |

---

# 🎯 Key Highlights

- Implemented two popular machine learning algorithms for image compression.
- Reduced image dimensionality using PCA.
- Performed color quantization using K-Means clustering.
- Achieved compression with minimal visual quality degradation.
- Explored practical applications of unsupervised learning in image processing.
- Compared the effectiveness of different compression approaches.

---

# 💡 Applications

- Image storage optimization
- Data transmission systems
- Multimedia applications
- Computer vision preprocessing
- Machine learning pipelines
- Cloud storage optimization

---

# 🔮 Future Enhancements

- Add GUI for user interaction.
- Support batch image compression.
- Calculate PSNR and SSIM metrics.
- Implement hybrid PCA + K-Means pipeline.
- Support additional image formats.
- Add deep learning-based compression methods.

---

# 📚 Learning Outcomes

Through this project, I gained hands-on experience in:

- Principal Component Analysis (PCA)
- K-Means Clustering
- Unsupervised Machine Learning
- Image Processing
- Data Compression Techniques
- Python-based Machine Learning Development

---

# 👨‍💻 Author

### Priyanshu Kumari

B.Tech Computer Science Student

**Skills:** Machine Learning, Image Processing, Data Structures & Algorithms, Java, Python, C++

Feel free to contribute, raise issues, or suggest improvements.
