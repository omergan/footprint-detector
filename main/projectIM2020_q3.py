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

names = []

def read_images(path):
    filenames = [img for img in glob.glob(path)]
    images = []
    for filename in filenames:
        names.append(filename)
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
    kernel = np.ones((1, 1), np.uint8)
    max = 0
    match = []
    orb = cv2.ORB_create()
    gray_working_copy = cv2.cvtColor(working_copy, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_working_copy, 50, 150, apertureSize=3)
    blur = cv2.GaussianBlur(img, (3, 3), 0)
    kp1, des1 = orb.detectAndCompute(blur, None)
    for i, candidate in enumerate(database):
        # closing = cv2.morphologyEx(candidate, cv2.MORPH_CLOSE, kernel)
        candidate_edges = cv2.Canny(candidate, 50, 150, apertureSize=3)
        kp2, des2 = orb.detectAndCompute(candidate, None)
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        # matches = sorted(matches, key=lambda x: x.distance)
        print(f'{len(matches)} {names[i + 6]}')
        if len(matches) > max:
            max = len(matches)
            match = database[i]
    show_image(search, match)


images = read_images("../images/q3/*.png")
db = read_images("../images/q2/*.png")
for img in images:
    search_engine(db, img)


