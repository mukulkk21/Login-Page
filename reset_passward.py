from tkinter import *
from tkinter import messagebox
import mysql.connector
import Login_class

class Reset:
    def __init__(self, mail, security):
        self.mail = mail
        self.security = security
        self.db1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crucial_data")
        self.cur = self.db1.cursor()
        self.reset()

    def reset(self):
        reset_window = Tk()
        reset_window.title("Reset Password")
        reset_window.maxsize(500,500)
        reset_window.geometry("500x200")
        reset_window.config(bg="#333333")
        reset_window.minsize(500, 400)
        # Frame to hold labels and entry fields
        frame = Frame(reset_window, bg="#333333")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        def focus_next_entry(event):
            event.widget.tk_focusNext().focus()
            return "break"

        # Mail
        mail_label = Label(frame, text="Mail", bg="white", fg="black")
        mail_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        mail_entry = Entry(frame)
        mail_entry.grid(row=0, column=1, padx=10, pady=5)
        mail_entry.insert(0, self.mail)  # Insert the provided mail into the entry

        # Security
        security_label = Label(frame, text="Security", bg="white", fg="black")
        security_label.grid(row=0, column=2, padx=10, pady=5, sticky="e")
        security_entry = Entry(frame)
        security_entry.grid(row=0, column=3, padx=10, pady=5)

        # New Password
        new_password_label = Label(frame, text="New Password", bg="white", fg="black")
        new_password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        new_password_entry = Entry(frame, show="*")
        new_password_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=5, sticky="ew")

        # Bind Enter key to move focus to the next entry box
        security_entry.bind("<Return>", focus_next_entry)
        mail_entry.bind("<Return>", focus_next_entry)
        new_password_entry.bind("<Return>", lambda event: check_and_reset())  # Call check_and_reset on Enter key

        # Set the focus on the security entry
        security_entry.focus()

        # Function to check if email and security match a record in the database and update password
        def check_and_reset():
            if new_password_entry.get() == "":
                messagebox.showerror("Error", "Please enter your new password")
            else:
                query = """
                    SELECT * FROM users
                    WHERE Mail = %s AND Security = %s
                """
                self.cur.execute(query, (mail_entry.get(), security_entry.get()))
                result = self.cur.fetchone()
                if result:
                    new_password = new_password_entry.get()
                    update_query = """
                        UPDATE users
                        SET Password = %s
                        WHERE Mail = %s
                    """
                    self.cur.execute(update_query, (new_password, mail_entry.get()))
                    self.db1.commit()
                    messagebox.showinfo("Success", "Password reset successful")  # Show success message
                    reset_window.destroy()
                    Login_class.login_window()
                else:
                    messagebox.showerror("Error", "Invalid email or security")

        def login():
            reset_window.destroy()
            Login_class.login_window()

        # Reset Button
        reset_button = Button(frame, text="Reset", command=check_and_reset, bg="#FF3399", width=10)
        reset_button.grid(row=2, column=1, columnspan=2, padx=10, pady=10)

        # Login Button
        login_button = Button(frame, text="Login", command=login, bg="#FF3399", width=10)
        login_button.grid(row=2, column=3, columnspan=2, padx=10, pady=10)

        reset_window.mainloop()
