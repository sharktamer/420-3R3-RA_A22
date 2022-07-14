from .Tables.tableItem import TableItem
from .Tables.tableVente import TableVente
from Modeles.item import Item
from Modeles.vente import Vente
from constantes import *

class GestionTransactions:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableItem = TableItem(self.connexion)
        self.tableVente = TableVente(self.connexion)

    def ObtenirListeVente(self):
        listeVente = []
        for tuple in self.tableVente.RequeteToutVente():
            listeVente.append(Vente(*tuple))
        return listeVente
    
    def ObtenirUnVente(self, id):
        tuple = self.tableVente.RequeteUnVente(id)
        return Vente(*tuple)

    def AjouterVente(self, vente):
        try:
            #On doit vérifié s'il reste suffisament de quantité de l'item qu'on veut acheté
            tuple = self.tableItem.RequeteUnItem(vente.id_item)
            item = Item(*tuple)

            if (vente.quantite > item.quantite):
                raise BoutiqueException("Il n'y a pas suffisament de {} pour procéder à la vente...".format(item.nom))

            #On ajoute la vente
            id = self.tableVente.RequeteAjouterVente(vente.id_client, vente.id_item, vente.quantite)
            #On met à jour la quantité de l'item
            nouvelleQuantite = item.quantite - vente.quantite
            self.tableItem.RequeteModifierQuantiteItem(item.id, nouvelleQuantite)
            self.connexion.commit()
        except (Exception)as error:
            print(error)
    
    def SupprimerVente(self, vente):
        try:
            self.tableVente.RequeteSupprimerVente(vente.id)
            self.connexion.commit()
        except (Exception)as error:
            print(error)