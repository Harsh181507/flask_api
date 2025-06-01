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