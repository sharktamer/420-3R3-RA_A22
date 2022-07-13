# Cette classe est responsable de faire toutes les requêtes à la table Client de la base de données
class TableClient:

    sql_obtenir_liste_client = """SELECT * FROM Client"""
    sql_obtenir_client_par_id = """SELECT * FROM Client WHERE id=%s"""
    sql_ajouter_client = """INSERT INTO Client (prenom, nom) VALUES (%s, %s)"""
    sql_supprimer_client = """DELETE FROM Client WHERE id=%s"""

    def __init__(self, connexion):
        self.connexion=connexion

    def RequeteToutClient(self):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_liste_client)
            tuples = curseur.fetchall()
            curseur.close()
            return tuples
        except (Exception)as error:
            print(error)

    def RequeteUnClient(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_client_par_id, [str(id)])
            tuple = curseur.fetchone()
            curseur.close()
            return tuple
        except (Exception)as error:
            print(error)

    def RequeteAjouterClient(self, prenom, nom):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_ajouter_client,[prenom, nom])
            curseur.close()
        except (Exception)as error:
            print(error)

    def RequeteSupprimerClient(self, id):
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_supprimer_client, [str(id)])
            curseur.close()
        except (Exception)as error:
            print(error)
