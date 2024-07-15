

---

# Mini Project: User Authentication System

Welcome to the User Authentication System project! This repository contains a simple user authentication system built using Python's Tkinter library and MySQL for database management. The project includes functionalities for user registration, login, quit and password reset.

## Features

- **User Registration**: New users can register by providing their details.
- **User Login**: Existing users can log in using their email and password.
- **Password Reset**: Users can reset their password by answering a security question.
- **Data Storage**: User data is stored in a MySQL database.

## Project Structure

```
.
├── main.py                    # Main file to launch the application
├── Login_class.py             # Contains the login window and related functions
├── registration_class.py      # Contains the registration window and related functions
├── Mysql.py                   # Handles database connections and queries
├── reset_password.py          # Contains the password reset window and related functions
├── file_saving.py             # Handles file saving operations (if needed)
└── README.md                  # This file
```

## Requirements

- Python 3.x
- Tkinter
- MySQL

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install the required Python libraries**:

    ```bash
    pip install mysql-connector-python
    ```

3. **Set up the MySQL database**:

    - Install MySQL server if it's not already installed.
    - Create a database named `crucial_data`.
    - Ensure the MySQL server is running.

4. **Modify database connection settings**:

    Update the MySQL connection settings in the `Mysql.py` file to match your local MySQL server configuration:

    ```python
    self.db1 = mysql.connector.connect(
        host="localhost",
        user="your-username",
        password="your-password",
        database="crucial_data"
    )
    ```

5. **Run the application**:

    ```bash
    python main.py
    ```

## Usage

- **Sign In**: Click on the "Sign in" button to open the login window.
- **Sign Up**: Click on the "Sign up" button to open the registration window.
- **Password Reset**: Click on the "Reset" button in the login window to reset your password.
- **Quit**: Click on the "Quit" button in the Login_page to exit from program

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.



## Acknowledgments

This project was developed as a learning exercise to practice building a user authentication system using Python and MySQL.


