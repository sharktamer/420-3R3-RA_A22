import math
from Modeles.item import Item
from constantes import *
class Arbre(Item):
    def __init__(self, id, nom, description, prix, quantite, hauteur):
        super().__init__(id, CATEGORIE_ARBRE, nom, description, prix, quantite)
        self.hauteur = hauteur

    # On remplace la fonction "==" entre 2 Arbres par notre propre implantation
    def __eq__(self, other):
        if not isinstance(other, Arbre):
            return NotImplemented
        return (
            self.id == other.id and
            self.id_categorie == other.id_categorie and
            self.nom == other.nom and
            self.description == other.description and
            # Le == entre 2 nombre à virgule flotante n'est pas fiable en raison des arrondissements. 
            # On utilise donc la fonction du module math pour la comparaison
            math.isclose(self.prix, other.prix) and
            self.quantite == other.quantite and
            math.isclose(self.hauteur, other.hauteur)
        )

    #Un constructeur à partir d'un Item
    def Arbre_parItem(item, hauteur):
        return Arbre(item.id, item.nom, item.description, item.prix, item.quantite, hauteur)

    def AfficherConsole(self):
        print("\nid:{}\nCatégorie:Arbre\nnom:{}\ndescription:{}\nprix:{}\nquantite:{}"
            .format(self.id, self.nom, self.description, self.prix, self.quantite))
        print("hauteur:{}".format(self.hauteur))