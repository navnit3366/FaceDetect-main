import cv2 as cv

img = cv.imread('photos/me01.jpg')
cv.imshow('Person', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray ,scaleFactor=1.1 , minNeighbors=2)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0), thickness=2)

cv.imshow('Deteced faces',img)

if len(faces_rect)>1:
    print("SwitchOFF the Machine with input 0 and Alarm Security")
else:
    print("SwitchON the machine send input value 1")
cv.waitKey(0)
