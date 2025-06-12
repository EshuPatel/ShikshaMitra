from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import threading

import cv2
import os
import numpy as np

class FaceRecognize():
    # calling constructor
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Shiksha-Mitra")

        # adding title
        title=Label(root, text="Face Recognition", font=("times new roman", 40, "bold"), bg="#834f1f", fg="White")
        title.place(x=0, y=0, width=1550, height=80)

        topImg=Image.open("../proozect/images/faceD.jpg")
        topImg = topImg.resize((1530,325))
        self.lftPhotoimg=ImageTk.PhotoImage(topImg)

        fLabel= Label(self.root, image=self.lftPhotoimg)
        fLabel.place(x=0, y=75, width=1530, height=325)

    # Button
        b1_1= Button(root, text="Face Detector",command=self.FaceRecogThread, cursor="hand2", font=("times new roman", 16, "bold"), bg="#9a6a41", fg="White")
        b1_1.place(x=0, y=400, width=1530, height=70)


        btmImg=Image.open("../proozect/images/faceD2.jpg")
        btmImg = btmImg.resize((1530,325))
        self.btmPhotoimg=ImageTk.PhotoImage(btmImg)

        fLabel= Label(self.root, image=self.btmPhotoimg)
        fLabel.place(x=0, y=460, width=1530, height=325)

    # ================ATTENDANCE
    def markAtt(self, d,n,r):
         with open("att.csv", "r+", newline="\n") as f:
            myData=f.readlines()
            nameList=[]
            for line in myData:
                   entry=line.split((","))
                   nameList.append(entry[0])
            if((d not in nameList) and (n not in nameList) and (r not in nameList)):
                 now= datetime.now()
                 d1= now.strftime("%d/%m/%Y")
                 dtString= now.strftime("%H:%M:%S")
                 f.writelines(f"\n{d},{n},{r},{dtString}, {d1}, Present")
                 
            

    

    

    def faceRecog(self):
        def drawFrame(img, classifier, scaleFactor, minNeighbor, color, text, clf):
            grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            feat= classifier.detectMultiScale(grayImg, scaleFactor, minNeighbor)

            coor=[]

            for (x,y,w,h) in feat:
                cv2.rectangle(img, (x,y), (x+w,y+h),(255,99,71), 3)
                    # (255,99,71) is tomato

                id, predict= clf.predict(grayImg[y:y+h, x:x+w])
                cnfidnce = int((100*(1-predict/300)))
                    
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
                crsr= conn.cursor()

                crsr.execute("select NAME from student where ERP=" + str(id))
                print(f"ERP being searched: {id}")  # Show the actual ERP value being queried

                n=crsr.fetchone()
                if n:
                    name = n[0]
                    print("Welcome", name)
                else:
                    messagebox.showwarning("Not Found", f"No student found with ERP: {id}")
                if n:  # Check if n is not None or empty
                    n = n[0]  # Extract the first element (the string) from the tuple
                    print(n)  # Print the extracted name
                else:
                    print("No data found")
                n = "+".join([n[0]])  # Join it as a list containing a single string
                print(n)

                crsr.execute("select ROLL from student where ERP=" + str(id))
                r=crsr.fetchone()
                r="+".join(r)

                crsr.execute("select ERP from student where ERP=" + str(id))
                d=crsr.fetchone()
                d="+".join(d)

                if cnfidnce>77:
                    cv2.putText(img, f"ROLL:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 69,0), 3)
                    cv2.putText(img, f"NAME:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 69,0), 3)
                    cv2.putText(img, f"ERP:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 69,0), 3)
                    self.markAtt(d,n,r)

                else:
                    cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0), 3)
                    cv2.putText(img, "UNREGISTERED FACE", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255,0), 3)



                coor=[x,y,w,h]
                    # or maybe y
                
            return coor
        

   

        def recog(img, clf, faceCascade):
            coor= drawFrame(img, faceCascade, 1.1, 10, (255,255,255), "FACE", clf)
            return img
            
        faceCascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf =  cv2.face.LBPHFaceRecognizer_create()
        clf.read(r"C:\Users\eshup\OneDrive\Desktop\proozect\classifier.xml")
            
        vidCap= cv2.VideoCapture(0)

        if not vidCap.isOpened():
                print("Error: Camera not accessible.")
                return  # or exit the function


        while True:
                ret, img= vidCap.read()
                img = recog(img, clf, faceCascade)
                cv2.imshow("WELCOME TO SHIKSHAMITRA", img)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        vidCap.release()
        cv2.destroyAllWindows()

            



    def FaceRecogThread(self):
        threading.Thread(target=self.faceRecog, daemon=True).start()



if __name__ == "__main__":
    root=Tk()
    obj= FaceRecognize(root)
    root.mainloop()
