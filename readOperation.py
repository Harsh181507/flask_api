import sqlite3



def authenticate_user(email, password):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE email = ? AND password =?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user






def getAllUsers():
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    conn.close()

    userJson=[]
    for user in users:
        tempUser ={
            "id" :user[0],
            "user_id": user[1],
            "password": user[2],
            "date_of_account_creation": user[3],
            "isApproved": user[4],
            "block": user[5],
            "name": user[6],
            "address": user[7],
            "email": user[8],
            "phone_number": user[9],
            "pin_code": user[10]
        }
        userJson.append(tempUser)

    return userJson


def getSpecificUser(userId):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE user_id = ?", (userId,))
    users = cursor.fetchone()
    conn.close()

    userJson ={
            "id" :users[0],
            "user_id": users[1],
            "password": users[2],
            "date_of_account_creation": users[3],
            "isApproved": users[4],
            "block": users[5],
            "name": users[6],
            "address": users[7],
            "email": users[8],
            "phone_number": users[9],
            "pin_code": users[10]
        }


    return userJson


def get_all_products():
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    conn.close()

    productJson=[]
    for product in products:
        tempProduct ={
            "id" :product[0],
            "products_id": product[1],
            "name": product[2],
            "price": product[3],
            "category": product[4],
            "stock": product[5]
        }
        productJson.append(tempProduct)

    return productJson

def get_specific_product(productId):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM Products WHERE products_id = ?", (productId,))
    product = cursor.fetchone()
    conn.close()

    productJson ={
            "id" :product[0],
            "products_id": product[1],
            "name": product[2],
            "price": product[3],
            "category": product[4],
            "stock": product[5]
        }

    return productJson


def get_all_orders_detail():
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Order_Details")
    orders = cursor.fetchall()
    conn.close()

    orderJson=[]
    for order in orders:
        tempOrder ={
            "id" :order[0],
            "order_id": order[1],
            "user_id": order[2],
            "product_id": order[3],
            "isApproved": order[4],
            "quantity": order[5],
            "date_of_order_creation": order[6],
            "price": order[7],
            "total_amount": order[8],
            "product_name": order[9],
            "user_name": order[10],
            "message": order[11],
            "category": order[12]
        }
        orderJson.append(tempOrder)

    return orderJson