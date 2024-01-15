import sqlite3
from prettytable import PrettyTable
from datetime import datetime

class CarRepair:
    def __init__(self, db_name='aioa.db'):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS car_repair (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_tag TEXT,
            car_name TEXT,
            date TEXT,
            car_status TEXT,
            email TEXT,
            phone TEXT
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_car_to_repair(self):
        car_tag = input("Enter Car Tag: ")
        car_name = input("Enter Car Name: ")
        car_status = "Pending"
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        query = '''
        INSERT INTO car_repair (car_tag, car_name, date, car_status, email, phone)
        VALUES (?, ?, ?, ?, ?, ?);
        '''
        self.conn.execute(query, (car_tag, car_name, date, car_status, email, phone))
        self.conn.commit()
        print(f"Car with tag '{car_tag}' added to repair.")

    def repair_car(self):
        car_tag = input("Enter Car Tag to mark as repaired: ")
        query = '''
        UPDATE car_repair
        SET car_status = 'Repaired'
        WHERE car_tag = ?;
        '''
        self.conn.execute(query, (car_tag,))
        self.conn.commit()
        print(f"Car with tag '{car_tag}' has been marked as repaired.")

    def display_repairs(self):
        query = '''
        SELECT * FROM car_repair;
        '''
        result = self.conn.execute(query).fetchall()

        if not result:
            print("No repairs found.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Car Tag", "Car Name", "Date", "Car Status", "Email", "Phone"]

        for row in result:
            table.add_row(row)

        print(table)

    def display_queue(self):
        query = '''
        SELECT * FROM car_repair
        WHERE car_status = 'Pending'
        ORDER BY date;
        '''
        result = self.conn.execute(query).fetchall()

        if not result:
            print("No cars in the repair queue.")
            return

        table = PrettyTable()
        table.field_names = ["ID", "Car Tag", "Car Name", "Date", "Car Status", "Email", "Phone"]

        for row in result:
            table.add_row(row)

        print(table)

    def close_connection(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    car_repair_manager = CarRepair()

    while True:
        print("\nMenu:")
        print("1. Add Car to Repair")
        print("2. Mark Car as Repaired")
        print("3. Display Repairs")
        print("4. Display Queue")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            car_repair_manager.add_car_to_repair()
        elif choice == '2':
            car_repair_manager.repair_car()
        elif choice == '3':
            car_repair_manager.display_repairs()
        elif choice == '4':
            car_repair_manager.display_queue()
        elif choice == '5':
            car_repair_manager.close_connection()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
