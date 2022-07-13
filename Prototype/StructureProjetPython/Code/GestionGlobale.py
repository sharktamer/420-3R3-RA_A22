from BD.Transactions.GestionClients import GestionClients
from BD.Transactions.GestionProduits import GestionProduits
from BD.Transactions.GestionVentes import GestionVentes


# Cette classe de gestion globale peut semble être répétitive face aux classes de transactions, mais l'idée est de séparer les types de transactions dans des classes différentes
# Cela permet de modifier plus facilement des parties de programmes sans affecter le reste.
# On a donc besoin d'un seul gestionnaire parent qui appelle des fonctions de ses gestionnaires enfants spécialisés dans certains aspects du programme.
# On utilise cette couche pour gerer des transactions qui impliquent plusieurs sous-transactions
# C'est à cette couche que l'interface utilisateur est connectée.
class GestionGlobale:
    def __init__(self, connexion):
        self.connexion = connexion
        self.gestionClients = GestionClients(self.connexion)
        self.gestionProduits = GestionProduits(self.connexion)
        self.gestionVentes = GestionVentes(self.connexion)