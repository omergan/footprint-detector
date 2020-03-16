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
    dst = cv2.fastNlMeansDenoisingColored(gray, None, 10, 10, 7, 21)
    equ = cv2.equalizeHist(dst)
    sharpened = cv2.filter2D(equ, -1, kernel_sharpening)
    thresh = cv2.adaptiveThreshold(sharpened, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    detect_circles(thresh)