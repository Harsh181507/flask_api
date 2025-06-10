import sqlite3
import uuid
from datetime import date, datetime


def create_User(
        name,password,address, email, phone_number,pincode):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    dateOfCreation =date.today()
    user_id=str(uuid.uuid4())

    cursor.execute('''
    INSERT INTO Users (
                   name, password, date_of_account_creation,isApproved, block, address, email, pin_code,phone_number,user_id)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''',(name, password, dateOfCreation,0,0, address,email, pincode, phone_number, user_id)
)
    conn.commit()
    conn.close()
    return user_id

def add_product(
        name, price, category, stock):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    product_id = str(uuid.uuid4())

    cursor.execute('''
    INSERT INTO Products (
                   name, price, category, stock, products_id)
                   VALUES (?, ?, ?, ?, ?)
''', (name, price, category, stock, product_id))
    
    conn.commit()
    conn.close()
    return product_id

def order_details(
        user_id, product_id, quantity, price, total_amount, product_name, user_name, category, message):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()

    order_id = str(uuid.uuid4())
    date_of_order_creation = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
    INSERT INTO Order_Details (
                   order_id, user_id, product_id, isApproved, quantity, date_of_order_creation, price, total_amount, product_name, user_name, message, category)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (order_id, user_id, product_id, 0, quantity, date_of_order_creation, price, total_amount, product_name, user_name, message, category))