import cv2 as cv

#Reading Images
img = cv.imread('S:\Programming Practice\GitHub\OpenCV\Learning and Practice\Picture Library\Landscape.jpg')

#Displaying the image
cv.imshow('Sunflower', img)

cv.waitKey(0)
