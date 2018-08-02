import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="",database="company") #connector object creation
cur=db.cursor()
cur.execute("select * from sample;")
row=cur.fetchall()
for rows in row:
    print(rows[0],rows[1])
db.close()

            
            
