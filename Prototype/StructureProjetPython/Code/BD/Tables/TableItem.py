class TableItem:

    def __init__(self, connexion):
        self.connexion=connexion

    sql_obtenir_liste_item = """SELECT * FROM Item"""
    sql_obtenir_item_par_id = """SELECT * FROM Item WHERE id=%s"""
    sql_ajouter_item = """INSERT INTO 
                        Item (id_categorie, nom, description, prix, quantite) 
                        VALUES (%s, %s, %s, %s, %s)"""
    sql_supprimer_item = """DELETE FROM Item WHERE id=%s"""

    def RequeteToutItem(self):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_liste_item)
            tuples = curseur.fetchall()
            curseur.close()
            return tuples
        except (Exception)as error:
            print(error)

    def RequeteUnItem(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_item_par_id, [id])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple
        except (Exception)as error:
            print(error)

    def RequeteAjouterItem(self, id_categorie, nom, description, prix, quantite):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_ajouter_item,
                [id_categorie, 
                nom, 
                description, 
                prix, 
                quantite])
            curseur.close()
        except (Exception)as error:
            print(error)

    def RequeteSupprimerItem(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_supprimer_item, [id])
            curseur.close()
        except (Exception)as error:
            print(error)
