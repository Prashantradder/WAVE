import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow library for image handling
import os

# File to store user credentials
CREDENTIALS_FILE = "user_credentials.txt"

# Function to load user credentials from file
def load_credentials():
    credentials = {}
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "r") as file:
            for line in file:
                username, password = line.strip().split(":")
                credentials[username] = password
    return credentials

# Function to save user credentials to file
def save_credentials(username, password):
    with open(CREDENTIALS_FILE, "a") as file:
        file.write(f"{username}:{password}\n")

# Load existing user credentials
user_credentials = load_credentials()

# Function to handle the login process
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in user_credentials and user_credentials[username] == password:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()  # Close the login window
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle the registration process
def register():
    reg_username = entry_reg_username.get()
    reg_password = entry_reg_password.get()
    
    if reg_username in user_credentials:
        messagebox.showerror("Registration Failed", "Username already exists")
    else:
        user_credentials[reg_username] = reg_password
        save_credentials(reg_username, reg_password)
        messagebox.showinfo("Registration Successful", "User registered successfully")
        register_window.destroy()

# Function to open the registration window
def open_register_window():
    global register_window, entry_reg_username, entry_reg_password
    
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("300x200")
    
    label_reg_username = tk.Label(register_window, text="Username")
    label_reg_username.pack(pady=5)
    
    entry_reg_username = tk.Entry(register_window)
    entry_reg_username.pack(pady=5)
    
    label_reg_password = tk.Label(register_window, text="Password")
    label_reg_password.pack(pady=5)
    
    entry_reg_password = tk.Entry(register_window, show="*")
    entry_reg_password.pack(pady=5)
    
    button_register = tk.Button(register_window, text="Register", command=register)
    button_register.pack(pady=10)

# Function to open the student information window
def show_information():
    info_window = tk.Toplevel()
    info_window.title("Student Information")
    info_window.geometry("300x200")

    # Add labels and other widgets to display student information
    label_info = tk.Label(info_window, text="Student Information", font=("Helvetica", 16))
    label_info.pack(pady=10)

    label_name = tk.Label(info_window, text="Name: John Doe")
    label_name.pack(pady=5)

    label_id = tk.Label(info_window, text="Student ID: 123456")
    label_id.pack(pady=5)

    label_course = tk.Label(info_window, text="Course: Computer Science")
    label_course.pack(pady=5)

    label_year = tk.Label(info_window, text="Year: Sophomore")
    label_year.pack(pady=5)

# Function to open the dashboard window
def open_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("300x400")

    # Buttons for different functionalities
    button_info = tk.Button(dashboard, text="Information", width=20, command=show_information)
    button_info.pack(pady=10)

    button_result = tk.Button(dashboard, text="Result", width=20)
    button_result.pack(pady=10)

    button_setting = tk.Button(dashboard, text="Setting Information", width=20)
    button_setting.pack(pady=10)

    button_course = tk.Button(dashboard, text="My Course", width=20)
    button_course.pack(pady=10)

    button_timetable = tk.Button(dashboard, text="Timetable", width=20)
    button_timetable.pack(pady=10)

    button_payment = tk.Button(dashboard, text="Online Payment", width=20)
    button_payment.pack(pady=10)

# Creating the main window
root = tk.Tk()
root.title("Student Login Page")

# Setting the window size
root.geometry("900x800")

# Load the background image
background_image = Image.open("f:\WAVE-main\WAVE\Screenshot 2024-05-15 133808.png")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas and set the background image
canvas = tk.Canvas(root, width=1000, height=800)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Creating and placing the username label and entry
label_username = tk.Label(root, text="Username", bg="white")
label_username_window = canvas.create_window(500, 250, anchor="center", window=label_username)

entry_username = tk.Entry(root)
entry_username_window = canvas.create_window(500, 275, anchor="center", window=entry_username)

# Creating and placing the password label and entry
label_password = tk.Label(root, text="Password", bg="white")
label_password_window = canvas.create_window(500, 310, anchor="center", window=label_password)

entry_password = tk.Entry(root, show="*")
entry_password_window = canvas.create_window(500, 335, anchor="center", window=entry_password)

# Creating and placing the login button
button_login = tk.Button(root, text="Login", command=login)
button_login_window = canvas.create_window(500, 380, anchor="center", window=button_login)

# Creating and placing the register button
button_register = tk.Button(root, text="Sign In", command=open_register_window)
button_register_window = canvas.create_window(500, 420, anchor="center", window=button_register)

# Running the application
root.mainloop()
