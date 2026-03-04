import mysql.connector

class Zoo:
    def __init__(self):

     self.mydb=mysql.connector.connect(
      host="localhost",
      user="root",
      password="Banane1001#",
      database="zoo",
     )

     self.cursor=self.mydb.cursor()

    def read(self):
       self.cursor.execute("SELECT * FROM animal")
       for x in self.cursor:
          print(x)
    
    def read_cage(self):
       self.cursor.execute("SELECT cage.id,cage.superficie,animal.name FROM cage INNER JOIN animal on cage.id=animal.cage_id")
       for x in self.cursor:
          print(x)
          
    def add_animal(self, name, race, cage_id,birthdate,country):
      request="INSERT INTO animal (name,race,cage_id,birthdate,country) VALUES (%s,%s,%s,%s,%s)"
      value=(name,race,cage_id,birthdate,country)
      self.cursor.execute(request,value)
      self.mydb.commit()
      print(f"{name} succesfully added to database!")

    def add_cage(self, superficie, max_capacity):
      request="INSERT INTO cage (superficie,max_capacity) VALUES (%s,%s)"
      value=(superficie, max_capacity)
      self.cursor.execute(request,value)
      self.mydb.commit()
      print(f"New cage succesfully added to database!")
    
    def delete_animal(self, id):
       request="DELETE FROM animal WHERE id=%s"
       value=(id,)
       self.cursor.execute(request,value)
       self.mydb.commit()
       print(f"{id} Succesfully deleted!")

    def delete_cage(self, id):
       request="DELETE FROM cage WHERE id=%s"
       value=(id,)
       self.cursor.execute(request,value)
       self.mydb.commit()
       print(f"{id} Succesfully deleted!")
    
    def modify_animal(self,column, id,new_value):
       request=f"UPDATE animal SET {column}=%s WHERE id=%s"
       value=(id,new_value)
       self.cursor.execute(request,value)
       self.mydb.commit()
       print(f"{new_value} succesfully added!")
    
    def modify_cage(self,column, id, new_value):
       request=f"UPDATE cage SET {column}=%s WHERE id=%s"
       value=(id,new_value)
       self.cursor.execute(request,value)
       self.mydb.commit()
       print(f"Cage succesfully modified!")
    
    def calculate(self):
       request="SELECT SUM(superficie) FROM cage"
       self.cursor.execute(request)
       result=self.cursor.fetchone()
       print(f"The total superficie is {result[0]} m2")

mon_zoo=Zoo()
mon_zoo.add_cage(500, 10) 
mon_zoo.add_animal("Simba", "Lion", 1, "2023-01-01", "Kenya") 
mon_zoo.read_cage() 
mon_zoo.calculate() 