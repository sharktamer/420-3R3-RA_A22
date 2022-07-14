class Item:
    def __init__(self, id, id_categorie, nom, description, prix, quantite):
        self.id = id
        self.id_categorie = id_categorie
        self.nom = nom
        self.description = description
        self.prix = prix
        self.quantite = quantite
    
    def AfficherConsole(self):
        print("\nid:{}\nid_categorie:{}\nnom:{}\ndescription:{}\nprix:{}\nquantite:{}"
            .format(self.id, self.id_categorie, self.nom, self.description, self.prix, self.quantite))