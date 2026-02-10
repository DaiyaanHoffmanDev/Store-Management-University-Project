import sqlite3
from abc import ABC, abstractmethod

class PersonManger(ABC):
    @abstractmethod
    def insert_person():
        pass

    @abstractmethod
    def remove_person():
        pass

    @abstractmethod
    def display_all():
        pass

class EmployeeManger(PersonManger):
    @staticmethod
    def insert_person(name, surname, cell, email):
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists employee (name TEXT, surname TEXT, cell TEXT, email TEXT)")
        cursor.execute("insert into employee (name, surname, cell, email) values (?, ?, ?, ?)", (name, surname, cell, email))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_person(name, surname, cell, email):
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("delete from employee where name = ? and surname = ? and cell = ? and email = ?", (name, surname, cell, email))
        conn.commit()
        conn.close()

    @staticmethod
    def display_all():
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists employee (name TEXT, surname TEXT, cell TEXT, email TEXT)")
        cursor.execute("select * from employee")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

class CustomerManger(PersonManger):
    @staticmethod
    def insert_person(name, surname, cell, email, billing_address):
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists customer (name TEXT, surname TEXT, cell TEXT, email TEXT, billing_address TEXT)")
        cursor.execute("insert into customer (name, surname, cell, email, billing_address) values (?, ?, ?, ?, ?)", (name, surname, cell, email, billing_address))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_person(name, surname, cell, email, billing_address):
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("delete from customer where name = ? and surname = ? and cell = ? and email = ? and billing_address = ?", (name, surname, cell, email, billing_address))
        conn.commit()
        conn.close()

    @staticmethod
    def display_all():
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists customer (name TEXT, surname TEXT, cell TEXT, email TEXT, billing_address TEXT)")
        cursor.execute("select * from customer")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

class Store:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists store (name TEXT, price TEXT, quantity INTEGER)")
        cursor.execute("insert into store (name, price, quantity) values (?, ?, ?)", (name, price, quantity))
        conn.commit()
        conn.close()
    
    @staticmethod
    def sellProduct():
        user_input = input("Enter the name of the product you want to sell: ")
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists store (name TEXT, price TEXT, quantity INTEGER)")
        cursor.execute("select * from store where name = ?", (user_input,))
        row = cursor.fetchone()
        if row:
            product_quantity = row[2]
            print(f"product quantity: {product_quantity}")
            if product_quantity > 0:
                product_quantity = product_quantity - 1
                cursor.execute("update store set quantity = ? where name = ?", (product_quantity, user_input))
                conn.commit()
                print("Product sold successfully.")
            else:
                print("Product is out of stock.")
        if row is None:
            print("product not found")
        conn.close()

    @staticmethod
    def display_all():
        conn = sqlite3.connect('LondonRoots.db')
        cursor = conn.cursor()
        cursor.execute("create table if not exists store (name TEXT, price TEXT, quantity INTEGER)")
        cursor.execute("select * from store")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()

while True:
    print(f"\nWelcome to the store management system \n 1 = employees \n 2 = customers \n 3 = store \n 4 = exit")
    user_input = input("Enter a num from 1 to 4 to make a selection:")
    
    if user_input == "1":
        print("1 = insert employee \n 2 = remove employee \n 3 = display all employees")
        add_employee = input("selection: ")
        if add_employee == "1":
            EmployeeManger.insert_person(input("Name: "), input("Surname: "), input("Cell: "), input("Email: "))
        elif add_employee == "2":
            EmployeeManger.remove_person(input("Name: "), input("Surname: "), input("Cell: "), input("Email: "))
        elif add_employee == "3":
            EmployeeManger.display_all()
                
    elif user_input == "2":
        print("1 = insert customer \n 2 = remove customer \n 3 = display all customers")
        add_customer = input("selection: ")
        if add_customer == "1":
            CustomerManger.insert_person(input("Name: "), input("Surname: "), input("Cell: "), input("Email: "), input("Address: "))
        elif add_customer == "2":
            CustomerManger.remove_person(input("Name: "), input("Surname: "), input("Cell: "), input("Email: "), input("Address: "))
        elif add_customer == "3":
            CustomerManger.display_all()

    elif user_input == "3":
        print("1 = add product \n 2 = sell product \n 3 = display all products")
        add_product = input("selection: ")
        if add_product == "1":
            Store(input("Name: "), input("Price: "), int(input("Qty: ")))
        elif add_product == "2":
            Store.sellProduct()
        elif add_product == "3":
            Store.display_all()

    elif user_input == "4":
        print("fisnished")
        break