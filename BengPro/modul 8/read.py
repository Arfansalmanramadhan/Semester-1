import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor = db.cursor()
sql = "SELECT * FROM customers"
cursor.execute(sql)
baca = cursor.fetchall()
for data in baca:
    print(data)
