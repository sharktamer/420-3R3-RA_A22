from .Tables.tableItem import TableItem
from .Tables.tableRoche import TableRoche
from .Tables.tableArbre import TableArbre
from Modeles.item import Item
from Modeles.arbre import Arbre
from Modeles.roche import Roche
from constantes import *


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
        listeItemCategorise = []
        for item in listeItem:
            if (item.id_categorie == CATEGORIE_ROCHE):
                listeItemCategorise.append(Roche(item.id,
                                                item.nom,
                                                item.description,
                                                item.prix,
                                                item.quantite,
                                                self.tableRoche.RequetePoidsRoche(item.id),
                                                self.tableRoche.RequeteCouleurRoche(item.id)))
            elif (item.id_categorie == CATEGORIE_ARBRE):
                listeItemCategorise.append(Arbre(item.id,
                                                item.nom,
                                                item.description,
                                                item.prix,
                                                item.quantite,
                                                self.tableArbre.RequeteHauteurArbre(item.id)))
        return listeItemCategorise
    
    def ObtenirUnItem(self, id):
        tuple = self.tableItem.RequeteUnItem(id)
        return Item(*tuple)

    def AjouterItem(self, item):
        #Soit on fait la transaction au complet, soit on n'enregistre rien. 
        #Aucune transactions partielle ne doit être effectué
        #C'est pourquoi les Try Catch son essentiel ici.
        try:
            # On crée l'entrée des infos de base de l'objet dans la BD
            self.tableItem.RequeteAjouterItem(item.id_categorie, item.nom, item.description, item.prix, item.quantite)
            # On ajoute les infos propres à la catégorie de l'item
            if (item.id_categorie == CATEGORIE_ROCHE):
                self.tableRoche.RequeteAjouterRoche(item.id, item.poids, item.couleur)
            elif(item.id_categorie == CATEGORIE_ARBRE):
                self.tableArbre.RequeteAjouterArbre(item.id, item.hauteur)
            self.connexion.commit()
        except (Exception)as error:
            print(error)
    
    def SupprimerItem(self, item):
        try:
            # On doit d'abord supprimer les éléments qui font référence à la clé id d'item
            if (item.id_categorie == CATEGORIE_ROCHE):
                self.tableRoche.RequeteSupprimerRoche(item.id)
            elif(item.id_categorie == CATEGORIE_ARBRE):
                self.tableArbre.RequeteSupprimerArbre(item.id)
            # On peut ensuite supprimer l'item
            self.tableItem.RequeteSupprimerItem(item.id)
            self.connexion.commit()
        except (Exception)as error:
            print(error)
