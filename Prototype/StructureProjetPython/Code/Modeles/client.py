class Client:
    def __init__(self, id, prenom, nom):
        self.id = id
        self.prenom = prenom
        self.nom = nom

    # On remplace la fonction "==" entre 2 Clients par notre propre implantation
    def __eq__(self, other):
        if not isinstance(other, Client):
            return NotImplemented
        return (
            self.id == other.id and
            self.prenom == other.prenom and
            self.nom == other.nom
        )
    
    def AfficherConsole(self):
        print("\nid:{}\nprenom:{}\nnom:{}".format(self.id, self.prenom, self.nom))