# Footprint Detector

## Part 1
#### Objective 
Finding the scales in the image and removing them
#### Solution
Removing the frame:
* Preprocessing of the image (grayscale, erosion)
* Detect edges using Canny
* Find lines using HoughLines
* Check which of the lines are the borders

Finding the scales:
* Apply threshold
* Find contours using cv.findContours
* Check which of the contours are in the right area size
* Convert a contour to a rectangle
* Draw corners according to rectangles that were found

## Part 2
#### Objective 
Finding circle patterns in footprints
#### Solution
PLACEHOLDER

## Part 3
#### Objective 
Finding a footprint in the database that matches a signature
#### Solution
PLACEHOLDER

## Part 4
#### Objective 
Finding circle patterns on footprints in real images
#### Solution
PLACEHOLDER

## Part 5
#### Objective 
Finding footprints in the database that match signatures of real footprints
#### Solution
PLACEHOLDER
