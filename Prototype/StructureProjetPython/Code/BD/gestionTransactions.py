from BD.Tables.tableItem import TableItem
from BD.Tables.tableVente import TableVente
from BD.Tables.tableClient import TableClient
from Modeles.item import Item
from Modeles.vente import Vente
from constantes import *

class GestionTransactions:
    def __init__(self, connexion):
        self.connexion=connexion
        self.tableItem = TableItem(self.connexion)
        self.tableVente = TableVente(self.connexion)
        self.tableClient = TableClient(self.connexion)

    
    def VenteExiste(self, id):
        return self.tableVente.RequeteExisteVente(id)

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
            # 1. Validations
            if (self.VenteExiste(vente.id)):
                raise BoutiqueException("La vente ayant pour id : {} existe déjà. Impossible de l'ajouter.".format(vente.id))
            if (self.tableClient.RequeteExisteClient(vente.id_client) is False):
                raise BoutiqueException("Le client ayant pour id : {} n'existe pas. Impossible de procéder à la vente".format(vente.id_client))
            if (self.tableItem.RequeteExisteItem(vente.id_item) is False):
                raise BoutiqueException("L'item ayant pour id : {} n'existe pas. Impossible de procéder à la vente".format(vente.id_item))
            #On doit vérifier s'il reste suffisament de quantité de l'item qu'on veut acheter
            tuple = self.tableItem.RequeteUnItem(vente.id_item)
            item = Item(*tuple)
            if (vente.quantite > item.quantite):
                raise BoutiqueException("Il n'y a pas suffisament de {} pour procéder à la vente...".format(item.nom))
            # 2. Actions
            #On ajoute la vente
            id = self.tableVente.RequeteAjouterVente(vente.id_client, vente.id_item, vente.quantite)
            #On met à jour la quantité de l'item
            nouvelleQuantite = item.quantite - vente.quantite
            self.tableItem.RequeteModifierQuantiteItem(item.id, nouvelleQuantite)
            # 3. Enregistrement
            self.connexion.commit()
            return id
        except (Exception)as error:
            print(error)
    
    def SupprimerVente(self, vente):
        try:
            # 1. Validations
            if (self.VenteExiste(vente.id) is False):
                raise BoutiqueException("La vente ayant pour id : {} n'existe pas. Impossible de la supprimer".format(vente.id))
            # 2. Actions
            self.tableVente.RequeteSupprimerVente(vente.id)
            # 3. Enregistrement
            self.connexion.commit()
        except (Exception)as error:
            print(error)