# Dans cette classe de gestion spécialisé pour les clients, l'objet communique directement avec les gestionnaires de table de base de données pertinents pour obtenir les données
# On utilise cette couche pour gerer des transactions qui implique plusieurs tables en même temps
# Cette couche connait à la fois la structure de la BD et les modèles de représentation des objets du logiciel
from .Tables.TableClient import TableClient
from Modeles.Client import Client

class GestionClients:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableClient=TableClient(self.connexion)

    def ObtenirListeClient(self):
        listeClient = []
        for tuple in self.tableClient.RequeteToutClient():
            listeClient.append(Client(tuple[0], tuple[1], tuple[2]))
        return listeClient
    
    def ObtenirUnClient(self, id):
        tuple = self.tableClient.RequeteUnClient(id)
        return Client(tuple[0], tuple[1], tuple[2])

    def AjouterClient(self, client):
        self.tableClient.RequeteAjouterClient(client.prenom, client.nom)
        self.connexion.commit()
    
    def SupprimerClient(self, client):
        # 1. Effectuer les vérifications requises
        # 2. Effectuer les actions
        self.tableClient.RequeteSupprimerClient(client.id)
        # 3. Enregistrer les changements
        self.connexion.commit()