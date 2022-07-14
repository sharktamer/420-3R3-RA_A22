class TableRoche:

    def __init__(self, connexion):
        self.connexion=connexion

    sql_obtenir_liste_roche = """SELECT * FROM Roche"""
    sql_obtenir_roche_par_id = """SELECT * FROM Roche WHERE id=%s"""
    sql_obtenir_poids_roche_par_id = """SELECT poids FROM Roche WHERE id_item=%s"""
    sql_obtenir_couleur_roche_par_id = """SELECT couleur FROM Roche WHERE id_item=%s"""
    sql_ajouter_roche = """INSERT INTO Roche (id_item, poids, couleur) VALUES (%s, %s, %s)"""
    sql_supprimer_roche = """DELETE FROM Roche WHERE id_item=%s"""

    def RequeteToutRoche(self):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_liste_roche)
            tuples = curseur.fetchall()
            curseur.close()
            return tuples
        except (Exception)as error:
            print(error)

    def RequeteUnRoche(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_roche_par_id, [id])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple
        except (Exception)as error:
            print(error)

    def RequetePoidsRoche(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_poids_roche_par_id, [id])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple[0]
        except (Exception)as error:
            print(error)

    def RequeteCouleurRoche(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_couleur_roche_par_id, [id])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple[0]
        except (Exception)as error:
            print(error)

    def RequeteAjouterRoche(self, id_item, poids, couleur):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_ajouter_roche, [id_item, poids, couleur])
            curseur.close()
        except (Exception)as error:
            print(error)

    def RequeteSupprimerRoche(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_supprimer_roche, [id])
            curseur.close()
        except (Exception)as error:
            print(error)