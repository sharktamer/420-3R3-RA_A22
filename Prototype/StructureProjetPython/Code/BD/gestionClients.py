from BD.Tables.tableClient import TableClient
from Modeles.client import Client
from constantes import *


###################
# Notes
###################
# Dans cette classe de gestion spécialisé pour les clients, l'objet communique directement avec les gestionnaires de table de base de données pertinents pour obtenir les données
# On utilise cette couche pour gerer des transactions qui implique plusieurs tables en même temps
# Cette couche connait à la fois la structure de la BD et les modèles de représentation des objets du logiciel
#####################
# La logique des transaction devrait toujours être la suivante:
    # 1. Effectuer les vérifications requises
    # 2. Effectuer les actions
    # 3. Enregistrer les changements (Si la transactions modifie la table)
# Soit on fait la transaction au complet, soit on n'enregistre rien. 
# Aucune transactions partielle ne doit être effectué
######################
# La construction d'objet avec *tuple est expliqué ici : https://docs.python.org/3.7/tutorial/controlflow.html#unpacking-argument-lists
# On pourrait également construire un item en faisant Client(tuple[0], tuple[1],  ..., tuple[n])
# L'idée générale est qu'on utilise les éléments de la liste un par un et on les passe dans le constructeur de l'objet avec un opérateur * plutôt que manuellement
#####################

class GestionClients:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableClient=TableClient(self.connexion)

    def ClientExiste(self, id):
        return self.tableClient.RequeteExisteClient(id)

    def ObtenirListeClient(self):
        listeClient = []
        for tuple in self.tableClient.RequeteToutClient():
            listeClient.append(Client(*tuple))
        return listeClient
    
    def ObtenirUnClient(self, id):

        if (self.ClientExiste(id) is False):
                raise BoutiqueException("Le client ayant pour id : {} n'existe pas".format(id))

        tuple = self.tableClient.RequeteUnClient(id)
        return Client(*tuple)

    def AjouterClient(self, client):
        try:
            # 1. Validations
            if (self.ClientExiste(client.id)):
                raise BoutiqueException("Le client ayant pour id : {} existe déjà. Impossible de l'ajouter.".format(client.id))
            # 2. Actions
            id = self.tableClient.RequeteAjouterClient(client.prenom, client.nom)
            # 3. Enregistrement
            self.connexion.commit()
            return id
        except (Exception)as error:
            print(error)
    
    def SupprimerClient(self, client):
        try:
            # 1. Validations
            if (self.ClientExiste(client.id) is False):
                raise BoutiqueException("Le client ayant pour id : {} n'existe pas. Impossible de le supprimer.".format(client.id))
            # 2. Actions
            self.tableClient.RequeteSupprimerClient(client.id)
            # 3. Enregistrement
            self.connexion.commit()
        except (Exception)as error:
            print(error)