import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="",database="company") #connector object creation
cur=db.cursor()
cur.execute("insert into sample(name)values('fahi');")
db.commit() #connector object.commit
db.close()

            
            
