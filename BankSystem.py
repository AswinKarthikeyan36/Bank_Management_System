import mysql.connector
from datetime import datetime

# database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Hubnet"
)

cursor = conn.cursor()

# create account
def create_account():
    name = input("Enter Name: ")
    username = input("Create Username: ")
    password = input("Create Password: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    address = input("Enter Address: ")
    mobile = input("Enter Mobile Number: ")
    aadhar = input("Enter Aadhar Number: ")
    balance = int(input("Enter Initial Balance: "))

    query = "INSERT INTO bank VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (name, username, password, dob, address, mobile, aadhar, balance)

    cursor.execute(query, values)
    conn.commit()

    print("Account Created Successfully")


# login
def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    query = "SELECT * FROM bank WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()

    if result:
        print("Login Successful")
        user_menu(username)
    else:
        print("Invalid Login")


# deposit money
def deposit(username):
    amount = int(input("Enter amount to deposit: "))

    cursor.execute("UPDATE bank SET balance=balance+%s WHERE username=%s", (amount, username))
    cursor.execute("INSERT INTO transactions VALUES(%s,%s,%s)", (amount,0,username))

    conn.commit()

    print("Amount Deposited")


# withdraw money
def withdraw(username):
    amount = int(input("Enter amount to withdraw: "))

    cursor.execute("SELECT balance FROM bank WHERE username=%s",(username,))
    balance = cursor.fetchone()[0]

    if amount > balance:
        print("Insufficient Balance")
    else:
        cursor.execute("UPDATE bank SET balance=balance-%s WHERE username=%s",(amount,username))
        cursor.execute("INSERT INTO transactions VALUES(%s,%s,%s)",(0,amount,username))

        conn.commit()
        print("Amount Withdrawn")


# check balance
def check_balance(username):

    cursor.execute("SELECT balance FROM bank WHERE username=%s",(username,))
    balance = cursor.fetchone()[0]

    print("Your Balance is:",balance)


# view transactions
def transaction_history(username):

    cursor.execute("SELECT * FROM transactions WHERE username1=%s",(username,))

    for row in cursor.fetchall():
        print(row)


# user menu
def user_menu(username):

    while True:

        print("\n1 Deposit")
        print("2 Withdraw")
        print("3 Check Balance")
        print("4 Transaction History")
        print("5 Logout")

        choice = int(input("Enter choice: "))

        if choice==1:
            deposit(username)

        elif choice==2:
            withdraw(username)

        elif choice==3:
            check_balance(username)

        elif choice==4:
            transaction_history(username)

        elif choice==5:
            break


# main menu
while True:

    print("\n--- COLONY BANK OF INDIA ---")
    print("1 Create Account")
    print("2 Login")
    print("3 Exit")

    choice = int(input("Enter choice: "))

    if choice==1:
        create_account()

    elif choice==2:
        login()

    elif choice==3:
        break