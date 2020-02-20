#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
import glob
import cv2

"""
    @title :        Main for Q1
    @description :  Finding scale and remove it
    @output:        Original, Scale with dots, No scale.
"""

def read_images():
    filenames = [img for img in glob.glob("../images/q1/*.jpg")]
    images = []
    for filename in filenames:
        images.append(cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB))
    return images

def show_image(img):
    plt.imshow(img)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def remove_ruler(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (1, 1), 0)
    edges = cv2.Canny(blur, 100, 200)
    return edges


def main():
    pictures = read_images()
    show_image(remove_ruler(pictures[0]))
main()
