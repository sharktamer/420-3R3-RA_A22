from BD.gestionClients import GestionClients
from BD.gestionProduits import GestionProduits
from BD.gestionTransactions import GestionTransactions
from Modeles.client import Client


# Cette classe de gestion globale peut sembler être répétitive face aux classes de transactions, mais l'idée est de séparer les types de transactions dans des classes différentes
# Autrement dit on fournit un point d'entré unique dans l'application, il suffit d'utiliser ce gestionnaire pour faire toutes les actions autorisés dans l'application.
# Cela permet de modifier plus facilement des parties de programmes sans affecter le reste.
# On a donc besoin d'un seul gestionnaire globale qui appelle des fonctions de ses gestionnaires spécialisés dont il est composé dans certains aspects du programme.
# On utilise cette couche pour gérer des transactions qui impliquent plusieurs sous-transactions
# C'est à cette couche que l'interface utilisateur est connectée, ce sont les fonctions disponibles directement pour l'utilisateur
# Cette couche ne connaît pas la représentation interne de la BD et manipules seulement les objets modèles
class GestionGlobale:
    def __init__(self, connexion):
        self.connexion = connexion
        self.gestionClients = GestionClients(self.connexion)
        self.gestionProduits = GestionProduits(self.connexion)
        self.gestionVentes = GestionTransactions(self.connexion)

    def AfficherListeClientConsole(self):
        for client in self.gestionClients.ObtenirListeClient():
            client.AfficherConsole()

    def AfficherListeItemConsole(self):
        for item in self.gestionProduits.ObtenirListeItem():
            item.AfficherConsole()

    def AfficherListeVenteConsole(self):
        pass

    def AjouterClient(self, prenom, nom):
        client = Client(None, prenom, nom)
        self.gestionClients.AjouterClient(client)

    def SupprimerClient(self, id):
        client = Client(id, None, None)
        self.gestionClients.SupprimerClient(client)

    def AjouterRoche(self, nom, description, prix, poids, couleur):
        pass

    def AjouterArbre(self, nom, description, prix, hauteur):
        pass

    def SupprimerItem(self, id):
        pass

    def ModifierQuantiteItem(self, id, qt):
        pass

    def VendreItem(self, iditem, idclient, qt):
        pass