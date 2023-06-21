import cv2 as cv

#Accessing Video
capture = cv.VideoCapture('S:\Programming Practice\GitHub\OpenCV\Learning and Practice\Video Library\Mountain.mp4')

#Reading Video frame by frame
while True:
    isTrue, frame = capture.read()

    #Displaying the video
    cv.imshow('Video', frame)

    #Preventing infinite loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#Dereferencing the capture pointer
capture.release()

#Destroying all open windows
cv.destroyAllWindows() 
