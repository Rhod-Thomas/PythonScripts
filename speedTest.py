import speedtest
from datetime import datetime
import mysql.connector

#get timestamp
timeNow = datetime.now()

#run speedtests
s =  speedtest.Speedtest()
down = s.download()
up = s.upload()

#write to database
db = mysql.connector.connect(
        host='localhost',
        user='piuser',
        password='pipassword',
        database='HouseLog'
        )

cursor = db.cursor()
time = datetime.now()


sql = ("insert into netwoekSpeed (time, down, up) values (%s, %s, %s)")
vals = (time, down, up)

cursor.execute(sql, vals)
db.commit()

cursor.close()
db.close()


