#!/usr/bin/env python
import numpy as np
from matplotlib import pyplot as plt
import glob
import cv2

"""
    @title :        Main for Q3
    @description :  Find a footprint in the database that matches a piece of a footprint
    @output:        Piece of the footprint and the full footprint
"""

def read_images():
    filenames = [img for img in glob.glob("../images/q3/*.png")]
    images = []
    for filename in filenames:
        images.append(cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB))
    return images

def show_image(org, img):
    plt.subplot(121)
    plt.imshow(org, cmap='gray')
    plt.subplot(122)
    plt.imshow(img, cmap='gray')
    # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def search_engine(database, search):
    working_copy = search.copy()
    kernel = np.ones((4, 4), np.uint8)
    match = []
    orb = cv2.ORB_create()
    gray_working_copy = cv2.cvtColor(working_copy, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_working_copy, 50, 150, apertureSize=3)
    kp1, des1 = orb.detectAndCompute(edges, None)
    for candidate in database:
        closing = cv2.morphologyEx(candidate, cv2.MORPH_CLOSE, kernel)
        candidate_edges = cv2.Canny(closing, 50, 150, apertureSize=3)
        kp2, des2 = orb.detectAndCompute(candidate_edges, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key=lambda x: x.distance)
        if len(matches) > len(match):
            match = candidate
    show_image(match, search)


images = read_images()
db = [images[1], images[3], images[4]]
search_engine(db, images[0])
# search_engine(db, images[2])