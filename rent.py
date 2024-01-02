import sqlite3
from prettytable import PrettyTable

class CarRent:
    def __init__(self, db_name="aioa.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()
        self.create_tableback()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS carrents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            color TEXT NOT NULL,
            mileage REAL NOT NULL,
            transmission TEXT NOT NULL,
            fuel TEXT NOT NULL,
            price REAL NOT NULL,
            damage TEXT NOT NULL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def create_tableback(self):
        query = '''
        CREATE TABLE IF NOT EXISTS carrentsBacks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            holder TEXT NOT NULL,
            duration INTEGER NOT NULL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_car(self, car_data):
        query = '''
        INSERT INTO carrents (name, year, color, mileage, transmission, fuel, price, damage)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        '''
        self.conn.execute(query, car_data)
        self.conn.commit()

    def rent_car(self, car_id):
        query = '''
        DELETE FROM carrents WHERE id = ?;
        '''
        self.conn.execute(query, (car_id,))
        self.conn.commit()

    def rent_car_back(self, car_id, Renter_name, days):
        query = '''
        INSERT INTO carrentsBacks (name, holder, duration)
        VALUES (?, ?, ?);
        '''
        self.conn.execute(query, (car_id, Renter_name, days))
        self.conn.commit()

    def update_car(self, car_id, car_data):
        query = '''
        UPDATE carrents
        SET name=?, year=?, color=?, mileage=?, transmission=?, fuel=?, price=?, damage=?
        WHERE id=?;
        '''
        self.conn.execute(query, (*car_data, car_id))
        self.conn.commit()

    def display_inventory(self):
        query = '''
        SELECT * FROM carrents;
        '''
        result = self.conn.execute(query).fetchall()
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Year", "Color", "Mileage", "Transmission", "Fuel", "Price", "Damage"]
        for row in result:
            table.add_row(row)
        print(table)
        
    def display_inventoryback(self):
        query = '''
        SELECT id, name, duration FROM carrentsBacks;
        '''
        result = self.conn.execute(query).fetchall()
        table = PrettyTable()
        table.field_names = ["ID", "Renter", "Days"]
        for row in result:
            table.add_row(row)
        print(table)

# Function to get car information from the user
def get_car_info():
    name = input("Enter car name: ")
    year = int(input("Enter car year: "))
    color = input("Enter car color: ")
    mileage = float(input("Enter car mileage: "))
    transmission = input("Enter car transmission: ")
    fuel = input("Enter car fuel type: ")
    price = float(input("Enter car price per day: ").replace(',', ''))
    damage = input("Enter car damage status: ")
    return name, year, color, mileage, transmission, fuel, price, damage

# Example Usage with user input
if __name__ == "__main__":
    car_rent = CarRent()
    while True:
        print("\n1. Add Car\n2. Rent Car\n3. Update Car\n4. Display Inventory\n5. Display rented\n6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            car_info = get_car_info()
            car_rent.add_car(car_info)
            print("Car added to inventory.")

        elif choice == "2":
            car_rent.display_inventory()
            car_id = int(input("Enter the ID of the car to rent: "))
            Renter_name = input("Enter the name of the renter: ")
            days = int(input("Enter number of days the car is rented for: "))
            car_rent.rent_car_back(car_id ,Renter_name, days)
            car_rent.rent_car(car_id)
            print(f"Car successfully rented to {Renter_name}.")

        elif choice == "3":
            car_id = int(input("Enter the ID of the car to update: "))
            car_info = get_car_info()
            car_rent.update_car(car_id, car_info)
            print("Car information updated.")

        elif choice == "4":
            print("\nInventory:")
            car_rent.display_inventory()

        elif choice == "5":
            print("\nRented:")
            car_rent.display_inventoryback()

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
