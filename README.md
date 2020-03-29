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
* Find circles using houghCircles
* If no circles are found, apply additional processing (erosion, canny)
* Use HoughCircles again (in an increasing accumulator magnitude), this will help detect smaller circles
* Draw the circles detected

## Part 3
#### Objective 
Finding a footprint in the database that matches a signature
#### Solution
* Use SIFT to find interest points on the image
* Use Flann algorithm to find matches
* Rate matching between signature and database
* Choose the best matched item

## Part 4
#### Objective 
Finding circle patterns on footprints in real images
#### Solution
* Preprocessing of the image (threshold, erosion)
* Use the algorithm from Part 2 to detect circles
* Draw the circles

## Part 5
#### Objective 
Finding footprints in the database that match signatures of real footprints
#### Solution
* Use algorithm of part 3
* ???
