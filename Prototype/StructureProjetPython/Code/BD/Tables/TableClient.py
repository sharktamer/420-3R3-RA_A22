from ..Tuples.TupleClient import TupleClient

# Cette classe est responsable de faire toutes les requêtes à la table Client de la base de données
class TableClient:

    sql_obtenir_liste_client = """SELECT * FROM Client"""

    def __init__(self, connexion):
        self.connexion=connexion

    def ObtenirListeClient(self):
        listeClient = []
        try:
            curseur = self.connexion.cursor()
            curseur.execute(self.sql_obtenir_liste_client)
            for tuple in curseur.fetchall():
                listeClient.append(TupleClient(tuple[0], tuple[1], tuple[2]))
        except (Exception)as error:
            print(error)
        return listeClient
