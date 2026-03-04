import mysql.connector

class Employe:
    def __init__(self):

     self.mydb=mysql.connector.connect(
      host="localhost",
      user="root",
      password="Banane1001#",
      database="employee",
     )

     self.cursor=self.mydb.cursor()

    def read(self):
     self.cursor.execute("SELECT * FROM employe")
     for x in self.cursor:
       print(x)

    def create(self,nom,prenom,salaire,id_service):
      new_employe="INSERT INTO employe (nom,prenom,salaire,id_service) VALUES (%s,%s,%s,%s)"
      values=(nom,prenom,salaire,id_service)
      self.cursor.execute(new_employe,values)
      self.mydb.commit()
      print(f"{nom} added succesfully!")

    def update(self,id_employe, new_name):
      request="UPDATE employe SET nom=%s WHERE id=%s"
      value=new_name,id_employe
      self.cursor.execute(request,value)
      self.mydb.commit()
      print(f"{id_employe} updated at {new_name}!")

    def delete(self, id):
      request="DELETE FROM employe WHERE id=%s"
      value=(id,)
      self.cursor.execute(request,value)
      self.mydb.commit()
      print(f"{id} deleted succesfully!")


gestion=Employe()
gestion.read()


      


