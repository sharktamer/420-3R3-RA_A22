class Arbre:
    def __init__(self, id_item, hauteur):
        self.id_item = id_item
        self.hauteur = hauteur

    def AfficherConsole(self):
        print("\nid:{}\nhauteur:{}".format(self.id_item, self.hauteur))