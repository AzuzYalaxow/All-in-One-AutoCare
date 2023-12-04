import sqlite3
from sqlite3 import Error
from getpass import getpass
from prettytable import PrettyTable

class Employee:
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            print(sqlite3.version)
            return conn
        except Error as e:
            print(e)
        return conn

    def createEmpTable(conn):
        try:
            conn.execute(''' CREATE TABLE IF NOT EXISTS Employee(
                    emp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL,
                    email TEXT NOT NULL,
                    password TEXT NOT NULL,
                    phone INTEGER NOT NULL,
                    salary TEXT NOT NULL,
                    department TEXT NOT NULL);
            ''')
            conn.commit()
            print("Table created successfully")
        except Error as e:
            print(e)

    def insertEmployee(conn):
        try:
            emp = Employee()
            emp.name = input("Enter name of emp: ")
            emp.age = int(input("Enter age of emp: "))
            emp.email = input("Enter email of emp: ")
            emp.password = getpass()
            emp.phone = int(input("Enter phone of emp: "))
            emp.salary = input("Enter salary of emp: ")
            emp.department = input("Enter the department of emp: ")

            conn.execute(f''' INSERT INTO Employee 
                            (name, age, email, password, phone, salary, department)
                            VALUES (
                            '{emp.name}', {emp.age}, '{emp.email}', 
                            '{emp.password}', {emp.phone}, '{emp.salary}', '{emp.department}');
            ''')
            conn.commit() 
            print("Employee added successfully")
        except Error as e:
            print(e)

    def deleteEmployee(conn, emp_id):
        try:
            conn.execute(f"DELETE FROM Employee WHERE emp_id = {emp_id};")
            conn.commit() 
            print("Employee deleted successfully")
        except Error as e:
            print(e)

    def updateEmployee(conn, emp_id):
        try:
            new_phone = input("Enter new phone number: ")
            new_salary = input("Enter new salary: ")

            conn.execute(f'''UPDATE Employee 
                            SET phone = '{new_phone}', salary = '{new_salary}' 
                            WHERE emp_id = {emp_id};
            ''')
            conn.commit()
            print("Employee updated successfully")
        except Error as e:
            print(e)

    def displayEmployees(conn):
        try:
            cursor = conn.execute("SELECT * FROM Employee")
            
            table = PrettyTable()
            table.field_names = [i[0] for i in cursor.description]
            
            for row in cursor.fetchall():
                table.add_row(row)

            print(table)
        except Error as e:
            print(e)

def main():
    conn = Employee.create_connection("aioa.db")
    Employee.createEmpTable(conn)

    print("Choose an operation:")
    print("1. Insert Employee")
    print("2. Delete Employee")
    print("3. Update Employee")
    print("4. Display Employees")

    choice = int(input("Enter the number corresponding to the operation: "))

    if choice == 1:
        Employee.insertEmployee(conn)
        main()
    elif choice == 2:
        emp_id = int(input("Enter the ID of the employee to delete: "))
        Employee.deleteEmployee(conn, emp_id)
        main()
    elif choice == 3:
        emp_id = int(input("Enter the ID of the employee to update: "))
        Employee.updateEmployee(conn, emp_id)
        main()
    elif choice == 4:
        Employee.displayEmployees(conn)
        main()
    else:
        print("Invalid choice. Please choose a valid number.")
        main()
    conn.close()

if __name__ == '__main__':
    main()
