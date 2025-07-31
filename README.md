# Handwritten Digit Recognition with CNN

## Project Overview

This project implements a Convolutional Neural Network (CNN) for handwritten digit recognition using the widely-used MNIST dataset. The goal is to classify handwritten digits (0-9) with high accuracy. The solution is developed in Python using TensorFlow and Keras.

## Features

* **CNN Architecture**: A robust CNN model designed for image classification tasks.
* **MNIST Dataset Integration**: Utilizes the popular MNIST dataset for training and evaluation.
* **Data Preprocessing**: Includes steps for normalizing pixel values and one-hot encoding labels.
* **Model Training & Evaluation**: Demonstrates the full machine learning pipeline, from model compilation to training and evaluation.
* **Prediction Visualization**: Visualizes sample predictions along with their true labels, highlighting misclassifications.
* **Model Persistence**: Saves the trained model for future use.

## Dataset

The project uses the **MNIST (Modified National Institute of Standards and Technology) dataset**.
* It consists of 60,000 training images and 10,000 testing images.
* Each image is a grayscale image of a handwritten digit, with a size of 28x28 pixels.
* The digits are centered and anti-aliased.

## Model Architecture

The CNN model used in this project is a sequential Keras model with the following layers:

1.  **`Conv2D` Layer**: Applies 2D convolution.
2.  **`MaxPooling2D` Layer**: Downsamples the input representation.
3.  **`Conv2D` Layer**: Another 2D convolution layer.
4.  **`MaxPooling2D` Layer**: Another downsampling layer.
5.  **`Flatten` Layer**: Flattens the 2D feature maps into a 1D vector.
6.  **`Dense` Layer (128 units)**: A fully connected layer with ReLU activation.
7.  **`Dropout` Layer (0.5 rate)**: Randomly sets input units to 0 with a frequency of rate at each step during training time, which helps prevent overfitting.
8.  **`Dense` Output Layer (10 units)**: A fully connected output layer with `softmax` activation for multi-class classification (0-9).

The model is compiled with the `adam` optimizer and `categorical_crossentropy` loss function.

## Requirements / Installation

To run this notebook, you'll need Python and the following libraries:

* `tensorflow`
* `keras` (usually comes with `tensorflow`)
* `numpy`
* `pandas`
* `matplotlib`

You can install these dependencies using pip:

```bash
pip install tensorflow numpy pandas matplotlib
