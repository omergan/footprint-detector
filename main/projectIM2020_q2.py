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
    # Pre precessing
    img = orig.copy()
    temp = orig.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bilateral_filtered_image = cv2.bilateralFilter(img, 5, 175, 175)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(img, kernel, iterations=1)
    edges = cv2.Canny(erosion, 50, 150, apertureSize=3)

    circles = cv2.HoughCircles(bilateral_filtered_image, cv2.HOUGH_GRADIENT, 1.2, 1, minRadius=20, maxRadius=60)
    color = (255, 255, 0)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(temp, (x, y), r, color, 3)
            cv2.rectangle(temp, (x - 4, y - 4), (x + 4, y + 4), (0, 128, 255), -1)

    else:
        radii = np.arange(0, 30, 10)
        for idx in range(len(radii) - 1):
            minRadius = radii[idx] + 1
            maxRadius = radii[idx + 1]
            circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 2.5, 25,
                                       param1=60, param2=75, minRadius=minRadius, maxRadius=maxRadius)
            if circles is None:
                continue
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                cv2.circle(temp, (x, y), r, color, 3)
                cv2.rectangle(temp, (x - 4, y - 4), (x + 4, y + 4), (0, 128, 255), -1)
    show_image(orig, temp)

def show_image(orig, img):
    plt.subplot(121), plt.imshow(orig, cmap='gray'), plt.title("Original")
    plt.subplot(122), plt.imshow(img, cmap='gray'), plt.title("Circles")
    plt.show()

images = read_images()
for image in images:
    detect_circles(image)