import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow library for image handling
import json

# File to store user credentials and details
CREDENTIALS_FILE = "user_credentials.json"

# Load user credentials from file
def load_credentials():
    try:
        with open(CREDENTIALS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save user credentials to file
def save_credentials(credentials):
    with open(CREDENTIALS_FILE, "w") as file:
        json.dump(credentials, file, indent=4)

# Initialize credentials
user_credentials = load_credentials()

# Function to handle the login process
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username in user_credentials and user_credentials[username]['password'] == password:
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()  # Close the login window
        open_dashboard(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Function to handle the registration process
def register():
    reg_username = entry_reg_username.get()
    reg_password = entry_reg_password.get()
    reg_name = entry_reg_name.get()
    reg_age = entry_reg_age.get()
    reg_section = entry_reg_section.get()
    reg_course = entry_reg_course.get()
    reg_address = entry_reg_address.get()
    
    if reg_username in user_credentials:
        messagebox.showerror("Registration Failed", "Username already exists")
    else:
        user_credentials[reg_username] = {
            'password': reg_password,
            'name': reg_name,
            'age': reg_age,
            'section': reg_section,
            'course': reg_course,
            'address': reg_address
        }
        save_credentials(user_credentials)
        messagebox.showinfo("Registration Successful", "User registered successfully")
        register_window.destroy()

# Function to open the registration window
def open_register_window():
    global register_window, entry_reg_username, entry_reg_password, entry_reg_name, entry_reg_age, entry_reg_section, entry_reg_course, entry_reg_address
    
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("300x400")
    
    label_reg_username = tk.Label(register_window, text="Username")
    label_reg_username.pack(pady=5)
    
    entry_reg_username = tk.Entry(register_window)
    entry_reg_username.pack(pady=5)
    
    label_reg_password = tk.Label(register_window, text="Password")
    label_reg_password.pack(pady=5)
    
    entry_reg_password = tk.Entry(register_window, show="*")
    entry_reg_password.pack(pady=5)
    
    label_reg_name = tk.Label(register_window, text="Name")
    label_reg_name.pack(pady=5)
    
    entry_reg_name = tk.Entry(register_window)
    entry_reg_name.pack(pady=5)
    
    label_reg_age = tk.Label(register_window, text="Age")
    label_reg_age.pack(pady=5)
    
    entry_reg_age = tk.Entry(register_window)
    entry_reg_age.pack(pady=5)
    
    label_reg_section = tk.Label(register_window, text="Section")
    label_reg_section.pack(pady=5)
    
    entry_reg_section = tk.Entry(register_window)
    entry_reg_section.pack(pady=5)
    
    label_reg_course = tk.Label(register_window, text="Course")
    label_reg_course.pack(pady=5)
    
    entry_reg_course = tk.Entry(register_window)
    entry_reg_course.pack(pady=5)
    
    label_reg_address = tk.Label(register_window, text="Home Address")
    label_reg_address.pack(pady=5)
    
    entry_reg_address = tk.Entry(register_window)
    entry_reg_address.pack(pady=5)
    
    button_register = tk.Button(register_window, text="Register", command=register)
    button_register.pack(pady=10)

# Function to open the student information window
def show_information(username):
    info_window = tk.Toplevel()
    info_window.title("Student Information")
    info_window.geometry("300x200")

    # Retrieve student details
    student_info = user_credentials[username]

    # Add labels and other widgets to display student information
    label_info = tk.Label(info_window, text="Student Information", font=("Helvetica", 16))
    label_info.pack(pady=10)

    label_name = tk.Label(info_window, text=f"Name: {student_info['name']}")
    label_name.pack(pady=5)

    label_age = tk.Label(info_window, text=f"Age: {student_info['age']}")
    label_age.pack(pady=5)

    label_section = tk.Label(info_window, text=f"Section: {student_info['section']}")
    label_section.pack(pady=5)

    label_course = tk.Label(info_window, text=f"Course: {student_info['course']}")
    label_course.pack(pady=5)

    label_address = tk.Label(info_window, text=f"Home Address: {student_info['address']}")
    label_address.pack(pady=5)

# Function to open the dashboard window
def open_dashboard(username):
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("300x400")

    # Buttons for different functionalities
    button_info = tk.Button(dashboard, text="Information", width=20, command=lambda: show_information(username))
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
