import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def sign_up():
    full_name = entry_fullname.get()
    email = entry_email.get()
    password = entry_password.get()
    if full_name and email and password:
        messagebox.showinfo("Success", "Signed up successfully!")
    else:
        messagebox.showwarning("Input error", "Please fill in all fields.")

# Create main window
root = tk.Tk()
root.title("ShikshaMitra - Sign Up")
root.geometry("800x600")

# Load and display background image
bg_image = Image.open("../proozect/images/login page.jpg")
bg_image = bg_image.resize((800, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Overlay frame
frame = tk.Frame(root, bg="white", bd=2)
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=300)

# Title
title = tk.Label(frame, text="Sign Up", font=("Helvetica", 18, "bold"), bg="white")
title.pack(pady=10)

subtitle = tk.Label(frame, text="Create a new account", font=("Helvetica", 10), bg="white")
subtitle.pack()

# Full Name
tk.Label(frame, text="Full Name", bg="white").pack(anchor="w", padx=20, pady=(10, 0))
entry_fullname = tk.Entry(frame, width=40)
entry_fullname.pack(padx=20)

# Email
tk.Label(frame, text="Email", bg="white").pack(anchor="w", padx=20, pady=(10, 0))
entry_email = tk.Entry(frame, width=40)
entry_email.pack(padx=20)

# Password
tk.Label(frame, text="Password", bg="white").pack(anchor="w", padx=20, pady=(10, 0))
entry_password = tk.Entry(frame, show='*', width=40)
entry_password.pack(padx=20)

# Sign Up Button
signup_btn = tk.Button(frame, text="Sign Up", bg="#007bff", fg="white", width=30, command=sign_up)
signup_btn.pack(pady=15)

# Sign In Link
signin_label = tk.Label(frame, text="Already have an account? Sign In", fg="blue", bg="white", cursor="hand2")
signin_label.pack()

root.mainloop()
