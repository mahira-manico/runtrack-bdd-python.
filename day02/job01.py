import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Banane1001#",
    database="LaPlateforme",
)



cursor=mydb.cursor()

cursor.execute("TRUNCATE TABLE etage") 
mydb.commit()

request="""
INSERT INTO etage (nom,numero,superficie)
VALUES ("RDC", 0, 500)
"""
mydb.commit()

cursor.execute(request)
cursor.execute("SELECT * FROM etage")
for x in cursor:
    print(x)

request2="""INSERT INTO etage (nom,numero,superficie)
VALUES ("R+1",1,500)
"""

cursor.execute(request2)
mydb.commit()
cursor.execute("SELECT * FROM etage")
for x in cursor:
    print(x)

request3="""INSERT INTO salle (nom,id_etage,capcite)
VALUES ("Lounge",1,100),
("Studio Son",1,5),
("Broadcasting",2,50),
("Bocal Peda",2,4),
("Coworking",2,80),
("Studio Video",2,5)
"""

cursor.execute("TRUNCATE TABLE salle") 
cursor.execute(request3)
mydb.commit()
cursor.execute("SELECT * FROM salle")
for x in cursor:
    print(x)

cursor.execute("SELECT nom,capcite FROM salle")
for x in cursor:
    print(x)