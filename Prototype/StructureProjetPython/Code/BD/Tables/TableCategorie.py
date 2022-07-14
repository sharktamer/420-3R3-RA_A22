class TableCategorie:

    def __init__(self, connexion):
        self.connexion=connexion

    sql_obtenir_liste_categorie = """SELECT * FROM Categorie"""
    sql_obtenir_categorie_par_id = """SELECT * FROM Categorie WHERE id=%s"""
    sql_ajouter_categorie = """INSERT INTO 
                        Categorie (id, nom) 
                        VALUES (%s, %s)"""
    sql_supprimer_categorie = """DELETE FROM Categorie WHERE id=%s"""

    def RequeteToutCategorie(self):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_liste_categorie)
            tuples = curseur.fetchall()
            curseur.close()
            return tuples
        except (Exception)as error:
            print(error)

    def RequeteUnCategorie(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_categorie_par_id, [id])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple
        except (Exception)as error:
            print(error)

    def RequeteAjouterCategorie(self, id, nom):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_ajouter_categorie, [id, nom])
            curseur.close()
        except (Exception)as error:
            print(error)

    def RequeteSupprimerCategorie(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_supprimer_categorie, [id])
            curseur.close()
        except (Exception)as error:
            print(error)