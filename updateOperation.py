import sqlite3

def approve_user(userID, isApproved):
    conn = sqlite3.connect('my_medicalShop.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE Users SET isApproved = ? WHERE userId = ?", (isApproved, userID))
    
    conn.commit()
    conn.close()
