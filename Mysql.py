import mysql.connector
from mysql.connector import Error
from tkinter import messagebox, Tk, Label, Entry, Button

class MQSQL:
    def __init__(self, Name, Mail, Username, Password, Security):
        self.Name = Name
        self.Mail = Mail
        self.Username = Username
        self.Password = Password
        self.Security = Security

        try:
            # Connect to MySQL server
            self.db1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crucial_data"
            )
            # Create cursor
            self.cur = self.db1.cursor()
            self.save()
        except Error as e:
            messagebox.showerror(title='Database Connection Error', message=f'An error occurred while connecting to the database: {e}')

    def save(self):
        # Create table if it doesn't exist
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                Name VARCHAR(255),
                Mail VARCHAR(255) PRIMARY KEY,
                Username VARCHAR(255),
                Password VARCHAR(255),
                Security VARCHAR(255)
            )
        """)

        try:
            # Insert user data
            self.cur.execute("""
                INSERT INTO users (Name, Mail, Username, Password, Security) 
                VALUES (%s, %s, %s, %s, %s)
            """, (self.Name, self.Mail, self.Username, self.Password, self.Security))
            self.db1.commit()
            return True
        except Error as e:
            # Check if the error is due to a duplicate entry
            if e.errno == mysql.connector.errorcode.ER_DUP_ENTRY:
                messagebox.showerror(title='Error', message='This email is already registered.')
            else:
                messagebox.showerror(title='Error', message=f'An error occurred: {e}')
            return False

class Existing_user:
    def __init__(self, Mail, Password):
        self.Mail = Mail
        self.Password = Password

        try:
            self.db1 = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="crucial_data"
            )
            # Create cursor
            self.cur = self.db1.cursor()
            self.user_exists = self.existing_user()
        except Error as e:
            messagebox.showerror(title='Database Connection Error', message=f'An error occurred while connecting to the database: {e}')




    def existing_user(self):
        query = """
            SELECT * FROM users
            WHERE Mail = %s AND Password = %s
        """
        self.cur.execute(query, (self.Mail, self.Password))

        # Fetch one row
        result = self.cur.fetchone()
        # print(result)  # For debugging purposes
        return result is not None


class Unique_mail:
    def __init__(self, Mail):
        self.Mail = Mail

        self.db1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="crucial_data")
        self.cur = self.db1.cursor()
        self.user_exists = self.MAIL()

    def MAIL(self):
        query = """
            SELECT * FROM users
            WHERE Mail = %s 
        """
        # Pass the parameter as a tuple
        self.cur.execute(query, (self.Mail,))

        # Fetch one row
        result = self.cur.fetchone()
        # print(result)  # For debugging purposes
        return result is not None


