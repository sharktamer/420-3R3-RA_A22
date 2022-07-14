class TableArbre:

    def __init__(self, connexion):
        self.connexion=connexion

    sql_obtenir_liste_arbre = """SELECT * FROM Arbre"""
    sql_obtenir_arbre_par_id = """SELECT * FROM Arbre WHERE id=%s"""
    sql_ajouter_arbre = """INSERT INTO 
                        Arbre (id_item, hauteur) 
                        VALUES (%s, %s)"""
    sql_supprimer_arbre = """DELETE FROM Arbre WHERE id=%s"""

    def RequeteToutArbre(self):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_liste_arbre)
            tuples = curseur.fetchall()
            curseur.close()
            return tuples
        except (Exception)as error:
            print(error)

    def RequeteUnArbre(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_arbre_par_id, [id])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple
        except (Exception)as error:
            print(error)

    def RequeteAjouterArbre(self, id_item, hauteur):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_ajouter_arbre, [id_item, hauteur])
            curseur.close()
        except (Exception)as error:
            print(error)

    def RequeteSupprimerArbre(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_supprimer_arbre, [id])
            curseur.close()
        except (Exception)as error:
            print(error)