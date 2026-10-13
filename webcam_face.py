
#pip install opencv_python

import cv2

face_cap = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
if face_cap.empty():
    raise RuntimeError("Could not load the Haar cascade XML file")

video_cap = cv2.VideoCapture(0)
if not video_cap.isOpened():
    raise RuntimeError("Could not open the webcam. Check that no other app is using it.")

while True:
    ret, video_data = video_cap.read()
    if not ret:
        print("Failed to read a frame, stopping.")
        break

    gray = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(video_data, (x, y), (x + w, y + h), (0, 0, 255), 10)

    cv2.imshow("video_live", video_data)
    if cv2.waitKey(10) == ord("a"):
        break

video_cap.release()
cv2.destroyAllWindows()

"""""
import cv2
# haarcascade_frontalface_default.xml
a = cv2.CalibrateRobertson("haarcascade_frontalface_default.xml")

b = cv2.VideoCapture(0)

while True:
    c_rec,d_image = b.read()
    e = cv2.cvtColor(d_image,cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e,1.3,6)

    for (x1,y1,w1,h1) in f:
        cv2.rectangle(d_image,(x1,y1),(x1+w1),(y1+h1),(255,0,0), 5)

    cv2.imshow('img',d_image)
    h = cv2.waitKey(40) & 0xff
    if(h == 40):
        break
b.release()
cv2.destroyAllWindows()

    faces = face_cap.detecMultiScale(
        col,
        scalefactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
"""""