import sqlite3
from sqlite3 import Error
from getpass import getpass

class Login:
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
        return conn
    
    def login_employee(conn):
        try:
            email = input("Enter your email: ")
            password = getpass("Enter your password: ")

            cursor = conn.execute(f"SELECT * FROM Employee WHERE email = '{email}' AND password = '{password}'")
            employee = cursor.fetchone()

            if employee:
                print("Login successful! Welcome, " + employee[1])  # Assuming the name is stored in the second column
                department_page(conn, employee[0])  # Redirect to department page, passing emp_id
            else:
                print("Login failed. Invalid email or password.")
        except Error as e:
            print(e)

def department_page(conn, emp_id):
    # Add your department-specific logic here
    print(f"Welcome to the department page, Employee ID: {emp_id}")

# ... (rest of the code)

def main():
   conn = Login.create_connection("aioa.db")
   Login.login_employee(conn)
   main()
if __name__ == '__main__':
    main()
