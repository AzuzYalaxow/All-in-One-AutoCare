import sqlite3
from prettytable import PrettyTable
from datetime import datetime, timedelta

class Clean:
    def __init__(self, database_name='aioa.db'):
        self.conn = sqlite3.connect(database_name)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cleaning_records (
                car_tag TEXT PRIMARY KEY,
                customer_name TEXT,
                phone_number TEXT,
                date_taken TEXT,
                cleaned BOOLEAN
            )
        ''')
        self.conn.commit()

    def add_cleaning_record(self, car_tag, customer_name, phone_number, date_taken):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO cleaning_records (car_tag, customer_name, phone_number, date_taken, cleaned)
            VALUES (?, ?, ?, ?, 0)
            ON CONFLICT(car_tag) DO NOTHING
        ''', (car_tag, customer_name, phone_number, date_taken))
        self.conn.commit()

    def mark_as_cleaned(self, car_tag):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE cleaning_records SET cleaned = 1 WHERE car_tag = ?', (car_tag,))
        self.conn.commit()

    def schedule_weekly_cleaning(self, car_tag, customer_name, phone_number, start_date):
        current_date = datetime.now()
        start_date = datetime.strptime(start_date, "%Y-%m-%d")

        while start_date <= current_date:
            self.add_cleaning_record(car_tag, customer_name, phone_number, start_date.strftime("%Y-%m-%d %H:%M:%S"))
            start_date += timedelta(days=7)

    def schedule_monthly_cleaning(self, car_tag, customer_name, phone_number, start_date):
        current_date = datetime.now()
        start_date = datetime.strptime(start_date, "%Y-%m-%d")

        while start_date <= current_date:
            self.add_cleaning_record(car_tag, customer_name, phone_number, start_date.strftime("%Y-%m-%d %H:%M:%S"))
            start_date += timedelta(days=30)

    def display_records(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM cleaning_records')
        records = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ["Car Tag", "Customer Name", "Phone Number", "Date Taken", "Cleaned"]

        for record in records:
            table.add_row(record)

        print(table)

if __name__ == "__main__":
    cleaner = Clean()

    while True:
        print("\n1. Add Cleaning Record")
        print("2. Mark as Cleaned")
        print("3. Schedule Weekly Cleaning")
        print("4. Schedule Monthly Cleaning")
        print("5. Display Cleaning Records")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            car_tag = input("Enter car tag: ")
            customer_name = input("Enter customer name: ")
            phone_number = input("Enter phone number: ")
            date_taken = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cleaner.add_cleaning_record(car_tag, customer_name, phone_number, date_taken)
            print("Cleaning record added successfully.")

        elif choice == '2':
            cleaner.display_records()
            car_tag = input("Enter the car tag of the record to mark as cleaned: ")
            cleaner.mark_as_cleaned(car_tag)
            print("Record marked as cleaned.")

        elif choice == '3':
            car_tag = input("Enter car tag: ")
            customer_name = input("Enter customer name: ")
            phone_number = input("Enter phone number: ")
            start_date = input("Enter the start date for weekly cleaning (YYYY-MM-DD): ")
            cleaner.schedule_weekly_cleaning(car_tag, customer_name, phone_number, start_date)
            print("Weekly cleaning scheduled successfully.")

        elif choice == '4':
            car_tag = input("Enter car tag: ")
            customer_name = input("Enter customer name: ")
            phone_number = input("Enter phone number: ")
            start_date = input("Enter the start date for monthly cleaning (YYYY-MM-DD): ")
            cleaner.schedule_monthly_cleaning(car_tag, customer_name, phone_number, start_date)
            print("Monthly cleaning scheduled successfully.")

        elif choice == '5':
            cleaner.display_records()

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")
