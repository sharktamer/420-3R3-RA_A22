from BD.Tables.tableItem import TableItem
from BD.Tables.tableRoche import TableRoche
from BD.Tables.tableArbre import TableArbre
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
    # 3. Enregistrer les changements (Si la transactions modifie la table)


class GestionProduits:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableItem = TableItem(self.connexion)
        self.tableRoche = TableRoche(self.connexion)
        self.tableArbre = TableArbre(self.connexion)

    def ItemExiste(self, id):
        return self.tableItem.RequeteExisteItem(id)
    
    def RocheExiste(self, id):
        return self.tableItem.RequeteExisteItem(id) and self.tableRoche.RequeteExisteRoche(id)
    
    def ArbreExiste(self, id):
        return self.tableItem.RequeteExisteItem(id) and self.tableArbre.RequeteExisteArbre(id)

    def ObtenirListeItem(self):
        listeItem = []
        for tuple in self.tableItem.RequeteToutItem():
            listeItem.append(Item(*tuple))
        listeItemCategorise = []
        for item in listeItem:
            if (item.id_categorie == CATEGORIE_ROCHE):
                listeItemCategorise.append(Roche.Roche_parItem(item,
                                                            self.tableRoche.RequetePoidsRoche(item.id),
                                                            self.tableRoche.RequeteCouleurRoche(item.id)
                                                            ))
            elif (item.id_categorie == CATEGORIE_ARBRE):
                listeItemCategorise.append(Arbre.Arbre_parItem(item, 
                                                            self.tableArbre.RequeteHauteurArbre(item.id)
                                                            ))
        return listeItemCategorise
    
    def ObtenirUnItem(self, id):
        try:
            # 1. Validations
            if (self.ItemExiste(id) is False):
                raise BoutiqueException("L'item ayant pour id : {} n'existe pas. Impossible de l'obtenir".format(id))
            # 2. Actions
            tuple = self.tableItem.RequeteUnItem(id)
            item = Item(*tuple)
            if (item.id_categorie == CATEGORIE_ROCHE):
                return Roche.Roche_parItem(item, self.tableRoche.RequetePoidsRoche(item.id), self.tableRoche.RequeteCouleurRoche(item.id))
            elif (item.id_categorie == CATEGORIE_ARBRE):
                return Arbre.Arbre_parItem(item, self.tableArbre.RequeteHauteurArbre(item.id))
        except (Exception)as error:
            print(error)


    def AjouterItem(self, item):
        #Soit on fait la transaction au complet, soit on n'enregistre rien. 
        #Aucune transactions partielle ne doit être effectué
        try:
            # 1. Validations
            if (self.ItemExiste(item.id)):
                raise BoutiqueException("L'item ayant pour id : {} existe déjà. Impossible de l'ajouter".format(item.id))
            # 2. Actions
            # On crée l'entrée des infos de base de l'objet dans la BD
            id = self.tableItem.RequeteAjouterItem(item.id_categorie, item.nom, item.description, item.prix, item.quantite)
            # On ajoute les infos propres à la catégorie de l'item
            if (item.id_categorie == CATEGORIE_ROCHE):
                self.tableRoche.RequeteAjouterRoche(id, item.poids, item.couleur)
            elif(item.id_categorie == CATEGORIE_ARBRE):
                self.tableArbre.RequeteAjouterArbre(id, item.hauteur)
            # 3. Enregistrement
            self.connexion.commit()
            return id
        except (Exception)as error:
            print(error)
    
    def SupprimerItem(self, item):
        try:
            # 1. Validations
            if (self.ItemExiste(item.id) is False):
                raise BoutiqueException("L'item ayant pour id : {} n'existe pas. Impossible de le supprimer".format(item.id))
            # 2. Actions
            # On doit d'abord supprimer les éléments qui font référence à la clé id d'item
            if (item.id_categorie == CATEGORIE_ROCHE):
                self.tableRoche.RequeteSupprimerRoche(item.id)
            elif(item.id_categorie == CATEGORIE_ARBRE):
                self.tableArbre.RequeteSupprimerArbre(item.id)
            # On peut ensuite supprimer l'item
            self.tableItem.RequeteSupprimerItem(item.id)
            # 3. Enregistrement
            self.connexion.commit()
        except (Exception)as error:
            print(error)

    def ModifierQuantiteItem(self, item, quantite):
        try:
            # 1. Validations
            if (self.ItemExiste(item.id) is False):
                raise BoutiqueException("L'item ayant pour id : {} n'existe pas. Impossible de modifier sa quantité".format(item.id))
            # 2. Actions
            self.tableItem.RequeteModifierQuantiteItem(item.id, quantite)
            # 3. Enregistrement
            self.connexion.commit()
        except (Exception)as error:
            print(error)
