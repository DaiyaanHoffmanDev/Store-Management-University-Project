import sqlite3
from datetime import datetime

class personmanger():
    def insert_person(self, *args):
        pass
    def remove_person(self, person_id):
        pass
    def display_all(self):
        pass

class employeemanger(personmanger):
    def insert_person(self, n, s, c, e):
        db = sqlite3.connect('londonroots.db')
        cursor = db.cursor()
        cursor.execute("insert into employee (name, surname, cell, email) values (?, ?, ?, ?)", (n, s, c, e))
        db.commit()
        db.close()

    def remove_person(self, emp_id):
        db = sqlite3.connect('londonroots.db')
        cursor = db.cursor()
        cursor.execute("delete from employee where employee_id = ?", (emp_id,))
        db.commit()
        db.close()

    def display_all(self):
        db = sqlite3.connect('londonroots.db')
        cursor = db.cursor()
        cursor.execute("select * from employee")
        for r in cursor.fetchall():
            print(r)
        db.close()

class customermanger(personmanger):
    def insert_person(self, n, s, c, e, ad):
        db = sqlite3.connect('londonroots.db')
        cursor = db.cursor()
        cursor.execute("insert into customer (name, surname, cell, email, billing_address) values (?, ?, ?, ?, ?)", (n, s, c, e, ad))
        db.commit()
        db.close()

    def remove_person(self, cust_id):
        db = sqlite3.connect('londonroots.db')
        cursor = db.cursor()
        cursor.execute("delete from customer where customer_id = ?", (cust_id,))
        db.commit()
        db.close()

    def display_all(self):
        db = sqlite3.connect('londonroots.db')
        cursor = db.cursor()
        cursor.execute("select * from customer")
        for x in cursor.fetchall():
            print(x)
        db.close()

class Store:
    @staticmethod
    def add_product(n, p, q):
        conn = sqlite3.connect('londonroots.db')
        cursor = conn.cursor()
        cursor.execute("insert into product (name, price, quantity) values (?, ?, ?)", (n, p, q))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_product(p_id):
        conn = sqlite3.connect('londonroots.db')
        cursor = conn.cursor()
        cursor.execute("delete from product where product_id = ?", (p_id,))
        conn.commit()
        conn.close()

    @staticmethod
    def update_product(p_id, p, q):
        conn = sqlite3.connect('londonroots.db')
        cursor = conn.cursor()
        cursor.execute("update product set price = ?, quantity = ? where product_id = ?", (p, q, p_id))
        conn.commit()
        conn.close()

    @staticmethod
    def display_products():
        conn = sqlite3.connect('londonroots.db')
        cursor = conn.cursor()
        cursor.execute("select * from product")
        for p in cursor.fetchall():
            print(p)
        conn.close()

    @staticmethod
    def sell_product(p_id, amount):
        conn = sqlite3.connect('londonroots.db')
        cursor = conn.cursor()
        cursor.execute("select * from product where product_id = ?", (p_id,))
        row = cursor.fetchone()
        
        if row:
            current_stock = row[3]
            if current_stock >= amount and amount > 0:
                new_qty = current_stock - amount
                total = row[2] * amount
                date = datetime.now().strftime("%y-%m-%d %h:%m:%s")
                
                cursor.execute("update product set quantity = ? where product_id = ?", (new_qty, p_id))
                cursor.execute("insert into sales (sale_date, product_name, quantity_sold, sale_total) values (?, ?, ?, ?)", 
                               (date, row[1], amount, total))
                conn.commit()
                print(f"success: sold {amount} of {row[1]}. total: r{total}")
            else:
                print("error: invalid quantity or insufficient stock.")
        else:
            print("error: product id not found.")
        conn.close()

    @staticmethod
    def display_sales():
        conn = sqlite3.connect('londonroots.db')
        cursor = conn.cursor()
        cursor.execute("select * from sales")
        for s in cursor.fetchall():
            print(s)
        conn.close()

e_mgr = employeemanger()
c_mgr = customermanger()

while True:
    print("london roots store system")
    print("1. employees\n2. customers\n3. store/inventory\n4. exit")
    choice = input("select menu: ")

    if choice == "1":
        print("1. add, 2. remove, 3. display")
        s = input("select: ")
        if s == "1": e_mgr.insert_person(input("name: "), input("surname: "), input("cell: "), input("email: "))
        elif s == "2": e_mgr.remove_person(input("employee id: "))
        elif s == "3": e_mgr.display_all()

    elif choice == "2":
        print("1. add, 2. remove, 3. display")
        s = input("select: ")
        if s == "1": c_mgr.insert_person(input("name: "), input("surname: "), input("cell: "), input("email: "), input("address: "))
        elif s == "2": c_mgr.remove_person(input("customer id: "))
        elif s == "3": c_mgr.display_all()

    elif choice == "3":
        print("1. add product, 2. remove, 3. update, 4. display, 5. sell, 6. sales report")
        s = input("select: ")
        if s == "1": Store.add_product(input("name: "), float(input("price: ")), int(input("qty: ")))
        elif s == "2": Store.remove_product(input("product id: "))
        elif s == "3": Store.update_product(input("id: "), float(input("new price: ")), int(input("new qty: ")))
        elif s == "4": Store.display_products()
        elif s == "5": 
            try:
                Store.sell_product(input("product id: "), int(input("qty: ")))
            except:
                print("error: please enter numbers only.")
        elif s == "6": Store.display_sales()

    elif choice == "4":
        print("system closed.")
        break