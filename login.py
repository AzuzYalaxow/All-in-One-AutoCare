import sqlite3
from sqlite3 import Error
from getpass import getpass
from sales import CarSales, main_sale
from rent import CarRent, main_rent
from repair import CarRepair, main_repair
from clean import Clean, main_clean

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
                print("Login successful! Welcome, " + employee[1])  
                department_page(conn, employee[0], employee[7])  
            else:
                print("Login failed. Invalid email or password.")
        except Error as e:
            print(e)

def department_page(conn, emp_id, department):
    if department == 'sales':
        car_sales = CarSales()
        
        print(f"Welcome to the Sales Department, Employee ID: {emp_id}")
        main_sale()

    elif department == 'rent':
        car_rent = CarRent()
        print(f"Welcome to the Rent Department, Employee ID: {emp_id}")
        main_rent()

    elif department == 'repair':
        car_repair = CarRepair()
        print(f"Welcome to the Repair Department, Employee ID: {emp_id}")
        main_repair()

    elif department == 'clean':
        cleaner = Clean()
        print(f"Welcome to the Clean Department, Employee ID: {emp_id}")
        main_clean()

    else:
        print("Invalid department. Please contact your administrator.")

def main():
    conn = Login.create_connection("aioa.db")
    Login.login_employee(conn)
    main()

if __name__ == '__main__':
    main()
