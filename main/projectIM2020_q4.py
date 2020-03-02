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

images = read_images()
for img in images:
    
    detect_circles(img)