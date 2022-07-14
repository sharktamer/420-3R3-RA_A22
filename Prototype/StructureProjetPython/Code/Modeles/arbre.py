from Modeles.item import Item
from constantes import *
class Arbre(Item):
    def __init__(self, id, nom, description, prix, quantite, hauteur):
        super().__init__(id, CATEGORIE_ARBRE, nom, description, prix, quantite)
        self.hauteur = hauteur

    def AfficherConsole(self):
        print("\nid:{}\nCatégorie:Arbre\nnom:{}\ndescription:{}\nprix:{}\nquantite:{}"
            .format(self.id, self.nom, self.description, self.prix, self.quantite))
        print("hauteur:{}".format(self.hauteur))