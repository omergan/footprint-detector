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

kernel = np.ones((3, 3), np.uint8)

images = read_images()
for img in images:
    temp = img.copy()
    gray = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)
    equ = cv2.equalizeHist(gray)
    sharpened = cv2.filter2D(equ, -1, kernel_sharpening)
    circles = cv2.HoughCircles(sharpened, cv2.HOUGH_GRADIENT, 1.2, 100, minRadius=20, maxRadius=60)

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            draw_circle(x, y, r, sharpened)
    show_image(equ, sharpened)
    # detect_circles(orig)