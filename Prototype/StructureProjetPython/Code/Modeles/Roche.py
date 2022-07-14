class Roche:
    def __init__(self, id_item, poids, couleur):
        self.id_item = id_item
        self.poids = poids
        self.couleur = couleur

    def AfficherConsole(self):
        print("\nid:{}\npoids{}\ncouleur:{}"
            .format(self.id_item, self.poids, self.couleur))