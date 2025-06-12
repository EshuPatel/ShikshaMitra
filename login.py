from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from main import Face

from PIL import Image, ImageTk, ImageFilter




def main():
    win=Tk()
    app= Login(win)
    win.mainloop()


class Login:
    def __init__(self, root):
        self.root=root
        self.root.title("Shiksha-Mitra Login")
        self.root.geometry("1550x800+0+0")

        # ===================================variables
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_psswd=StringVar()
        self.var_confPasswd = StringVar()


        img=Image.open("../proozect/images/login page.jpg")
        img= img.resize((1530,800))
        blurred_image = img.filter(ImageFilter.GaussianBlur(radius=5))
        self.photoimg= ImageTk.PhotoImage(blurred_image)

        lbl= Label(self.root, image=self.photoimg)
        lbl.place(x=0,y=50,width=1530, height=710)


        # title
        title=tk.Label(root, text="ShikshaMitra: A Teacher's Buddy", font=("times new roman", 40, "bold"), bg="#161616", fg="#b99904")
        title.place(x=0, y=0, width=1530, height=80)


        frame= Frame(self.root, bg="white")
        frame.place(x=500, y= 190, width=560, height=480)


        # ============card===========

        title = tk.Label(frame, text="Sign In", font=("Arial", 24, "bold"), bg="white")
        title.pack(pady=10)

        subtitle = tk.Label(frame, text="Sign In to your account", font=("Arial", 16), bg="white", fg="grey")
        subtitle.pack()

        # ====form --------------email
        emailLabel=Label(frame, text="Email", font=("Arial", 15, "bold"), fg= "black", bg="white")
        emailLabel.place(x=65, y=110)

        self.txtemail= Entry(frame, font=("Arial", 15, "bold"), highlightthickness=2,
                 highlightbackground="#dcdcdc",
                 highlightcolor="blue")
        self.txtemail.place(x=65, y=150, width= 400, height=40 )

        # ====form -------------passwd
        psswdLabel=Label(frame, text="Password", font=("Arial", 15, "bold"), fg= "black", bg="white")
        psswdLabel.place(x=65, y=210)

        self.txtpsswd= Entry(frame, font=("Arial", 15, "bold"), highlightthickness=2,
                 highlightbackground="#dcdcdc",
                 highlightcolor="blue")
        self.txtpsswd.place(x=65, y=250, width= 400, height=40 )


        # ============sign in buttom
        loginBtn= Button(frame, text="Sign In",command=self.login, font=("Arial", 15, "bold"), relief=RIDGE, fg="white", bg="#0b68d4", activeforeground="white", activebackground="#0b68d4")
        loginBtn.place(x=65, y=320, width=400, height=50)

        # ===============register buttom
        signUpBtn= Button(frame, text="Don't have an account? Sign Up!",command=self.registerWindow, font=("Arial", 13),borderwidth=0, relief=RIDGE, fg="#0b68d4", bg="white", activeforeground="#0b68d4", activebackground="white")
        signUpBtn.place(x=65, y=380, width=400)

        # # ==================forgot psswd
        # forgotBtn= Button(frame, text="Forgot Password", command=self.forgotPassword, font=("Arial", 13), borderwidth=0,  relief=RIDGE, fg="#0b68d4", bg="white", activeforeground="#0b68d4", activebackground="white")
        # forgotBtn.place(x=65, y=410, width=400)

    def registerWindow(self):
        self.new_window = Toplevel(self.root)
        self.app= Register(self.new_window)

    def login(self):
        if self.txtemail.get()=="" or self.txtpsswd.get()=="":
            messagebox.showerror("Error", "All fields required!!")

        elif(self.txtemail.get()=="eshu@gmail.com" and self.txtpsswd.get()=="123"):
            messagebox.showinfo("Success", " Welcome to dashboard")
            self.new_window=Toplevel(self.root)
            self.app= Face(self.new_window)
            self.root.withdraw() 

        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
            crsr= conn.cursor()
            crsr.execute("select * from register where Email=%s and Password=%s", (
                self.txtemail.get(),
                self.txtpsswd.get()
            ))
            row=crsr.fetchone()

            if row== None:
                messagebox.showerror("Error", "Invalid Email & Password")
            else:
                openMsg= messagebox.askyesno("Select", "If only Admin access")
                if openMsg>0:
                    self.new_window=Toplevel(self.root)
                    self.app= Face(self.new_window)
                    self.root.withdraw() 
                else:
                    if not openMsg:
                        return
            conn.commit()
            conn.close()
            
            
        






    # def forgotPassword(self):
    #     if self.txtemail.get()=="":
    #         messagebox.showerror("Error", "Enter email to reset password")
    #     else:
    #         conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
    #         crsr= conn.cursor()
    #         query=("select * from register where email=%s")
    #         val=(self.txtemail.get(),)
    #         crsr.execute(query,val)

    #         row=crsr.fetchone()
    #         # print(row)

    #         if row==None:
    #             messagebox.showerror("Error", "Enter email")
    #         else:
    #             conn.close()
    #             self.root2 = Toplevel()
    #             self.root2.title("Forgot Password")
    #             self.root2.geometry("340x450+610+170")

    #             l=tk.Label(self.root, text="Forgot Password", font=("Arial", 24, "bold"), bg="white")
    #             l.place(x=0,y=10,relwidth=1)
                







class Register:
    def __init__(self, root):
        self.root=root
        self.root.title("Shiksha-Mitra SignUp")
        self.root.geometry("1550x800+0+0")


        # ===================================variables
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_psswd=StringVar()
        self.var_confPasswd = StringVar()


        img=Image.open("../proozect/images/login page.jpg")
        img= img.resize((1530,800))
        blurred_image = img.filter(ImageFilter.GaussianBlur(radius=5))
        self.photoimg= ImageTk.PhotoImage(blurred_image)

        lbl= Label(self.root, image=self.photoimg)
        lbl.place(x=0,y=50,width=1530, height=710)


        # title
        title=tk.Label(root, text="ShikshaMitra: A Teacher's Buddy", font=("times new roman", 40, "bold"), bg="#161616", fg="#b99904")
        title.place(x=0, y=0, width=1530, height=80)


        frame= Frame(self.root, bg="white")
        frame.place(x=500, y= 150, width=560, height=520)


        # ============card

        title = tk.Label(frame, text="Sign Up", font=("Arial", 24, "bold"), bg="white")
        title.pack(pady=10)

        subtitle = tk.Label(frame, text="Create a new account", font=("Arial", 16), bg="white", fg="grey")
        subtitle.pack(pady=5)

        # ===========full name
        nameLabel=Label(frame, text="Full Name", font=("Arial", 15, "bold"), fg= "black", bg="white")
        nameLabel.place(x=65, y=110)

        self.txtname= Entry(frame,textvariable= self.var_name, font=("Arial", 15, "bold"), highlightthickness=2,
                 highlightbackground="#dcdcdc",
                 highlightcolor="blue")
        self.txtname.place(x=65, y=140, width= 400, height=40 )

        # ===============email
        emailLabel=Label(frame, text="Email", font=("Arial", 15, "bold"), fg= "black", bg="white")
        emailLabel.place(x=65, y=200)

        self.txtemail= Entry(frame, textvariable= self.var_email, font=("Arial", 15, "bold"), highlightthickness=2,
                 highlightbackground="#dcdcdc",
                 highlightcolor="blue")
        self.txtemail.place(x=65, y=230, width= 400, height=40 )


        # =============psswd
        psswdLabel=Label(frame, text="Password", font=("Arial", 15, "bold"), fg= "black", bg="white")
        psswdLabel.place(x=65, y=300)

        self.txtpsswd= Entry(frame, textvariable= self.var_psswd, font=("Arial", 15, "bold"), highlightthickness=2,
                 highlightbackground="#dcdcdc",
                 highlightcolor="blue")
        self.txtpsswd.place(x=65, y=330, width= 400, height=40 )

        # =============confirm psswd
        # psswdLabel=Label(frame, text="Password", font=("Arial", 15, "bold"), fg= "black", bg="white")
        # psswdLabel.place(x=65, y=300)

        # self.txtpsswd= Entry(frame, textvariable= self.var_psswd, font=("Arial", 15, "bold"), highlightthickness=2,
        #          highlightbackground="#dcdcdc",
        #          highlightcolor="blue")
        # self.txtpsswd.place(x=65, y=330, width= 400, height=40 )

        # register button
        signUpBtn= Button(frame, text="Register", command=self.reg, font=("Arial", 15, "bold"), relief=RIDGE, fg="white", bg="#0b68d4", activeforeground="white", activebackground="#0b68d4")
        signUpBtn.place(x=65, y=400, width=400)

        # login bttn

        # loginBtn= Button(frame, text="Already have an account? Sign In!", font=("Arial", 13),borderwidth=0, relief=RIDGE, fg="#0b68d4", bg="white", activeforeground="#0b68d4", activebackground="white")
        # loginBtn.place(x=65, y=450, width=400)


        # ==========================
    def reg(self):
        if self.var_name.get()== "" or self.var_email.get()=="" :
            messagebox.showerror("Error", "All field required")

        # elif self.var_psswd.get() != self.var_confPasswd.get():
        #     messagebox.showerror("??", "Passwords don't match.")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="root", database="shikshamitra")
            crsr= conn.cursor()
            query =("select * from register where Email=%s")
            val=(self.var_email.get(),)
            crsr.execute(query, val)
            row=crsr.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exists.")
            else:
                crsr.execute("insert into register values(%s,%s,%s)", (
                    self.var_name.get(),
                    self.var_email.get(), 
                    self.var_psswd.get()))
            
            conn.commit()
            conn.close()
            messagebox.showinfo("success", "Successful Registeration")
            self.root.destroy()





if __name__=="__main__":
    main()
    # root= Tk()
    # app= Login(root) 
    # root.mainloop()