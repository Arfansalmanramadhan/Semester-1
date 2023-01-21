import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor = db.cursor()
sql = "UPDATE customers SET name=%s, address=%s WHERE customer_id=%s "
val = ("Azzam", "Jakarta", 1)
cursor.execute(sql, val)

db.commit()
print("{} data ditambahkan", format(cursor.rowcount))
