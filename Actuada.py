# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 19:02:39 2018
=================================================================

==================================================================
Author: Andres Mitre Ortiz

Email: andresmitre.fic@uas.edu.mx | andres18m@gmail.com

Linkedin: https://www.linkedin.com/in/andres18m

Twitter:  https://twitter.com/andres18m

                  Apache License
              Version 2.0, January 2004
            http://www.apache.org/licenses/

=================================================================

==================================================================

"""

import imutils
import serial
import cv2
import time

from datetime import datetime
import csv


# Load Haar cascade files:
path_cascade = "./haarcascades/"

face_cascade = cv2.CascadeClassifier(
    path_cascade + 'haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier(path_cascade + 'haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier(
    path_cascade + 'haarcascade_mcs_eyepair_big.xml')
# eye_cascade = cv2.CascadeClassifier(
#  path_cascade + 'haarcascade_eye_tree_eyeglasses.xml')


csv_path = "./CSV_files/"

# Data path
IAPS_img = "./IAPS_Images/"
Act_img = "./Act_Images/"

# Spontaneous dataset
Neutral_img = "./img_data/Spontaneous_emotion/Neutral/"
Happy_img = "./img_data/Spontaneous_emotion/Happy/"
Boredom_img = "./img_data/Spontaneous_emotion/Boredom/"
Relaxed_img = "./img_data/Spontaneous_emotion/Relaxed/"
Stressed_img = "./img_data/Spontaneous_emotion/Stressed/"

# Acting dataset
Neutral_act = "./img_data/Acting_emotion/Neutral/"
Happy_act = "./img_data/Acting_emotion/Happy/"
Stress_act = "./img_data/Acting_emotion/Stress/"
Boredom_act = "./img_data/Acting_emotion/Boredom/"


#Resolution 0 ; 10 FPS ; Face - 400x400 ; Eyes - 255x61  
#Width=640
#Height =360
#n=80

#Resolution 1 ; 10 FPS ; Face - 400x400 ; Eyes - 255x61PS ; Face - 400x400 ; Eyes - 255x61PS ; Face - 400x400 ; Eyes - 255x61  
Width=720
Height =480
n=300

#Resolution 2 ; 6.6 FPS ; Face - 450x450 ; Eyes - 320x80  
#Width=1024
#Height =768
#n=40

#Resolution 3 ; 5 FPS ; Face - 706x706 ; Eyes - 444x120
#Width=1280
#Height =1024
#n=30



# Indicates person ID
num = input("Person ID (i.e: S1, S2, ... ,Sn):")


# Load video capture:
cap = cv2.VideoCapture(3)



GSR_Array = []
#______________________________Acting emotions________________________________#

a=100
while (True):   
    image = cv2.imread(Act_img + 'Neutral_Instruction.jpg')                    
    cv2.imshow('Instruction', image)
    print ("Press space to continue...")
    k = cv2.waitKey(300) & 0xff
    if k == 32:
        break  
cv2.destroyAllWindows()    

cpt = 0
maxFrames = a
while(True):          
    image = cv2.imread(Act_img + 'Neutral_Act.jpg') 
    cv2.imshow('image',image)                                   
    cv2.waitKey(100) 
    break    

Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate 
cpt = 0
maxFrames = a
while(True):    
    ret, img = cap.read()
    img = imutils.resize(img, width=Width, height = Height)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)    
    if (cpt < maxFrames): 
        while (Sensor.inWaiting() ==0):     #Wait until there is data 
            pass                            #N O T H I N G ---
        GSR = Sensor.readline()     #Convert string to floating number 
        cpt += 1 
        currentTime = datetime.now()
        Time =  currentTime.strftime("%H: %M: %S.%f")[:-3]      
        csvRow = [str(Time), str(num) , "Neutral", str(GSR), str(cpt)]
        fieldnames = ['GSR', 'ID']
        csvfile = (csv_path + str(num) + '_Neutral_A_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', quotechar=' ',
                            quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
    for (x, y, w, h) in faces:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        roi_gray = gray[y: y + h, x : x + w]
        roi_color = img[y+1: y + h-1, x+1 : x + w-1]
        cv2.imwrite(Neutral_act  + "Neutral_" + str(num) +
                    "_Face%02i_.jpg" %cpt, roi_color)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 1)
            img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                                                 
            print (str(cpt) + " GSR: " + str(GSR) + 
                   ". Picture 1: %s" % time.ctime()) 
            cv2.imwrite(Neutral_act + "Neutral_" + str(num) + 
                        "_Eyes%02i_.jpg" %cpt, img_eye)
        break               
    if(cpt==maxFrames):
        with open(csvfile ,newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]
        with open(csvfile,'w',newline='') as f:
            w = csv.writer(f)
            w.writerow(["Timestamp", "ID", "Emotion" ,
                        "GSR", "Picture number"])
            w.writerows(data)            
        cv2.waitKey(100) 
        break     
    
cv2.destroyAllWindows() 
Sensor.close()   
            
cpt = 0
maxFrames = a
while (True):   
    image = cv2.imread(Act_img + 'Happy_Instruction.jpg')                       
    cv2.imshow('Instruction', image)
    print ("Press space to continue...")
    k = cv2.waitKey(300) & 0xff
    if k == 32:
        break   
cv2.destroyAllWindows()  




Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate 

while(True):                                  
    image = cv2.imread(Act_img + 'Happy_Act.jpg') 
    cv2.imshow('image',image)                                   
    cv2.waitKey(100) 
    break 

while(True):    
    ret, img = cap.read()
    img = imutils.resize(img, width=Width, height = Height)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)    
    if (cpt < maxFrames): 
        while (Sensor.inWaiting() ==0):     #Wait until there is data 
            pass                            #N O T H I N G ---
        GSR = Sensor.readline()     #Convert string to floating number 
        cpt += 1 
        currentTime = datetime.now()
        Time =  currentTime.strftime("%H: %M: %S.%f")[:-3]      
        csvRow = [str(Time), str(num) , "Happy", str(GSR), str(cpt)]
        fieldnames = ['GSR', 'ID']
        csvfile = (csv_path + str(num) + '_Happy_A_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', quotechar=' ',
                            quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
    for (x, y, w, h) in faces:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        roi_gray = gray[y: y + h, x : x + w]
        roi_color = img[y+1: y + h-1, x+1 : x + w-1]
        cv2.imwrite(Happy_act  + "Happy_" + str(num) + 
                    "_Face%02i_.jpg" %cpt, roi_color)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 1)
            img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                                               
            print (str(cpt) + " GSR: " + str(GSR) + 
                   ". Picture 2: %s" % time.ctime()) 
            cv2.imwrite(Happy_act + "Happy_" + str(num) +
                        "_Eyes%02i_.jpg" %cpt, img_eye)
        break            
    if(cpt==maxFrames):
        with open(csvfile ,newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]
        with open(csvfile,'w',newline='') as f:
            w = csv.writer(f)
            w.writerow(["Timestamp", "ID", "Emotion" ,
                        "GSR", "Picture number"])
            w.writerows(data)              
        cv2.waitKey(100) 
        break      
cv2.destroyAllWindows()  
Sensor.close()


while (True):   
    image = cv2.imread(Act_img + 'Stress_Instruction.jpg')                        
    cv2.imshow('Instruction', image)
    print ("Press space to continue...")
    k = cv2.waitKey(300) & 0xff
    if k == 32:
        break
     
cv2.destroyAllWindows()  


Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate 
while(True):                               
    image = cv2.imread(Act_img + 'Stress_Act.jpg') 
    cv2.imshow('image',image)                                   
    cv2.waitKey(100) 
    break     
            
cpt = 0
maxFrames = a

while(True):    
    ret, img = cap.read()
    img = imutils.resize(img, width=Width, height = Height)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if (cpt < maxFrames): 
        while (Sensor.inWaiting() ==0):     #Wait until there is data 
            pass                            #N O T H I N G ---
        GSR = Sensor.readline()     #Convert string to floating number 
        cpt += 1 
        currentTime = datetime.now()
        Time =  currentTime.strftime("%H: %M: %S.%f")[:-3]      
        csvRow = [str(Time), str(num) , "Stress", str(GSR), str(cpt)]
        fieldnames = ['GSR', 'ID']
        csvfile = (csv_path + str(num) + '_Stress_A_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', 
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
    for (x, y, w, h) in faces:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        roi_gray = gray[y: y + h, x : x + w]
        roi_color = img[y+1: y + h-1, x+1 : x + w-1]
        cv2.imwrite(Stress_act  + "Stress_" + str(num) + 
                    "_Face%02i_.jpg" %cpt, roi_color)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 1)
            img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                                               
            print (str(cpt) + " GSR: " + str(GSR) + 
                   ". Picture 3: %s" % time.ctime()) 
            cv2.imwrite(Stress_act + "Stress_" + str(num) +
                        "_Eyes%02i_.jpg" %cpt, img_eye)
        break             
    if(cpt==maxFrames):
        with open(csvfile ,newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]
        with open(csvfile,'w',newline='') as f:
            w = csv.writer(f)
            w.writerow(["Timestamp", "ID", "Emotion" ,
                        "GSR", "Picture number"])
            w.writerows(data)
            Sensor.close()
        cv2.waitKey(100) 
        break                
cv2.destroyAllWindows()  


while (True):   
    image = cv2.imread(Act_img + 'Boredom_Instruction.jpg')                       
    cv2.imshow('Instruction', image)
    print ("Press space to continue...")
    k = cv2.waitKey(300) & 0xff
    if k == 32:
        break     
cv2.destroyAllWindows()  



Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate 
while(True):                               
    image = cv2.imread(Act_img + 'Boredom_Act.jpg') 
    cv2.imshow('image',image)                                   
    cv2.waitKey(100) 
    break     

cpt = 0
maxFrames = a         
while(True):    
    ret, img = cap.read()
    img = imutils.resize(img, width=Width, height = Height)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)   
    if (cpt < maxFrames): 
        while (Sensor.inWaiting() ==0):     #Wait until there is data 
            pass                            #N O T H I N G ---
        GSR = Sensor.readline()     #Convert string to floating number 
        cpt += 1 
        currentTime = datetime.now()
        Time =  currentTime.strftime("%H: %M: %S.%f")[:-3]      
        csvRow = [str(Time), str(num) , "Boredom", str(GSR), str(cpt)]
        fieldnames = ['GSR', 'ID']
        csvfile = (csv_path + str(num) + '_Boredom_A_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', 
                            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)   
    for (x, y, w, h) in faces:       
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
        roi_gray = gray[y: y + h, x : x + w]
        roi_color = img[y+1: y + h-1, x+1 : x + w-1]
        cv2.imwrite(Boredom_act  + "Boredom_" + str(num) + 
                    "_Face%02i_.jpg" %cpt, roi_color)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey),
                          (ex + ew, ey + eh), (0, 255, 0), 1)
            img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                                               
            cv2.imwrite(Boredom_act + " GSR: " + str(GSR) + "Boredom_" + str(num) +
                        "_Eyes%02i_.jpg" %cpt, img_eye)
        break        
    if(cpt==maxFrames):
        with open(csvfile ,newline='') as f:
            r = csv.reader(f)
            data = [line for line in r]
        with open(csvfile,'w',newline='') as f:
            w = csv.writer(f)
            w.writerow(["Timestamp", "ID", "Emotion" ,
                        "GSR", "Picture number"])
            w.writerows(data)        
        cv2.waitKey(100) 
        break     
           
cv2.destroyAllWindows()  
Sensor.close()
