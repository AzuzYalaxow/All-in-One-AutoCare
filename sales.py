import sqlite3
from prettytable import PrettyTable

class CarSales:
    def __init__(self, db_name="aioa.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS carsales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            year INTEGER NOT NULL,
            color TEXT NOT NULL,
            mileage REAL NOT NULL,
            power INTEGER NOT NULL,
            transmission TEXT NOT NULL,
            fuel TEXT NOT NULL,
            price REAL NOT NULL
        );
        '''
        self.conn.execute(query)
        self.conn.commit()

    def add_car(self, car_data):
        query = '''
        INSERT INTO carsales (name, year, color, mileage, power, transmission, fuel, price)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        '''
        self.conn.execute(query, car_data)
        self.conn.commit()

    def sell_car(self, car_id):
        query = '''
        DELETE FROM carsales WHERE id = ?;
        '''
        self.conn.execute(query, (car_id,))
        self.conn.commit()

    def update_car(self, car_id, car_data):
        query = '''
        UPDATE carsales
        SET name=?, year=?, color=?, mileage=?, power=?, transmission=?, fuel=?, price=?
        WHERE id=?;
        '''
        self.conn.execute(query, (*car_data, car_id))
        self.conn.commit()

    def display_inventory(self):
        query = '''
        SELECT * FROM carsales;
        '''
        result = self.conn.execute(query)
        table = PrettyTable()
        table.field_names = ["ID", "Name", "Year", "Color", "Mileage", "Power", "Transmission", "Fuel", "Price"]
        table.add_rows(result)
        print(table)

# Function to get car information from the user
def get_car_info():
    name = input("Enter car name: ")
    year = int(input("Enter car year: "))
    color = input("Enter car color: ")
    mileage = float(input("Enter car mileage: "))
    power = int(input("Enter car power: "))
    transmission = input("Enter car transmission: ")
    fuel = input("Enter car fuel type: ")
    price = float(input("Enter car price: ").replace(',',''))
    return name, year, color, mileage, power, transmission, fuel, price

car_sales = CarSales()

def main_sale():
    while True:
        print("\n1. Add Car\n2. Sell Car\n3. Update Car\n4. Display Inventory\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            car_info = get_car_info()
            car_sales.add_car(car_info)
            print("Car added to inventory.")

        elif choice == "2":
            car_sales.display_inventory()
            car_id = int(input("Enter the ID of the car to sell: "))
            car_sales.sell_car(car_id)
            print("Car sold and removed from inventory.")

        elif choice == "3":
            car_id = int(input("Enter the ID of the car to update: "))
            car_info = get_car_info()
            car_sales.update_car(car_id, car_info)
            print("Car information updated.")

        elif choice == "4":
            print("\nInventory:")
            car_sales.display_inventory()

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
