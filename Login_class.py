from tkinter import messagebox
from tkinter import *
import file_saving  # Assuming this is the correct module for saving functions
import registration_class
import reset_passward
import Mysql

def login_window():
    # Create a new Tkinter window instance
    login_win = Tk()
    login_win.title("Login")
    login_win.maxsize(500,400)
    login_win.geometry("500x400")
    login_win.config(bg='#333333')

    # Configure the grid to center widgets
    login_win.columnconfigure(0, weight=1)
    login_win.columnconfigure(1, weight=1)

    login_label = Label(login_win, text="Login Window", bg='#333333', fg='white', font=("Arial", 14))
    login_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Add Username label and entry
    Username_label = Label(login_win, text="Email ID", bg='#333333', fg='white')
    Username_label.grid(row=1, column=0, pady=10, padx=10, sticky='e')
    Username_entry = Entry(login_win, bg='white')
    Username_entry.grid(row=1, column=1, pady=10, padx=10, sticky='w')

    # Add Password label and entry
    Password_label = Label(login_win, text="Password", bg='#333333', fg='white')
    Password_label.grid(row=2, column=0, pady=10, padx=10, sticky='e')
    Password_entry = Entry(login_win, bg='white', show='*')
    Password_entry.grid(row=2, column=1, pady=10, padx=10, sticky='w')

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"

    Username_entry.bind("<Return>", focus_next_widget)
    Password_entry.bind("<Return>", focus_next_widget)

    def Match1():
        us = Username_entry.get()
        pas = Password_entry.get()
        if len(us) == 0 or len(pas) == 0:
            messagebox.showinfo("Error", "Please enter a valid username and password")
        else:
            user = Mysql.Existing_user(us, pas)
            if user.user_exists:
                messagebox.showinfo(title='Success', message='You have successfully logged in')
                login_win.destroy()
            else:
                messagebox.showwarning(title='Warning', message='Incorrect username or password')

    def signUP():
        login_win.destroy()
        registration_class.register_window()
    def reset() :
        mail = Username_entry.get()
        pas = Password_entry.get()
        login_win.destroy()
        reset_passward.Reset(mail, pas)


    # Sign in button
    Sign_label = Button(login_win, text="Sign in", bg='#FF3399', command=Match1)
    Sign_label.grid(row=3, column=0, columnspan=2, pady=10)
    reset_Button = Button(login_win, text="Reset", bg='white', command=reset)
    reset_Button.grid(row=3, column=1, pady=10)
    # note_label = Label(login_win, text="Existing user?", bg='#333333', fg='white')
    # note_label.grid(row=4, column=0, columnspan=2, pady=10)

    # Add Quit and Sign up buttons
    sign_up_button = Button(login_win, text="Sign up", bg='white', command=signUP)
    sign_up_button.grid(row=4, column=0, columnspan=2, pady=10)

    quit_button = Button(login_win, text="Quit", bg='white', command=login_win.destroy)
    quit_button.grid(row=4, column=1, columnspan=4, pady=10)

    login_win.mainloop()
