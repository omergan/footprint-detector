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
    filenames = [img for img in glob.glob("../images/q1/*.JPG")]
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

def remove_ruler(image):
    img = image.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(gray, kernel, iterations=1)
    edges = cv2.Canny(erosion, 50, 150, apertureSize=3)
    # Detect points that form a line
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 30, minLineLength=1000, maxLineGap=10)
    # Draw lines on the image
    x = 0
    y = img.shape[1]

    for line in lines:
        x1, y1, x2, y2 = line[0]
        if vertical_or_horizontal(line) == 'horizontal':
            if min(y1, y2) < y:
                y = min(y1, y2)
        elif vertical_or_horizontal(line) == 'vertical':
            if max(x1, x2) > x:
                x = max(x1, x2)
    return img[0:y, x:]

def vertical_or_horizontal(line):
    x1, y1, x2, y2 = line[0]
    if abs(x1 - x2) == 0:
        return 'vertical'
    m = abs(y1 - y2) / abs(x1 - x2)
    return 'vertical' if m > 1 else 'horizontal'

def chess_detection(image):
    img = image.copy()
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)
    thresh_holds = []
    _, thresh1 = cv2.threshold(gray, 75, 150, cv2.THRESH_BINARY_INV)
    _, thresh2 = cv2.threshold(gray, 75, 150, cv2.THRESH_BINARY)
    thresh3 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 5)
    thresh4 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 111, 0)

    thresh_holds.append(thresh1)
    thresh_holds.append(thresh2)
    thresh_holds.append(thresh3)
    thresh_holds.append(thresh4)

    rectangles = []

    for thresh in thresh_holds:
        _, contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for c in contours:
            # find bounding box coordinates
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.12 * peri, True)
            if len(approx) == 4:
                x, y, w, h = cv2.boundingRect(c)
                area = cv2.contourArea(c)
                # find minimum area
                if 500 < area < 20000:
                    rect = cv2.minAreaRect(c)
                    # calculate coordinates of the minimum area rectangle
                    box = cv2.boxPoints(rect)
                    # normalize coordinates to integers
                    box = np.int0(box)
                    # draw contours
                    cv2.drawContours(img, [box], 0, (0, 0, 255), 3)
                    rectangles.append(rect)

    for rect in rectangles:
        print(rect)
    return img

def main():
    # Read and rotate image if you need
    pictures = read_images()
    img_rotate_90_counterclockwise = cv2.rotate(pictures[1], cv2.ROTATE_90_COUNTERCLOCKWISE)

    # Rulers Removed
    # removed_1 = remove_ruler(pictures[0])
    # removed_2 = remove_ruler(img_rotate_90_counterclockwise)
    # removed_3 = remove_ruler(pictures[2])

    # Plotting Q1A
    # show_image(pictures[0], removed_1)
    # show_image(img_rotate_90_counterclockwise, removed_2)
    # show_image(pictures[2], removed_3)

    detected_1 = chess_detection(pictures[0])
    detected_2 = chess_detection(img_rotate_90_counterclockwise)
    detected_3 = chess_detection(pictures[2])

    # Plotting Q1B
    show_image(pictures[0], detected_1)
    show_image(img_rotate_90_counterclockwise, detected_2)
    show_image(pictures[2], detected_3)

main()
