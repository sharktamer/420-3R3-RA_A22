from Modeles.item import Item
from constantes import *
class Roche(Item):
    def __init__(self, id, nom, description, prix, quantite, poids, couleur):
        Item.__init__(self, id, CATEGORIE_ROCHE, nom, description, prix, quantite)
        self.poids = poids
        self.couleur = couleur

    def AfficherConsole(self):
        print("\nid:{}\nCatégorie:Roche\nnom:{}\ndescription:{}\nprix:{}\nquantite:{}"
            .format(self.id, self.nom, self.description, self.prix, self.quantite))
        print("poids:{}\ncouleur:{}".format(self.poids, self.couleur))