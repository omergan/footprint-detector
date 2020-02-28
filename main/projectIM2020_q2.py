#!/usr/bin/env python
import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

"""
    @title :        Main for Q2
    @description :  Finding circle patterns on footprints
    @output:        All footprints with marked circles if exist
"""

def read_images():
    filenames = [img for img in glob.glob("../images/q2/*.png")]
    images = []
    for filename in filenames:
        images.append(cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB))
    return images

def detect_circles(orig):
    img = orig.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bilateral_filtered_image = cv2.bilateralFilter(img, 5, 175, 175)
    circles = cv2.HoughCircles(bilateral_filtered_image, cv2.HOUGH_GRADIENT, 1.2, 75, minRadius=20, maxRadius=60)

    if circles is not None:
        print("Circles found")
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(img, (x - 4, y - 4), (x + 4, y + 4), (0, 128, 255), -1)

    return img

def show_image(orig, img):
    plt.subplot(231), plt.imshow(orig, cmap='gray'), plt.title("Original")
    plt.subplot(232), plt.imshow(img, cmap='gray'), plt.title("Circles")
    plt.subplot(233), plt.imshow(orig, cmap='gray'), plt.title("Original")
    plt.subplot(234), plt.imshow(img, cmap='gray'), plt.title("Circles")
    plt.subplot(235), plt.imshow(orig, cmap='gray'), plt.title("Original")
    plt.subplot(236), plt.imshow(img, cmap='gray'), plt.title("Circles")
    plt.show()

images = read_images()
detected = []
for image in images:
    detected.append(detect_circles(image))