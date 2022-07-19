import math
from Modeles.item import Item
from constantes import *
class Arbre(Item):
    def __init__(self, id, nom, description, prix, quantite, hauteur):
        super().__init__(id, CATEGORIE_ARBRE, nom, description, prix, quantite)
        self.hauteur = hauteur

    def __eq__(self, other):
        if not isinstance(other, Arbre):
            return NotImplemented
        return (
            self.id == other.id and
            self.id_categorie == other.id_categorie and
            self.nom == other.nom and
            self.description == other.description and
            math.isclose(self.prix, other.prix) and
            self.quantite == other.quantite and
            self.hauteur == other.hauteur
        )

    #Un constructeur à partir d'un Item
    def Arbre_parItem(item, hauteur):
        return Arbre(item.id, item.nom, item.description, item.prix, item.quantite, hauteur)

    def AfficherConsole(self):
        print("\nid:{}\nCatégorie:Arbre\nnom:{}\ndescription:{}\nprix:{}\nquantite:{}"
            .format(self.id, self.nom, self.description, self.prix, self.quantite))
        print("hauteur:{}".format(self.hauteur))