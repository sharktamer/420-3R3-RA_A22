class Vente:
    def __init__(self, id, id_client, id_item, quantite):
        self.id = id
        self.id_client = id_client
        self.id_item = id_item
        self.quantite = quantite
    
    def AfficherConsole(self):
        print("\nid:{}\nid_client:{}\nid_item:{}\nquantite:{}"
            .format(self.id, self.id_client, self.id_item, self.quantite))