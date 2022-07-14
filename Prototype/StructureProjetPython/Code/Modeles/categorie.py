class Categorie:
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
    
    def AfficherConsole(self):
        print("\nid:{}\nnom:{}".format(self.id, self.nom))