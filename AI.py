import cv2
from random import randrange as rd

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# takes data from xml file

cam = cv2.VideoCapture(0)
# 0 for defualt camera input

running = True

while running:
    successfull, frame = cam.read()
    # cam.read to read frame
    # unpacks actual frame and boolean value if success


    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # converts to gray_img for easier detection


    coordinates = face_data.detectMultiScale(gray_img)
    # gives coordinates of rectangles around face

    for x,y,w,h in coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (rd(255),rd(255),rd(255)), 3)

    # assigning coordinates to variables
    # coordinate of top left; coordinate of bottom right; color; thickness


    cv2.imshow('Face Detection', frame)
    key = cv2.waitKey(1)
    # waits 1 second and then takes another frame

    if key == 113:
        running = False
    # ascii code for letter q is 113
    # stops loop and camera


# cv2.VideoCapture(0) = captures video;
# cv2.imshow = image show
# cv2.waitKey = image remains open until a key is pressed
