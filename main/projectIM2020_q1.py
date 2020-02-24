#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
import glob
import cv2
import scipy.stats
import PIL.Image

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

def show_image(org, img):
    plt.subplot(121)
    plt.imshow(org, cmap='gray')
    plt.subplot(122)
    plt.imshow(img, cmap='gray')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def remove_ruler(image):
    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(gray, kernel, iterations=1)
    edges = cv2.Canny(erosion, 75, 150, apertureSize=3)
    # Detect points that form a line
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, minLineLength=500, maxLineGap=50)
    # Draw lines on the image
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)
    x1, y1, x2, y2 = lines[len(lines) - 1][0]
    print('x1:' + str(x1) + ' y1:' + str(y1) + ' x2:' + str(x2) + ' y2:' + str(y2))
    return img

def detect_chess(image):
    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 100, 550)
    ret, thresh = cv2.threshold(edged, 75, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    return img

def main():
    pictures = read_images()
    show_image(pictures[0], detect_chess(pictures[0]))
main()
