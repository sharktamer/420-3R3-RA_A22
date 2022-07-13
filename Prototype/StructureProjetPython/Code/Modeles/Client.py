class Client:
    def __init__(self, id, prenom, nom):
        self.id = id
        self.prenom = prenom
        self.nom = nom 
    
    def AfficherConsole(self):
        print("\nid:{}\nprenom:{}\nnom:{}".format(self.id, self.prenom, self.nom))