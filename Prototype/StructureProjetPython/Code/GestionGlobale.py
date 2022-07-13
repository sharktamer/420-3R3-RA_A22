from BD.GestionClients import GestionClients
from BD.GestionProduits import GestionProduits
from BD.GestionVentes import GestionVentes
from Modeles.Client import Client


# Cette classe de gestion globale peut semble être répétitive face aux classes de transactions, mais l'idée est de séparer les types de transactions dans des classes différentes
# Cela permet de modifier plus facilement des parties de programmes sans affecter le reste.
# On a donc besoin d'un seul gestionnaire parent qui appelle des fonctions de ses gestionnaires enfants spécialisés dans certains aspects du programme.
# On utilise cette couche pour gerer des transactions qui impliquent plusieurs sous-transactions
# C'est à cette couche que l'interface utilisateur est connectée, ce sont les fonctions disponibles directement pour l'utilisateur
# Cette couche ne connaît pas la représentation interne de la BD et manipules seulement les objets modèles
class GestionGlobale:
    def __init__(self, connexion):
        self.connexion = connexion
        self.gestionClients = GestionClients(self.connexion)
        self.gestionProduits = GestionProduits(self.connexion)
        self.gestionVentes = GestionVentes(self.connexion)

    def AfficherListeClientConsole(self):
        for client in self.gestionClients.ObtenirListeClient():
            client.AfficherConsole()

    def AfficherListeItemConsole(self):
        pass

    def AfficherListeRocheConsole(self):
        pass

    def AfficherListeArbreConsole(self):
        pass

    def AfficherListeVenteConsole(self):
        pass

    def AjouterClient(self, prenom, nom):
        pass

    def SupprimerClient(self, id):
        pass

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