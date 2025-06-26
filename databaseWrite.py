import mysql.connector


myDbHandle = mysql.connector.connect(
        host="localhost",
        user="piuser",
        password="pipassword",
        database="shedlog")

myCursor = myDbHandle.cursor()

sql = "select * from shedData"

myCursor.execute(sql)

val = myCursor.fetchall()

print(val)
