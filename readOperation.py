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
    user = cursor.fetchone()
    conn.close()


    return user


   