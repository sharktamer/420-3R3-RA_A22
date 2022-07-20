import math
from Modeles.item import Item
from constantes import *
class Roche(Item):
    def __init__(self, id, nom, description, prix, quantite, poids, couleur):
        super().__init__(id, CATEGORIE_ROCHE, nom, description, prix, quantite)
        self.poids = poids
        self.couleur = couleur

    # On remplace la fonction "==" entre 2 Roches par notre propre implantation
    def __eq__(self, other):
        if not isinstance(other, Roche):
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
            math.isclose(self.poids, other.poids) and
            self.couleur == other.couleur
        )


    # Un constructeur à partir d'un Item
    def Roche_parItem(item, poids, couleur):
        return Roche(item.id, item.nom, item.description, item.prix, item.quantite, poids, couleur)

    def AfficherConsole(self):
        print("\nid:{}\nCatégorie:Roche\nnom:{}\ndescription:{}\nprix:{}\nquantite:{}"
            .format(self.id, self.nom, self.description, self.prix, self.quantite))
        print("poids:{}\ncouleur:{}".format(self.poids, self.couleur))