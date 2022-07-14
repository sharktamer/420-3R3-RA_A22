class TableVente:

    sql_obtenir_liste_vente = """SELECT * FROM Vente"""
    sql_obtenir_vente_par_id = """SELECT * FROM Vente WHERE id=%s"""
    sql_ajouter_vente = """INSERT INTO Vente (id_client, id_item, quantite) VALUES (%s, %s, %s) RETURNING id"""
    sql_supprimer_vente = """DELETE FROM Vente WHERE id=%s"""

    def __init__(self, connexion):
        self.connexion=connexion

    def RequeteToutVente(self):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_liste_vente)
            tuples = curseur.fetchall()
            curseur.close()
            return tuples
        except (Exception)as error:
            print(error)

    def RequeteUnVente(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_vente_par_id, [id])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple
        except (Exception)as error:
            print(error)

    def RequeteAjouterVente(self, id_client, id_item, quantite):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_ajouter_vente,[id_client, id_item, quantite])
            id = curseur.fetchone()
            curseur.close()
            return id[0]
        except (Exception)as error:
            print(error)

    def RequeteSupprimerVente(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_supprimer_vente, [id])
            curseur.close()
        except (Exception)as error:
            print(error)
