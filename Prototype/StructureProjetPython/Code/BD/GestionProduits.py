from .Tables.tableItem import TableItem
from .Tables.tableRoche import TableRoche
from .Tables.tableArbre import TableArbre
from Modeles.item import Item
from Modeles.arbre import Arbre
from Modeles.roche import Roche


#La construction d'objet avec *tuple est expliqué ici : https://docs.python.org/3.7/tutorial/controlflow.html#unpacking-argument-lists
#On pourrait également construire un item en faisant Item(tuple[0], tuple[1],  ..., tuple[n])
#L'idée générale est qu'on utilise les éléments de la liste un par un et on les passe dans le constructeur de l'objet avec un opérateur * plutôt que manuellement

#La logique des transaction devrait toujours être la suivante:
    # 1. Effectuer les vérifications requises
    # 2. Effectuer les actions
    # 3. Enregistrer les changements


class GestionProduits:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableItem = TableItem(self.connexion)
        self.tableRoche = TableRoche(self.connexion)
        self.tableArbre = TableArbre(self.connexion)

    def ObtenirListeItem(self):
        listeItem = []
        for tuple in self.tableItem.RequeteToutItem():
            listeItem.append(Item(*tuple))
        return listeItem
    
    def ObtenirUnItem(self, id):
        tuple = self.tableItem.RequeteUnItem(id)
        return Item(*tuple)

    def AjouterItem(self, item):
        #Soit on fait la transaction au complet, soit on n'enregistre rien. 
        #Aucune transactions partielle ne doit être effectué
        #C'est pourquoi les Try Catch son essentiel ici.
        try:
            self.tableItem.RequeteAjouterItem(item.id_categorie, item.nom, item.description, item.prix, item.quantite)
            
            
            self.connexion.commit()
        except (Exception)as error:
            print(error)
    
    def SupprimerItem(self, item):
        try:
            self.tableItem.RequeteSupprimerItem(item.id)
            self.connexion.commit()
        except (Exception)as error:
            print(error)
