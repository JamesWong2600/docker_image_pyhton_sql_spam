import mysql.connector
from mysql.connector import Error


#192.168.0.252
x = 0
count = 0
while x < 10:
    conn = mysql.connector.connect(
    host="192.168.0.88",
    user="james",
    password="",
    database="test"
    )
    cursor = conn.cursor()
    cursor.execute("UPDATE datafile SET point = point + 1")
    count += 1
    print("count:", count)
    conn.commit()
    conn.close()