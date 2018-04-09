import cv2
import numpy as np
import sqlite3

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def getProfile(Id):
    connection = sqlite3.connect("faceDatabase.db")
    cmd = "SELECT * FROM people WHERE Id=" + str(Id)
    cursor = connection.execute(cmd)
    profile = None
    for row in cursor:
        profile = row
    connection.close()
    return profile

fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (0, 0, 255)

Id = 0
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        [Id,conf] = recognizer.predict(gray[y:y+h,x:x+w])
        profile = getProfile(Id)
        if(profile != None and conf> 50):
            cv2.putText(im,str(profile[1]), (x,y+h),fontface, fontscale, fontcolor) 
        else:
            Id="Unknown"
            cv2.putText(im,str(Id), (x,y+h),fontface, fontscale, fontcolor) 
           
    cv2.imshow('im',im) 
    if(cv2.waitKey(10)  ==ord('q')):
        break
cam.release()
cv2.destroyAllWindows()