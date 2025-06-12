from tkinter import * 
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter
from tkinter import Button
from student import Student
from att import Attendance
from faceRecognize import FaceRecognize


import cv2
from tkinter import messagebox


import numpy as np

import os

class Face():
    # calling constructor
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Shiksha-Mitra")

        # Adding bg
        img=Image.open("../proozect/images/bg.jpg")
        img= img.resize((1530,710))
        blurred_image = img.filter(ImageFilter.GaussianBlur(radius=5))
        self.photoimg= ImageTk.PhotoImage(blurred_image)


        lbl= Label(self.root, image=self.photoimg)
        lbl.place(x=0,y=50,width=1530, height=710)

        # adding title
        title=tk.Label(root, text="SHIKSHA-MITRA: A TEACHER'S BUDDY", font=("times new roman", 40, "bold"), bg="#834f1f", fg="white")
        title.place(x=0, y=0, width=1530, height=60)


        # add student buttons
        img_b=Image.open("../proozect/images/details.jpeg")
        img_b= img_b.resize((220,220))
        photoimg_b= ImageTk.PhotoImage(img_b)

        b1=Button(root, image=photoimg_b, command= self.student_details,  cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)
        b1.image= photoimg_b

        b1_1= Button(root, text="Student Details",command= self.student_details, cursor="hand2", font=("times new roman", 16, "bold"), bg="#696969", fg="black")
        b1_1.place(x=200, y=300, width=220, height=40)


        # add face recognition button
        img_2=Image.open("../proozect/images/faceDetect.jpg")
        img_2= img_2.resize((220,220))
        photoimg_b2= ImageTk.PhotoImage(img_2)

        b2=Button(root, image=photoimg_b2,command=self.faceData, cursor="hand2")
        b2.place(x=600, y=100, width=220, height=220)
        b2.image= photoimg_b2

        b2_2= Button(root, text="face detector", command=self.faceData, cursor="hand2", font=("times new roman", 16, "bold"), bg="Black", fg="White")
        b2_2.place(x=600, y=300, width=220, height=40)




        # attendance button
        img_3=Image.open("../proozect/images/attend.jpg")
        img_3= img_3.resize((220,220))
        photoimg_b3= ImageTk.PhotoImage(img_3)

        b3=Button(root, image=photoimg_b3,command=self.atten, cursor="hand2")
        b3.place(x=1000, y=100, width=220, height=220)
        b3.image= photoimg_b3

        b3_2= Button(root, text="See Attendance",command=self.atten, cursor="hand2", font=("times new roman", 16, "bold"), bg="Black", fg="White")
        b3_2.place(x=1000, y=300, width=220, height=40)




        # add Train Data button
        img_4=Image.open("../proozect/images/trainData.jpg")
        img_4= img_4.resize((220,220))
        photoimg_b4= ImageTk.PhotoImage(img_4)

        b4=Button(root, image=photoimg_b4,command= self.train_classifier, cursor="hand2")
        b4.place(x=200, y=380, width=220, height=220)
        b4.image= photoimg_b4

        b4_2= Button(root, text="Train Data",command= self.train_classifier, cursor="hand2", font=("times new roman", 16, "bold"), bg="Black", fg="White")
        b4_2.place(x=200, y=580, width=220, height=40)




        # add Photos button
        img_5=Image.open("../proozect/images/photos.jpg")
        img_5= img_5.resize((220,220))
        photoimg_b5= ImageTk.PhotoImage(img_5)

        b5=Button(root, image=photoimg_b5, cursor="hand2", command=self.open_img)
        b5.place(x=600, y=380, width=220, height=220)
        b5.image= photoimg_b5

        b5_2= Button(root, text="Photos", cursor="hand2",command=self.open_img, font=("times new roman", 16, "bold"), bg="Black", fg="White")
        b5_2.place(x=600, y=580, width=220, height=40)



        # add exit button
        img_6=Image.open("../proozect/images/exit.jpg")
        img_6= img_6.resize((220,220))
        photoimg_b6= ImageTk.PhotoImage(img_6)

        b6=Button(root, image=photoimg_b6,command=self.iexit, cursor="hand2")
        b6.place(x=1000, y=380, width=220, height=220)
        b6.image= photoimg_b6

        b6_2= Button(root, text="Exit",command=self.iexit, cursor="hand2", font=("times new roman", 16, "bold"), bg="Black", fg="White")
        b6_2.place(x=1000, y=580, width=220, height=40)


        # =============Function Buttons===========
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def open_img(self):
        os.startfile("data")

    def iexit(self):
        self.iexit= messagebox.askyesno("ShikshaMitra", "You want to exit???")
        if self.iexit>0:
            self.root.destroy()
        else:
            return


 
    

    # def capture_faces(user_id, save_path="data"):
    #     cam = cv2.VideoCapture(0)
    #     face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    #     count = 0

    #     os.makedirs(save_path, exist_ok=True)

    #     while True:
    #         ret, frame = cam.read()
    #         if not ret:
    #             break

    #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #         faces = face_detector.detectMultiScale(gray, 1.3, 5)

    #         for (x, y, w, h) in faces:
    #             count += 1
    #             cv2.imwrite(f"{save_path}/user.{user_id}.{count}.jpg", gray[y:y+h, x:x+w])
    #             cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #         cv2.imshow('Capturing Faces', frame)

    #     # Stop the loop after 100 images
    #         if count >= 100:
    #             print(f"[INFO] Collected 100 face samples for user ID: {user_id}")
    #             break  # Stop after 100 images

    #     # Give the user time to adjust their face or take another shot
    #         if cv2.waitKey(1) & 0xFF == ord('q'):  # You can use 'q' to quit manually if needed
    #             break

    #     cam.release()
    #     cv2.destroyAllWindows()
    
   




    def train_classifier(self):
        foldrPath=("data")
        path= [os.path.join(foldrPath, file) for file in os.listdir(foldrPath)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L") # into Gray Scale
            imgNp = np.array(img,  'uint8') 
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imgNp)
            ids.append(id)
            cv2.imshow("Training", imgNp)
            cv2.waitKey(1)==13

        ids = np.array(ids)

        # =====================trining nd save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces , ids )
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("RESULT", "TRAINING COMPLETED!!! ")



    def faceData(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognize(self.new_window)


    def atten(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window) 






if __name__ == "__main__":
    root=Tk()
    obj=Face(root)
    root.mainloop()