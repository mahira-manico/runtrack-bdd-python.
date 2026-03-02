--request to add a student from the table etudiant
INSERT INTO etudiant
    -> (nom,prenom,age,email)
    -> VALUES ("Dupuis","Martin","18","martin.dupuis@laplateforme.io");

 select * from etudiant
    -> ORDER BY nom;