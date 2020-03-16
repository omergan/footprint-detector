"""
    @title :        Main for Q2
    @description :  Finding circle patterns on footprints in real images
    @output:        All footprints with marked circles if exist
"""
import glob
import cv2
from main.projectIM2020_q2 import *

def read_images():
    filenames = [img for img in glob.glob("../images/q4/*.jpg")]
    images = []
    for filename in filenames:
        images.append(cv2.imread(filename))
    return images

kernel_sharpening = np.array([[-1, -1, -1],
                              [-1, 11, -1],
                              [-1, -1, -1]])

kernel_3x3 = np.ones((3, 3), np.float32) / 9

kernel = np.ones((2, 2), np.uint8)

images = read_images()
for img in images:
    temp = img.copy()
    ret, thresh = cv2.threshold(img, 180, 220, cv2.THRESH_TOZERO)
    gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    erosion = cv2.erode(gray, kernel, iterations=2)
    erosion = cv2.cvtColor(erosion, cv2.COLOR_GRAY2BGR)
    circles = detect_circles(erosion, 1.5, 100, 20, 56)
    if circles is not None and len(circles) > 0:
        for (x, y, r) in circles:
            draw_circle(x, y, r, temp)
    show_image(img, temp)