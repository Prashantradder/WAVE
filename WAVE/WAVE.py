import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Pillow library for image handling

# Function to handle the login process
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # For demonstration purposes, we'll use a hardcoded username and password
    if username == "ur" and password == "ps":
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()  # Close the login window
        open_dashboard()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
# Function to open the dashboard window
def open_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("300x400")

    # Buttons for different functionalities
    button_info = tk.Button(dashboard, text="Information", width=20)
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
background_image = Image.open("F:\WAVE\Screenshot 2024-05-15 133808.png")
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
# Function to open the dashboard window
def open_dashboard():
    dashboard = tk.Toplevel()
    dashboard.title("Dashboard")
    dashboard.geometry("900x800")

    # Buttons for different functionalities
    button_info = tk.Button(dashboard, text="Information", width=20)
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

# Running the application
root.mainloop()
