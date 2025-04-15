import sqlite3
import uuid
from datetime import date

def createUser(
        name,password,phone_number,address,pincode,
        email
):
    conn=sqlite3.connect("my_medicalShop.db")
    cursor=conn.cursor()

    dateofCreation=date.today()
    user_id=str(uuid.uuid4())
    cursor.execute(''' 
        INSERT INTO Users(
user_id, password, name, phone_number, address, pin_code, email, created_at, isApproved, block
)
                   VALUES(?,?,?,?,?,?,?,?,?,?)
                   ''',(name,password,phone_number,address,pincode,email,dateofCreation,0,0,user_id)
                   )
    conn.commit()
    conn.close()
    return user_id

