#!/usr/bin/env python

"""
    @title :        Main for Q3
    @description :  Find footprints in the database that match pieces of real footprints
    @output:        As many matches as possible
"""
from main.projectIM2020_q3 import *

q2_db = read_images("../images/q5/q2_db/*.png")
q4_db = read_images("../images/q5/q4_db/*.jpg")

for img in q2_db:
    search_engine(q4_db, img)