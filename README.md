# Bank_Management_System
The Virtual Bank Management System is a console-based banking application developed using Python and MySQL. This project simulates a basic banking environment where bank staff can manage customer records, perform transactions, and maintain account details securely.
The system stores all customer information in a MySQL database and performs CRUD operations (Create, Read, Update, Delete) using Python. The application also includes user authentication, ensuring that only authorized users can access the banking system.

The project demonstrates the use of database connectivity in Python, exception handling, and basic banking operations in a structured and user-friendly way.

🚀 Features

🔐 User Authentication

Login with username and password

New user registration

👤 Customer Account Management

Create new customer account

View all customer records

View a specific customer account

💰 Bank Transactions

Deposit money

Withdraw money

Track transaction history

🛠 Record Management

Update customer details

Delete customer records

⚠️ Exception Handling

Handles invalid inputs and database errors gracefully

🧑‍💻 Technologies Used

Python

MySQL

mysql.connector (Python MySQL driver)

VS Code / Python IDLE

📂 Database Structure
Bank Table

Stores customer account information.

CREATE TABLE bank(
name VARCHAR(30),
UserName VARCHAR(30) PRIMARY KEY,
password TINYTEXT,
Date_of_birth DATE,
address VARCHAR(40),
Mobile_Number VARCHAR(30),
Aadhar_no VARCHAR(30),
Balance INT
);
Transaction Table

Stores deposit and withdrawal details.

CREATE TABLE Transaction(
credited INT,
debited INT,
username1 VARCHAR(20),
FOREIGN KEY(username1) REFERENCES bank(username)
);
⚙️ Requirements

Make sure the following are installed before running the project:

Python (3.x)

MySQL Server

MySQL Connector for Python

Install MySQL connector using:

pip install mysql-connector-python
▶️ How to Run the Project

Install Python and MySQL.

Create the bank database in MySQL.

Create the required tables using the SQL commands above.

Update the database connection credentials in the Python code:

mysql.connector.connect(
host="localhost",
user="root",
password="12345678",
database="bank"
)

Run the Python file:

python bank_project.py
