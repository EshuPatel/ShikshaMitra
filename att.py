from tkinter import * 
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import threading
import tkinter as tk

import csv
from tkinter import filedialog
import cv2
import os
import numpy as np

mydata=[]

class Attendance():
    # calling constructor
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Shiksha-Mitra")


        # ==============text var
        self.attId = StringVar()
        self.name = StringVar()
        self.roll = StringVar()
        self.time= StringVar()
        self.date = StringVar()
        self.att = StringVar()



        # Adding bg
        img=Image.open("../proozect/images/bg.jpg")
        img= img.resize((1530,710))
        self.photoimg= ImageTk.PhotoImage(img)


        lbl= Label(root, image=self.photoimg)
        lbl.place(x=0,y=50,width=1530, height=710)
        lbl.image= self.photoimg

        # adding title
        title=tk.Label(root, text="STUDENT'S ATTENDANCE INFORMATION", font=("times new roman", 40, "bold"), bg="TOMATO", fg="white")
        title.place(x=0, y=0, width=1550, height=80)

        frame=Frame(root, bd=2)
        frame.place(x=10,y=80,width=1500, height=650)




        # left label frame
        lft= LabelFrame(frame, bd=2, relief=RIDGE, text="STUDENT ATTENDANCE DETAILS", font=("times new roman", 16, "bold"))
        lft.place(x=10, y=10,width=740, height=580)

         # sub-left "course" frame
        sub_lft= LabelFrame(lft, bd=2, relief=RIDGE, text="ATTENDANCE INFORMATION", font=("times new roman", 16, "bold"))
        sub_lft.place(x=5, y=10,width=730, height=400)



        # =====================LABELS AND ENTRY
        attId=Label(sub_lft, text="ATT. ID:", font=("times new roman", 14, "bold"))
        attId.grid(row=0, column=0, padx=15, pady=10, sticky=W)

        attEntry=ttk.Entry(sub_lft, width=15, textvariable=self.attId, font=("times new roman", 14, "bold") )
        attEntry.grid(row=0, column=1, padx=15, sticky=W)

        # Name
        name=Label(sub_lft, text="NAME:", font=("times new roman", 14, "bold"))
        name.grid(row=1, column=0, padx=15, pady=10, sticky=W)

        nameEntry=ttk.Entry(sub_lft, width=15,textvariable=self.name, font=("times new roman", 14, "bold") )
        nameEntry.grid(row=1, column=1, padx=15, sticky=W)


        # roll
        roll=Label(sub_lft, text="ROLL:", font=("times new roman", 14, "bold"))
        roll.grid(row=4, column=0, padx=15, pady=10, sticky=W)

        rollEntry=ttk.Entry(sub_lft,textvariable=self. roll, width=15, font=("times new roman", 14, "bold") )
        rollEntry.grid(row=4, column=1, padx=15, sticky=W)


        # time
        time=Label(sub_lft, text="TIME:", font=("times new roman", 14, "bold"))
        time.grid(row=2, column=0, padx=15, pady=10, sticky=W)

        timeEntry=ttk.Entry(sub_lft, textvariable=self.time, width=15, font=("times new roman", 14, "bold") )
        timeEntry.grid(row=2, column=1, padx=15, sticky=W)


        # date
        date=Label(sub_lft, text="DATE:", font=("times new roman", 14, "bold"))
        date.grid(row=3, column=0, padx=15, pady=10, sticky=W)

        dateEntry=ttk.Entry(sub_lft,textvariable=self.date,  width=15, font=("times new roman", 14, "bold") )
        dateEntry.grid(row=3, column=1, padx=15, sticky=W)

        # attendance
        att=Label(sub_lft, text="ATTENDANCE", font=("times new roman", 16, "bold"))
        att.grid(row=0, column=2, padx=10, pady=15)

        att_comboBox=ttk.Combobox(sub_lft, font=("times new roman", 16, "bold"), width=15, textvariable=self.att, state="readonly")
        att_comboBox["values"]=("No Selection", "Present", "Absent")
        att_comboBox.current(0)
        att_comboBox.grid(row=0, column=3, padx=3, pady=10, sticky=W)



        # ==========================BUTTONS
        btn_frame= Frame(sub_lft, bd=2,relief= RIDGE)
        btn_frame.place(x=0, y=300, width=715, height=150)

        save= Button(btn_frame, text="IMPORT CSV", command=self.importCsv, font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        save.grid(row=0,column=0,padx=3, pady=5)

        exprt= Button(btn_frame, text="EXPORT CSV",command=self.exportCsv, font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        exprt.grid(row=0,column=1, padx=3, pady=5)

        update= Button(btn_frame, text="UPDATE", font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        update.grid(row=0,column=2, padx=3, pady=5)

        reset= Button(btn_frame, text="RESET", command=self.reset, font=("times new roman", 16, "bold"), width=13, bg="Tomato", fg="White" )
        reset.grid(row=0,column=4, padx=3, pady=5)




        # ryt label frame
        ryt= LabelFrame(frame, bd=2, relief=RIDGE, text="ATTENDANCE DETAILS", font=("times new roman", 16, "bold"))
        ryt.place(x=750, y=10,width=720, height=580)

        r_img=Image.open("../proozect/images/wall.jpg")
        r_img= r_img.resize((720,150))
        self.photoimg_r= ImageTk.PhotoImage(r_img)
        # r_img.image= photoimg_r

        r_lbl= Label(ryt, image=self.photoimg_r)
        r_lbl.place(x=5,y=0,width=720, height=150)


        # table frame
        tbl_frm= Frame(ryt, bd=2, bg="white", relief=RIDGE)
        tbl_frm.place(x=5, y=200, width=710, height=250)

        scroll_x=ttk.Scrollbar(tbl_frm, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(tbl_frm, orient=VERTICAL)

        self.AttendanceReportTable= ttk.Treeview(tbl_frm, column=("id","name", "roll", "time", "date", "att"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Att. ID")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("att", text="Attendance")


        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("att", width=100)


        self.AttendanceReportTable['show']="headings"

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.getCursor)


        # ============================fetch data
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

        
    def importCsv(self):
        global mydata
        mydata.clear()
        fname= filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV file","*.csv"),("All Files","*.*" )], parent=self.root)
        with open(fname) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)


    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error", "No Data Found!!")
                return False
            fname= filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=[("CSV file","*.csv"),("All Files","*.*" )], parent=self.root)
            with open(fname, mode="w", newline="") as myfile:
                expWrite= csv.writer(myfile, delimiter=",")
                for i in mydata:
                    expWrite.writerow(i)
                messagebox.showinfo("Data Exported","Data Sucessfully Exported.")

        except Exception as e:
             messagebox.showerror("Error", f"Due to : {str(e)}")



    def getCursor(self, event=''):
        crsrRow=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(crsrRow)
        rows= content['values']
        self.attId.set(rows[0])
        self.name.set(rows[1])
        self.roll.set(rows[2])
        self.time.set(rows[3])
        self.date.set(rows[4])
        self.att.set(rows[5])


    def reset(self):
        self.attId.set("")
        self.name.set("")
        self.roll.set("")
        self.time.set("")
        self.date.set("")
        self.att.set("")






if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()