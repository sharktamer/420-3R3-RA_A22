import math
class Item:
    def __init__(self, id, id_categorie, nom, description, prix, quantite):
        self.id = id
        self.id_categorie = id_categorie
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantite = quantite

    # On remplace la fonction "==" entre 2 Items par notre propre implantation
    def __eq__(self, other):
        if not isinstance(other, Item):
            return NotImplemented
        return (
            self.id == other.id and
            self.id_categorie == other.id_categorie and
            self.nom == other.nom and
            self.description == other.description and
            # Le == entre 2 nombre à virgule flotante n'est pas fiable en raison des arrondissements. 
            # On utilise donc la fonction du module math pour la comparaison
            math.isclose(self.prix, other.prix) and
            self.quantite == other.quantite
        )

    def AfficherConsole(self):
        pass