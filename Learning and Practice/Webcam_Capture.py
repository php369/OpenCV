import cv2 as cv

#Ascessing the webcam
capture = cv.VideoCapture(0)

#Reading the video from the webcam frame by frame
while True:
    isTrue, frame = capture.read()

    #Displaying the webcam video
    cv.imshow('Webcam Capture', frame)

    #Preventing infinite loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

#Dereferencing the capture pointer
capture.release()

#Destroying all open windows
cv.destroyAllWindows()