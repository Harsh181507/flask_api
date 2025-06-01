import sqlite3



def authenticate_user(email, password):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE email = ? AND password =?", (email, password))
    user = cursor.fetchone()
    conn.close()

    return user