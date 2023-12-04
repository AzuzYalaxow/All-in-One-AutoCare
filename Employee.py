import sqlite3
from sqlite3 import Error
from getpass import getpass


class Employee:
    emp_id=0
    name=""
    age=0
    email=""
    password=""
    phone=0
    salary=""
    department=""
    

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    conn=sqlite3.connect("aioa.db")
    
    def createEmpTable():
        conn.execute(''' CREATE TABLE Employee(
                emp_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL,
                phone INTEGER NOT NULL,
                salary TEXT NOT NULL,
                department TEXT NOT NULL);
''')
        conn.close()
    
    def insertValues():
        emp=Employee()
        emp.name=input("Enter name of emp: ")
        emp.age=input("Enter age of emp: ")
        emp.email=input("Enter email of emp: ")
        emp.password=getpass()
        emp.phone=input("Enter phone of emp: ")
        emp.salary=input("Enter salary of emp: ")
        emp.department=input("Enter the departmant of emp: ")
        
        conn.execute(f''' INSERT INTO Employee VALUES(
                    '{emp.name}',
                    {emp.age},
                    '{emp.email}',
                    '{emp.password}',
                    {emp.phone},
                    '{emp.salary}',
                    '{emp.department}');
''')
        print("Added seccesfuly")
        conn.close()
    insertValues()

    