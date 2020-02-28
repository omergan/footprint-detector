#!/usr/bin/env python

"""
    @title :        Main for Q2
    @description :  Finding circle patterns on footprints
    @output:        All footprints with marked circles if exist
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob

def read_images():
    filenames = [img for img in glob.glob("../images/q2/*.png")]
    images = []
    for filename in filenames:
        images.append(cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB))
    return images

def detect_circles(orig):
    img = orig.copy()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.2, 100, maxRadius=60)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            cv2.circle(img, (x, y), r, (0, 255, 0), 4)
            cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

    show_image(orig, img)

def show_image(orig, img):
    plt.subplot(121), plt.imshow(orig, cmap='gray'), plt.title("Original")
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray'), plt.title("Circles")
    plt.xticks([]), plt.yticks([])
    plt.show()


images = read_images()
for image in images:
    detect_circles(image)