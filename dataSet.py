import cv2
<<<<<<< HEAD
import sqlite3
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def createOrUpdatePeople(Id,name):
    connection = sqlite3.connect("faceDatabase.db")
    cmd= "SELECT * FROM people WHERE Id =" + str(Id)
    cursor = connection.execute(cmd)
    ifRecordExist = 0
    for row in cursor:
        ifRecordExist = 1
    if(ifRecordExist == 1):
        cmd = "UPDATE people SET name=" + str(name) + "WHERE Id =" + str(Id)
    else:
        cmd = "INSERT INTO people(Id,name) Values(" + str(Id) + "," + str(name) + ")"
    connection.execute(cmd)
    connection.commit() 
    connection.close()   


Id=input('Enter your id: ')
name = input('Enter name: ')
createOrUpdatePeople(Id,name)

=======
cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Id=input('Enter your id: ')
>>>>>>> d390bf551e39eb12ce93c9b3daf4bdad67972c82
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        
        #incrementing sample number 
        sampleNum=sampleNum+1
        #saving the captured face in the dataset folder
        cv2.imwrite("dataSet/User."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 20
    elif sampleNum>20:
        break
cam.release()
cv2.destroyAllWindows()