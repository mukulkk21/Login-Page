from tkinter import messagebox
from tkinter import *
import Login_class
import registration_class

def sign_fun():
    window.destroy()  # Close the main window
    Login_class.login_window()

def sign_up():
    window.destroy()  # Close the main windowk
    registration_class.register_window()

window = Tk()
window.title("Select Window")
window.minsize(200, 150)
window.maxsize(500, 400)
window.geometry("500x400")
window.config(bg='#333333')

frame = Frame(window, bg='#333333')
frame.place(relx=0.5, rely=0.3, anchor=CENTER)  # Center the frame

label_case = Label(frame, text="""


Welcome To Mini Project

We learn because we take challenges
""", bg='#333333', fg='white', font=("Arial", 12))
label_case.pack(pady=5)

# Create a frame for buttons to align them horizontally
button_frame = Frame(frame, bg='#333333')
button_frame.pack(pady=10)

Sign_button = Button(button_frame, text="Sign in", bg='#FF3399', font=("Arial", 12), command=sign_fun)
Sign_button.pack(side='left', padx=5)

click_button = Button(button_frame, text="Sign up", bg='#FF3399', font=("Arial", 12), command=sign_up)
click_button.pack(side='left', padx=5)

window.mainloop()
