import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="toko_mainan"
)

cursor = db.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
values = [
    ("ARFAN", "BANDUNG"),
    ("Salman", "Bandung"),
    ("Ramadhan", "Basdung")]
for val in values:
    cursor.execute(sql, val)
    db.commit()
print("{} data ditambahkan", format(len(values)))
