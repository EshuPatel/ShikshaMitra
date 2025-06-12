from tkinter import * 
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Button
from tkinter import messagebox
import mysql.connector
import time

import cv2

class Student():
    # calling constructor
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Shiksha-Mitra")

        # ================variables============
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_erp = StringVar()
        self.var_stdName = StringVar()
        self.var_clss = StringVar()
        self.var_roll = StringVar()
        self.var_tName = StringVar()


        # Adding bg
        img=Image.open("../proozect/images/bg.jpg")
        img= img.resize((1530,710))
        self.photoimg= ImageTk.PhotoImage(img)


        lbl= Label(root, image=self.photoimg)
        lbl.place(x=0,y=50,width=1530, height=710)
        lbl.image= self.photoimg

        # adding title
        title=tk.Label(root, text="STUDENT'S INFORMATION", font=("times new roman", 40, "bold"), bg="tomato", fg="White")
        title.place(x=0, y=0, width=1550, height=80)

        frame=Frame(root, bd=2)
        frame.place(x=10,y=80,width=1500, height=650)




        # left label frame
        lft= LabelFrame(frame, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=("times new roman", 16, "bold"))
        lft.place(x=10, y=10,width=740, height=580)

         # sub-left "course" frame
        course_lft= LabelFrame(lft, bd=2, relief=RIDGE, text="COURSE CURRENT INFORMATION", font=("times new roman", 16, "bold"))
        course_lft.place(x=5, y=10,width=730, height=150)

        # |---->course----> dept
        dep_label=Label(course_lft, text="Department", font=("times new roman", 16, "bold"))
        dep_label.grid(row=0, column=0, padx=15, pady=15)

        dep_comboBox=ttk.Combobox(course_lft, textvariable=self.var_dep, font=("times new roman", 16, "bold"), width=15, state="readonly")
        dep_comboBox["values"]=("No Selection", "Computer", "IT")
        dep_comboBox.current(0)
        dep_comboBox.grid(row=0, column=1, padx=3, pady=10, sticky=W)

        # |---->course----> Course
        course_label=Label(course_lft, text="Course", font=("times new roman", 16, "bold"))
        course_label.grid(row=0, column=2, padx=10, pady=15)

        course_comboBox=ttk.Combobox(course_lft,textvariable=self.var_course, font=("times new roman", 16, "bold"), width=15, state="readonly")
        course_comboBox["values"]=("No Selection", "Maths", "English", "Java")
        course_comboBox.current(0)
        course_comboBox.grid(row=0, column=3, padx=3, pady=10, sticky=W)

        # |---->course----> Year
        yr_label=Label(course_lft, text="Year", font=("times new roman", 16, "bold"))
        yr_label.grid(row=1, column=0, padx=15, pady=15)

        yr_comboBox=ttk.Combobox(course_lft,textvariable=self.var_year, font=("times new roman", 16, "bold"), width=15, state="readonly")
        yr_comboBox["values"]=("No Selection", "2021", "2022", "2023")
        yr_comboBox.current(0)
        yr_comboBox.grid(row=1, column=1, padx=3, pady=10, sticky=W)

        # |---->course----> Semester
        sem_label=Label(course_lft, text="Semester", font=("times new roman", 16, "bold"))
        sem_label.grid(row=1, column=2, padx=15, pady=15)

        sem_comboBox=ttk.Combobox(course_lft,textvariable=self.var_sem, font=("times new roman", 16, "bold"), width=15, state="readonly")
        sem_comboBox["values"]=("No Selection", "Even", "Odd")
        sem_comboBox.current(0)
        sem_comboBox.grid(row=1, column=3, padx=1, pady=10, sticky=W)


        # ---->Student info..
        stud_lft= LabelFrame(lft, bd=2, relief=RIDGE, text="STUDENT PERSONAL INFORMATION", font=("times new roman", 16, "bold"))
        stud_lft.place(x=5, y=170,width=730, height=260)

        # ---->Student info---->erpId
        erp_label=Label(stud_lft, text="ERP ID:", font=("times new roman", 14, "bold"))
        erp_label.grid(row=0, column=0, padx=15, pady=10, sticky=W)

        erp=ttk.Entry(stud_lft, textvariable=self.var_erp, width=15, font=("times new roman", 14, "bold") )
        erp.grid(row=0, column=1, padx=15, sticky=W)
 
        # ---->Student info---->StudentName
        std_label=Label(stud_lft, text="Student Name:", font=("times new roman", 14, "bold"))
        std_label.grid(row=0, column=2, padx=15, pady=10, sticky=W)

        std=ttk.Entry(stud_lft, textvariable=self.var_stdName, width=15, font=("times new roman", 14, "bold") )
        std.grid(row=0, column=3, padx=15, sticky=W)

        # ---->Student info---->Class Division
        div_label=Label(stud_lft, text="Class:", font=("times new roman", 14, "bold"))
        div_label.grid(row=1, column=0, padx=15, pady=5, sticky=W)

        div=ttk.Entry(stud_lft,textvariable=self.var_clss, width=15, font=("times new roman", 14, "bold") )
        div.grid(row=1, column=1, padx=15, pady=5, sticky=W)

        # ---->Student info---->Roll No.
        roll_label=Label(stud_lft, text="Roll:", font=("times new roman", 14, "bold"))
        roll_label.grid(row=1, column=2, padx=15, pady=5, sticky=W)

        roll=ttk.Entry(stud_lft,textvariable=self.var_roll, width=15, font=("times new roman", 14, "bold") )
        roll.grid(row=1, column=3, padx=15,pady=5, sticky=W)

       

        # ---->Student info---->Teacher Name
        tName_label=Label(stud_lft, text="Teacher Name:", font=("times new roman", 14, "bold"))
        tName_label.grid(row=2, column=0, padx=15, pady=5, sticky=W)

        tName=ttk.Entry(stud_lft,textvariable=self.var_tName, width=15, font=("times new roman", 14, "bold") )
        tName.grid(row=2, column=1, padx=15,pady=5, sticky=W)

        # radioButtons
        self.var_r1= StringVar()
        r1=ttk.Radiobutton(stud_lft,variable=self.var_r1, text="Take Photo", value="Yes")
        r1.grid(row=2, column=2)

        
        r2=ttk.Radiobutton(stud_lft,variable=self.var_r1, text="No Photo", value="No")
        r2.grid(row=2, column=3)


        # buttons frame
        btn_frame= Frame(stud_lft, bd=2,relief= RIDGE)
        btn_frame.place(x=0, y=120, width=715, height=150)

        save= Button(btn_frame, text="SAVE",command= self.add_data, font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        save.grid(row=0,column=0,padx=3, pady=5)

        update= Button(btn_frame, text="UPDATE",command= self.update_data, font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        update.grid(row=0,column=1, padx=3, pady=5)

        delete= Button(btn_frame, text="DELETE", command= self.delete_data, font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        delete.grid(row=0,column=2, padx=3, pady=5)

        reset= Button(btn_frame, text="RESET",command= self.reset_data,  font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        reset.grid(row=0,column=3, padx=3, pady=5)

        tPhoto= Button(btn_frame, text="Take Photo", command= self.generate_dataset, font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        tPhoto.grid(row=1,column=0, padx=5, pady=5)

        uPhoto= Button(btn_frame, text="Update Photo", font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        uPhoto.grid(row=1,column=1, padx=3, pady=5)





        # ryt label frame
        ryt= LabelFrame(frame, bd=2, relief=RIDGE, text="STUDENT DETAILS", font=("times new roman", 16, "bold"))
        ryt.place(x=750, y=10,width=720, height=580)

        r_img=Image.open("../proozect/images/wall.jpg")
        r_img= r_img.resize((720,150))
        self.photoimg_r= ImageTk.PhotoImage(r_img)
        # r_img.image= photoimg_r

        r_lbl= Label(ryt, image=self.photoimg_r)
        r_lbl.place(x=5,y=0,width=720, height=150)

        #=============== search system===================
        srch_frm= LabelFrame(ryt, bd=2, relief=RIDGE, text="SEARCH FROM THE SYSTEM", font=("times new roman", 16, "bold"), fg="tomato")
        srch_frm.place(x=5, y=170,width=730, height=260)

        srch_label=Label(srch_frm, text="Search By: ", font=("times new roman", 14, "bold"), bg="tomato", fg="white")
        srch_label.grid(row=0, column=0, padx=15, pady=5, sticky=W)

        srch_comboBox=ttk.Combobox(srch_frm, font=("times new roman", 16, "bold"), width=15, state="readonly")
        srch_comboBox["values"]=("No Selection", " By Roll", "By phn no.")
        srch_comboBox.current(0)
        srch_comboBox.grid(row=0, column=1, padx=3, pady=10, sticky=W)


        srch_entry=ttk.Entry(srch_frm, width=15, font=("times new roman", 16, "bold") )
        srch_entry.grid(row=0, column=3, padx=15, pady=5, sticky=W)

        srch= Button(srch_frm, text="SEARCH", font=("times new roman", 14, "bold"), width=13, bg="Tomato", fg="White" )
        srch.grid(row=1,column=0, padx=3, pady=5)

        shwAll= Button(srch_frm, text="SHOW ALL", font=("times new roman", 14, "bold"), width=13, bg="Tomato", fg="White" )
        shwAll.grid(row=1,column=1, padx=3, pady=5)



        # =======tbl frame===========
        tbl_frm= Frame(ryt, bd=2, bg="white", relief=RIDGE)
        tbl_frm.place(x=5, y=300, width=710, height=250)

        scroll_x=ttk.Scrollbar(tbl_frm, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frm, orient=VERTICAL)

        self.std_tbl= ttk.Treeview(tbl_frm, column=("DEP", "COURSE", "YEAR", "SEM", "ERP", "NAME","CLASS", "ROLL", "TEACHER", "PHOTO"), xscrollcommand= scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.std_tbl.xview)
        scroll_y.config(command=self.std_tbl.yview)


        self.std_tbl.heading("DEP", text="DEPT.")
        self.std_tbl.heading("COURSE", text="COURSE")
        self.std_tbl.heading("YEAR", text="YEAR")
        self.std_tbl.heading("SEM", text="SEM")
        self.std_tbl.heading("ERP", text="ERP")
        self.std_tbl.heading("NAME", text="NAME")
        self.std_tbl.heading("CLASS", text="CLASS")
        self.std_tbl.heading("ROLL", text="ROLL")
        self.std_tbl.heading("TEACHER", text="TEACHER")
        self.std_tbl.heading("PHOTO", text="PHOTO")
        self.std_tbl['show']="headings"

        self.std_tbl.column("DEP", width=100)
        self.std_tbl.column("COURSE", width=100)
        self.std_tbl.column("YEAR", width=100)
        self.std_tbl.column("SEM", width=100)
        self.std_tbl.column("ERP", width=100)
        self.std_tbl.column("NAME", width=100)
        self.std_tbl.column("CLASS", width=100)
        self.std_tbl.column("ROLL", width=100)
        self.std_tbl.column("TEACHER", width=100)
        self.std_tbl.column("PHOTO", width=100)

        self.std_tbl.pack(fill=BOTH, expand=1)

        self.std_tbl.bind("<ButtonRelease>", self.get_crsr)
        self.fetch_data()


    # =========  func. to add data==========
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_erp.get()=="":
            messagebox.showerror("Error", "ALl fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
                crsr= conn.cursor()
                crsr.execute("insert into student values(%s, %s, %s,%s,%s,%s,%s,%s, %s, %s)", 
                            (self.var_dep.get(), 
                            self.var_course.get(), 
                            self.var_year.get(), 
                            self.var_sem.get(), 
                            self.var_erp.get(),
                            self.var_stdName.get(),
                            self.var_clss.get(),
                            self.var_roll.get(), 
                            self.var_tName.get(), 
                            self.var_r1.get(), ))
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Info added successfully")
            
            except Exception as e:
                messagebox.showerror("Error", f"Due to : {str(e)}")


    # ===============fetching
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
        crsr= conn.cursor()
        crsr.execute("Select * from student")
        data=crsr.fetchall()
        if len(data)!=0:
            self.std_tbl.delete(*self.std_tbl.get_children())
            for i in data:
                self.std_tbl.insert("", END, values=i)
            conn.commit()

        conn.close()
    

    # ==============get cursor========
    def get_crsr(self, event=""):
        crsr_focus=self.std_tbl.focus()
        content=self.std_tbl.item(crsr_focus, "values")
        print(content)
        # data=content["values"]

        self.var_dep.set(content[0]),
        self.var_course.set(content[1]),
        self.var_year.set(content[2]),
        self.var_sem.set(content[3]),
        self.var_erp.set(content[4]),
        self.var_stdName.set(content[5]),
        self.var_clss.set(content[6]),
        self.var_roll.set(content[7]),
        self.var_tName.set(content[8]),
        self.var_r1.set(content[9]),


    # ==========================update func========================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_erp.get()=="":
            messagebox.showerror("Error", "ALl fields are required")
        
        else: 
            try:
                update=messagebox.askyesno("Want to Update..??", "You sure about this..??")
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
                    crsr= conn.cursor()
                    crsr.execute("update student set DEPT=%s, COURSE=%s, YEAR=%s, SEM=%s, ERP=%s, NAME=%s, CLASS=%s, ROLL=%s, TEACHER=%s, PHOTO=%s where ERP=%s", 
                            (self.var_dep.get(), 
                            self.var_course.get(), 
                            self.var_year.get(), 
                            self.var_sem.get(),
                            self.var_erp.get(), 
                            self.var_stdName.get(), 
                            self.var_clss.get(),
                            self.var_roll.get(),
                            self.var_tName.get(), 
                            self.var_r1.get(),
                            self.var_erp.get()  )) 
                

                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Updation Completed!!!")
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as e:
                messagebox.showerror("OOPS!!!",f"Due to : {str(e)}" )


    # =======================delete button function
    def delete_data(self):
        if self.var_erp.get()=="":
            messagebox.showerror("Error", "ERP is required!! ")
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page", "Are you sure???")
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
                    crsr= conn.cursor()
                    qry="delete from student where ERP=%s"
                    val = (self.var_erp.get(), )
                    crsr.execute(qry, val)
                
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Deleted!!", "Successsfully deleted.")

            except Exception as e:
                messagebox.showerror("OOPS!!!",f"Due to : {str(e)}" )


    # ===================reset button functioning
    def reset_data(self):
        self.var_dep.set("No Selection")
        self.var_course.set("No Selection")
        self.var_year.set("No Selection")
        self.var_sem.set("No Selection")
        self.var_erp.set("")
        self.var_stdName.set("")
        self.var_clss.set("")
        self.var_roll.set("")
        self.var_tName.set("")
        self.var_r1.set("")



    # =======================generating dataset or taking photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_stdName.get()=="" or self.var_erp.get()=="":
            messagebox.showerror("Error", "ALl fields are required")
        
        else: 
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
                crsr= conn.cursor()
                crsr.execute("select * from student")
                res= crsr.fetchall()
                id=0

                
                for i in res:
                    id+=1
                    crsr.execute("Update student set DEPT=%s, COURSE=%s, YEAR=%s, SEM=%s, ERP=%s, NAME=%s,CLASS=%s, ROLL=%s, TEACHER=%s, PHOTO=%s where ERP=%s", 
                            (self.var_dep.get(), 
                            self.var_course.get(), 
                            self.var_year.get(), 
                            self.var_sem.get(), 
                            self.var_erp.get(),
                            self.var_stdName.get(), 
                            self.var_clss.get(),
                            self.var_roll.get(),
                            self.var_tName.get(), 
                            self.var_r1.get(),
                            self.var_erp.get()== id+1   ))
                    conn.commit()
                    self.fetch_data()
                    self.reset_data()
                    

                    # ====================loading data from frontalface .xml
                    face_cls = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                    def faceCrop(img):
                        gayScale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces= face_cls.detectMultiScale(gayScale, 1.3, 5)
                        # 1.3 scaling factor and 5 is minimum neighbor

                        for (x,y,w,h) in faces:
                            faceCrop = img[y:y+h,x:x+w]
                            return faceCrop

                    cap = cv2.VideoCapture(0)
                    imgId = 0

                    timestamp = int(time.time()) # Place this before the while loop

                    while True:
                        ret, myFrame = cap.read()
                        if faceCrop(myFrame) is not None:
                            imgId+=1
                            face= cv2.resize(faceCrop(myFrame), (450,450))
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                            # file = "data/user." + str(id) + "." + str(imgId) + "."+"jpg"
                            file = f"data/user.{id}.{timestamp}.{imgId}.jpg"

                            cv2.imwrite(file, face)
                            cv2.putText(face, str(imgId),(50,50), cv2.FONT_HERSHEY_COMPLEX, 2, (255,99,71), 2 )
                            cv2.imshow("Cropped face", face)
                        
                        if cv2.waitKey(1)==13 or int(imgId)==100:
                            break
                    
                    cap.release()
                    cv2.destroyAllWindows()

                    messagebox.showinfo("Result", "Generating dataset completed")
            
            
            except Exception as e:
                messagebox.showerror("OOPS!!!",f"Due to : {str(e)}" )

            
            finally:
                if conn.is_connected():
                    crsr.close()
                    conn.close()




if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()