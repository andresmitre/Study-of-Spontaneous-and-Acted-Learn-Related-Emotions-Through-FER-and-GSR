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

#SEGUNDA FALANGE



# Indicates person ID
num = input("Person ID (i.e: S1, S2, ... ,Sn):")


GSR_Array = []





# Load video capture:
cap = cv2.VideoCapture(3)



#______________________________Spontanoues emotions________________________________#

# Create multiscale classifier:
while (True):
   
    ret, img = cap.read()
    img = imutils.resize(img, width=Width, height = Height)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #image, Scale factor, min Neighbors, min size, max size
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x-10,y-10) , (x+w+10, y+h+30), (0,0,255), 2)
        roi_gray = gray[y : y + h, x : x + w]
        roi_color = img[y : y + h, x : x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10, 10)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,255,0), 1, )
            img_eye = roi_color[ey : ey + eh , ex : ex + ew]         
        # Display the resulting frame     
        cv2.imshow('Camera',img) 
        print ("Press space to continue...")
    k = cv2.waitKey(300) & 0xff
    if k == 32:
        print ("do not move")
        break  
cv2.destroyAllWindows()     
time.sleep(5) 


cpt = 0
maxFrames = n
while(True):
   time.sleep(310) 
#   time.sleep(3)
   break    


Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate 
cpt = 0
maxFrames = n
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
        csvRow = [str(Time), str(num) , "Stressed", GSR, str(cpt)]
        fieldnames = ['GSR', 'ID']
        csvfile = (csv_path + str(num) + '_Stressed_S_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
        for (x, y, w, h) in faces:      
            cv2.rectangle(img, (x, y), (x + w, y + h), 
                          (0, 0, 255), 1)
            roi_gray = gray[y: y + h, x : x + w]
            roi_color = img[y+1: y + h-1, x+1 : x + w-1]
            cv2.imwrite(Stressed_img + "Stressed_" + str(num) + 
                        "_Face_%03i.jpg" %cpt, roi_color)
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex + ew, ey + eh), (0, 255, 0), 1)
                img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                 
                print (str(cpt) + " GSR: " + str(GSR) + ". Stress: %s" % time.ctime())          
                cv2.imwrite(Stressed_img + "Stressed_" + str(num) + 
                            "_Eyes_%03i.jpg" %cpt, img_eye)
            break          
        if(cpt==maxFrames):
            with open(csvfile ,newline='') as f:
                r = csv.reader(f)
                data = [line for line in r]
            with open(csvfile,'w',newline='') as f:
                w = csv.writer(f)
                w.writerow(["Timestamp", "ID", "Emotion" , "GSR", "Picture number"])
                w.writerows(data)    
            cv2.waitKey(100) 
            break
    
print("Stress done")      
Sensor.close()          
cpt = 0
maxFrames = n

while(True):
    time.sleep(75) 
#    time.sleep(3)
    break
  

Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate     
cpt = 0
maxFrames = n
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
        csvfile = (csv_path + str(num) + '_Neutral_S_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
            
        for (x, y, w, h) in faces:       
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            roi_gray = gray[y: y + h, x : x + w]
            roi_color = img[y+1: y + h-1, x+1 : x + w-1]
            cv2.imwrite(Neutral_img  + "Neutral_" + str(num) +
                "_Face_%03i.jpg" %cpt, roi_color)
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex + ew, ey + eh), (0, 255, 0), 1)
                img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                           
                print (str(cpt) + " GSR: " + str(GSR) + ". Neutral: %s" % time.ctime())
                cv2.imwrite(Neutral_img  + "Neutral_" + str(num) +
                "_Eyes_%03i.jpg" %cpt, img_eye)
                    
            break              
        if(cpt==maxFrames):
            with open(csvfile ,newline='') as f:
                r = csv.reader(f)
                data = [line for line in r]
            with open(csvfile,'w',newline='') as f:
                w = csv.writer(f)
                w.writerow(["Timestamp", "ID", "Emotion" , "GSR", "Picture number"])
                w.writerows(data)    
            cv2.waitKey(100) 
            break
        
print("Neutral done")
Sensor.close()        
cpt = 0
maxFrames = n
while(True):
    time.sleep(145) #####################
#    time.sleep(3)
    break

            
Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate     
cpt = 0
maxFrames = n
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
        csvRow = [str(Time), str(num) , "Relaxed", str(GSR), str(cpt)]
        fieldnames = ['GSR', 'ID']
        csvfile = (csv_path + str(num) + '_Relaxed_S_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
            
        for (x, y, w, h) in faces:       
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            roi_gray = gray[y: y + h, x : x + w]
            roi_color = img[y+1: y + h-1, x+1 : x + w-1]
            cv2.imwrite(Relaxed_img  + "Relaxed_" + str(num) +
                "_Face_%03i.jpg" %cpt, roi_color)
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex + ew, ey + eh), (0, 255, 0), 1)
                img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                           
                print (str(cpt) + " GSR: " + str(GSR) + ". Relaxed: %s" % time.ctime())
                cv2.imwrite(Relaxed_img  + "Relaxed_" + str(num) +
                "_Eyes_%03i.jpg" %cpt, img_eye)               
            break              
        if(cpt==maxFrames):
            with open(csvfile ,newline='') as f:
                r = csv.reader(f)
                data = [line for line in r]
            with open(csvfile,'w',newline='') as f:
                w = csv.writer(f)
                w.writerow(["Timestamp", "ID", "Emotion" , "GSR", "Picture number"])
                w.writerows(data)    
            cv2.waitKey(100) 
            break        

print("Relaxed done")           
Sensor.close()        
cpt = 0
maxFrames = n
while(True):
    time.sleep(210)   ##################
#    time.sleep(2)
    break

    

Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate    
cpt = 0
maxFrames = n
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
        csvfile = (csv_path + str(num) + '_Boredom_S_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
            
        for (x, y, w, h) in faces:       
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            roi_gray = gray[y: y + h, x : x + w]
            roi_color = img[y+1: y + h-1, x+1 : x + w-1]
            cv2.imwrite(Boredom_img  + "Boredom_" + str(num) +
                "_Face_%03i.jpg" %cpt, roi_color)
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex + ew, ey + eh), (0, 255, 0), 1)
                img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                           
                print (str(cpt) + " GSR: " + str(GSR) + ". Boredom: %s" %time.ctime())
                cv2.imwrite(Boredom_img  + "Boredom_" + str(num) +
                "_Eyes_%03i.jpg" %cpt, img_eye)                
            break              
        if(cpt==maxFrames):
            with open(csvfile ,newline='') as f:
                r = csv.reader(f)
                data = [line for line in r]
            with open(csvfile,'w',newline='') as f:
                w = csv.writer(f)
                w.writerow(["Timestamp", "ID", "Emotion" , "GSR", "Picture number"])
                w.writerows(data)    
            cv2.waitKey(100) 
            break     
        
print("Boredom done")    
Sensor.close()                     
cpt = 0
maxFrames = n
while(True):
#    time.sleep(388)
    time.sleep(348)    
#    time.sleep(3)
    break
                   
    
    
Sensor = serial.Serial('COM6', 115200)  #Serial PORT at certain baudRate     
cpt = 0
maxFrames = n
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
        csvfile = (csv_path + str(num) + '_Happy_S_GSR.csv') 
        with open(csvfile, "a",  newline='') as file: 
            wr = csv.writer(file, dialect='excel', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
            wr.writerow(csvRow)  
                
        for (x, y, w, h) in faces:       
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 1)
            roi_gray = gray[y: y + h, x : x + w]
            roi_color = img[y+1: y + h-1, x+1 : x + w-1]
            cv2.imwrite(Happy_img  + "Happy_" + str(num) +
                "_Face_%03i.jpg" %cpt, roi_color)
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 10, 10)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex + ew, ey + eh), (0, 255, 0), 1)
                img_eye = roi_color[ey+1 : ey + eh-1 , ex+1 : ex + ew-1]                                           
                print (str(cpt) + " GSR: " + str(GSR) + ". Happy: %s" % time.ctime())
                cv2.imwrite(Happy_img  + "Happy_" + str(num) +
                "_Eyes_%03i.jpg" %cpt, img_eye)
                
            break              
        if(cpt==maxFrames):
            with open(csvfile ,newline='') as f:
                r = csv.reader(f)
                data = [line for line in r]
            with open(csvfile,'w',newline='') as f:
                w = csv.writer(f)
                w.writerow(["Timestamp", "ID", "Emotion" , "GSR", "Picture number"])
                w.writerows(data)    
            cv2.waitKey(100) 
            break            
       
Sensor.close()        
        
cv2.destroyAllWindows()  


    
