from tkinter import messagebox
from tkinter import *
# import file_saving
import Login_class
# import reset_passward
import Mysql
# import sys


def register_window():
    register_win = Tk()
    register_win.title("Register")
    register_win.maxsize(800,600)
    register_win.geometry("800x500")
    register_win.config(bg='#333333')

    form_frame = Frame(register_win, bg='#333333')
    form_frame.pack(pady=50)

    # Add your registration widgets here
    register_label = Label(form_frame, text="Register Window", bg='#333333', fg='white', font=("Arial", 18))
    register_label.grid(row=0, column=1, columnspan=2, pady=10)

    Name_label = Label(form_frame, text="Name", bg='#333333', fg='white', font=("Arial", 14))
    Name_label.grid(row=1, column=0, pady=5, padx=5, sticky=E)
    Name_entry = Entry(form_frame, bg='white', fg='black', width=30)
    Name_entry.grid(row=1, column=1, pady=5, padx=5, sticky=W)

    Username_label = Label(form_frame, text="Username", bg='#333333', fg='white', font=("Arial", 14))
    Username_label.grid(row=2, column=0, pady=5, padx=5, sticky=E)
    Username_entry = Entry(form_frame, bg='white', fg='black', width=30)
    Username_entry.grid(row=2, column=1, pady=5, padx=5, sticky=W)

    Password_label = Label(form_frame, text="Password", bg='#333333', fg='white', font=("Arial", 14))
    Password_label.grid(row=3, column=0, pady=5, padx=5, sticky=E)
    Password_entry = Entry(form_frame, bg='white', fg='black', width=30, show='*')
    Password_entry.grid(row=3, column=1, pady=5, padx=5, sticky=W)

    Email_label = Label(form_frame, text="Email", bg='#333333', fg='white', font=("Arial", 14))
    Email_label.grid(row=4, column=0, pady=5, padx=5, sticky=E)
    Email_entry = Entry(form_frame, bg='white', fg='black', width=30)
    Email_entry.grid(row=4, column=1, pady=5, padx=5, sticky=W)

    Security_label = Label(form_frame, text="Enter your best friend's name", bg='#333333', fg='white',
                           font=("Arial", 14))
    Security_label.grid(row=5, column=0, pady=5, padx=5, sticky=E)
    Security_entry = Entry(form_frame, bg='white', fg='black', width=30)
    Security_entry.grid(row=5, column=1, pady=5, padx=5, sticky=W)

    # Function to move focus to the next entry
    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return "break"

    # Bind Enter key to each entry widget
    Name_entry.bind("<Return>", focus_next_widget)
    Username_entry.bind("<Return>", focus_next_widget)
    Password_entry.bind("<Return>", focus_next_widget)
    Email_entry.bind("<Return>", focus_next_widget)
    Security_entry.bind("<Return>", focus_next_widget)

    def pass_save():
        name = Name_entry.get()
        us = Username_entry.get()
        pas = Password_entry.get()
        mail = Email_entry.get()
        sec = Security_entry.get()

        if not name or not us or not pas or not mail or not sec:
            messagebox.showerror(title='Error', message='All fields must be filled out')
            return

        # Check if the email already exists in the database
        user =Mysql.Unique_mail(mail)
        if user.user_exists:
            messagebox.showerror(title='Error', message='This email is already registered.')
              # This will be executed if the email already exists
        else:
            # If the email doesn't exist, insert the information into the database
            Mysql.MQSQL(name, mail, us, pas, sec)
            # file_saving.Save(name, mail, us, pas, sec)
            messagebox.showinfo(title='Success', message='You have successfully signed up')
            register_win.destroy()
            register_window()
    def signIn():
        register_win.destroy()
        Login_class.login_window()

    # def reset() :
    #     mail = Username_entry.get()
    #     pas = Password_entry.get()
    #     register_win.destroy()
    #     reset_passward.Reset(mail, pas)

    explanation_label = Label(form_frame, text="This will help you to recover your password if you forget it.",
                              bg='#333333', fg='white', font=("Arial", 10))
    explanation_label.grid(row=6, column=1, columnspan=2, pady=5)

    signUp_button = Button(form_frame, text="Sign up", bg='white', font=("Arial", 12), command=pass_save)
    signUp_button.grid(row=7, column=1, pady=5, padx=5, sticky=W)

    signIn_button = Button(form_frame, text="Sign in", bg='white', font=("Arial", 12), command=signIn)
    signIn_button.grid(row=7, column=1, pady=5, padx=5, sticky=E)

    quit_button = Button(form_frame, text="Quit", bg='white', font=("Arial", 12), command=register_win.destroy)
    quit_button.grid(row=7, column=2, pady=5, padx=5, sticky=E)

    register_win.mainloop()
