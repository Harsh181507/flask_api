import sqlite3

def createTables():
    conn=sqlite3.connect("my_medicalShop.db")
    cursor=conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                phone_number VARCHAR(255) NOT NULL,
                address VARCHAR(255) NOT NULL,
                pin_code VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                created_at DATE,
                isApproved BOOLEAN ,
                block BOOLEAN
                );
                   
    ''')
    conn.commit()
    conn.close()