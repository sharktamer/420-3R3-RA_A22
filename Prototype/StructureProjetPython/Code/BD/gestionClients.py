# Dans cette classe de gestion spécialisé pour les clients, l'objet communique directement avec les gestionnaires de table de base de données pertinents pour obtenir les données
# On utilise cette couche pour gerer des transactions qui implique plusieurs tables en même temps
# Cette couche connait à la fois la structure de la BD et les modèles de représentation des objets du logiciel
from .Tables.tableClient import TableClient
from Modeles.client import Client

#La construction d'objet avec *tuple est expliqué ici : https://docs.python.org/3.7/tutorial/controlflow.html#unpacking-argument-lists
#On pourrait également construire un item en faisant Client(tuple[0], tuple[1],  ..., tuple[n])
#L'idée générale est qu'on utilise les éléments de la liste un par un et on les passe dans le constructeur de l'objet avec un opérateur * plutôt que manuellement

class GestionClients:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableClient=TableClient(self.connexion)

    def ObtenirListeClient(self):
        listeClient = []
        for tuple in self.tableClient.RequeteToutClient():
            listeClient.append(Client(*tuple))
        return listeClient
    
    def ObtenirUnClient(self, id):
        tuple = self.tableClient.RequeteUnClient(id)
        return Client(*tuple)

    def AjouterClient(self, client):
        #Soit on fait la transaction au complet, soit on n'enregistre rien. 
        #Aucune transactions partielle ne doit être effectué
        #C'est pourquoi les Try Catch son essentiel ici.
        try:
            self.tableClient.RequeteAjouterClient(client.prenom, client.nom)
            self.connexion.commit()
        except (Exception)as error:
            print(error)
    
    def SupprimerClient(self, client):
        try:
            self.tableClient.RequeteSupprimerClient(client.id)
            self.connexion.commit()
        except (Exception)as error:
            print(error)