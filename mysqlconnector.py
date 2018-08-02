import mysql.connector
db = mysql.connector.connect(host="localhost",user="root",password="",database="Company")#connector object creation
cur=db.cursor()
cur.execute("create table datafield(id int auto_increment,primary key(id),name text)")
db.commit() #connector object.commit
db.close()

            
            
