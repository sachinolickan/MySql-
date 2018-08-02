import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="",database="company") #connector object creation
cur=db.cursor()
cur.execute("create table field(id int auto_increment,primary key(id),name text);")
db.commit() #connector object.commit
db.close()

            
            
