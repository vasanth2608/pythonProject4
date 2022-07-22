import mysql.connector

conn = mysql.connector.connect(host='localhost',database='apidevelop',user='root',password='vasanth')
cursor=conn.cursor()
print(conn.is_connected())

mysql='select * from customerinfo'
cursor.execute(mysql)

rows = cursor.fetchall()
print(type(rows))
print(rows)