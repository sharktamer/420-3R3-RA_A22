# Dans cette classe de gestion spécialisé pour les clients, l'objet communique directement avec les gestionnaires de table de base de données pertinents pour obtenir les données
# On utilise cette couche pour gerer des transactions qui implique plusieurs tables en même temps
from ..Tables.TableClient import TableClient

class GestionClients:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableClient=TableClient(self.connexion)