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
        images.append(cv2.imread(filename))
    return images

def detect_circles(orig):
    img = orig.copy()
    temp = orig.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bilateral_filtered_image = cv2.bilateralFilter(img, 5, 175, 175)
    circles = cv2.HoughCircles(bilateral_filtered_image, cv2.HOUGH_GRADIENT, 1.2, 75, minRadius=20, maxRadius=60)
    color = (255, 255, 0)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(temp, (x, y), r, color, 10)
            cv2.rectangle(temp, (x - 4, y - 4), (x + 4, y + 4), (0, 128, 255), -1)

    return temp

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

plt.subplot(231), plt.imshow(images[6], cmap='gray'), plt.title("Original")
plt.subplot(232), plt.imshow(images[7], cmap='gray'), plt.title("Original")
plt.subplot(233), plt.imshow(images[8], cmap='gray'), plt.title("Original")
plt.subplot(234), plt.imshow(detected[6], cmap='gray'), plt.title("Circles")
plt.subplot(235), plt.imshow(detected[7], cmap='gray'), plt.title("Circles")
plt.subplot(236), plt.imshow(detected[8], cmap='gray'), plt.title("Circles")
plt.show()