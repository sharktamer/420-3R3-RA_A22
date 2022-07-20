import unittest
from gestionGlobale import GestionGlobale
from Modeles.client import Client
from Modeles.roche import Roche
from Modeles.arbre import Arbre
from Modeles.item import Item
from Modeles.vente import Vente
from constantes import *
import psycopg2

try:
    #Initialisation d'une connexion à la base de données
    connexion = psycopg2.connect(
        host="localhost",
        database="boutique",
        user="postgres",
        password="toor"
    )
except (Exception) as error:
    print(error)
    exit()

# Initialisation du gestionnaire globale utilisé par les tests
gestionnaire = GestionGlobale(connexion)

class TestClient(unittest.TestCase):
    def test_ajout_suppression(self):
        client = Client(ID_DEFAUT_CREATION, "Carlos", "Lamarmotte")
        # On ajoute le client (Par l'interface accessible, donc par le gestionnaire)
        id = gestionnaire.AjouterClient(client.prenom, client.nom)
        # On valide si le client existe maintenant (On peut appeler les fonctions des gestionnaires spécialisés directement pour les tests)
        assert(gestionnaire.gestionClients.ClientExiste(id))
        # On valide que les informations du client sont celles attendues
        client.id = id
        assert(client == gestionnaire.gestionClients.ObtenirUnClient(id))
        # On supprime le client nouvellement ajouté
        gestionnaire.SupprimerClient(id)
        # On valide que le client n'existe plus
        assert(gestionnaire.gestionClients.ClientExiste(id) is False)

class TestArbre(unittest.TestCase):
    def test_ajout_suppression(self):
        arbre = Arbre(ID_DEFAUT_CREATION, "Palmier", "Source #1 de noix de coco", 200.99, 0, 125)
        id = gestionnaire.AjouterArbre(arbre.nom, arbre.description, arbre.prix, arbre.hauteur)
        assert(gestionnaire.gestionProduits.ArbreExiste(id))
        arbre.id = id
        assert(arbre == gestionnaire.gestionProduits.ObtenirUnItem(id))
        gestionnaire.SupprimerItem(id)
        assert(gestionnaire.gestionProduits.ArbreExiste(id) is False)

class TestRoche(unittest.TestCase):
    def test_ajout_suppression(self):
        roche = Roche(ID_DEFAUT_CREATION, "Bedrock", "La roche la plus solide de l'univers", 999.43, 0, 333, "Gris")
        id = gestionnaire.AjouterRoche(roche.nom, roche.description, roche.prix, roche.poids, roche.couleur)
        assert(gestionnaire.gestionProduits.RocheExiste(id))
        roche.id = id
        assert(roche == gestionnaire.gestionProduits.ObtenirUnItem(id))
        gestionnaire.SupprimerItem(id)
        assert(gestionnaire.gestionProduits.RocheExiste(id) is False)

class TestItem(unittest.TestCase):
    def test_modification_quantite(self):
        arbre = Arbre(ID_DEFAUT_CREATION, "Palmier", "Source #1 de noix de coco", 200.99, 0, 125)
        id = gestionnaire.AjouterArbre(arbre.nom, arbre.description, arbre.prix, arbre.hauteur)
        # On valide que la quantite initiale est bien de 0
        item = gestionnaire.gestionProduits.ObtenirUnItem(id)
        assert(item.quantite == 0)
        # On augmente la quantite à 100 et on valide que la nouvelle quantité a été mise à jour
        gestionnaire.ModifierQuantiteItem(id, 100)
        item = gestionnaire.gestionProduits.ObtenirUnItem(id)
        assert(item.quantite == 100)
        # On supprime l'arbre créé pour le test
        gestionnaire.SupprimerItem(id)

class TestVente(unittest.TestCase):

    # Cette fonction s'exécutera au début de chaque fonction test de la classe TestVente
    def setUp(self):
        # On doit avoir minimalement un client et un article dans la BD pour ajouter des ventes
        client = Client(ID_DEFAUT_CREATION, "Carlos", "Lamarmotte")
        arbre = Arbre(ID_DEFAUT_CREATION, "Palmier", "Source #1 de noix de coco", 200.99, 0, 125)
        self.id_client = gestionnaire.AjouterClient(client.prenom, client.nom)
        self.id_item = gestionnaire.AjouterArbre(arbre.nom, arbre.description, arbre.prix, arbre.hauteur)

    # Cette fonction s'exécutera à la fin de chaque test
    def tearDown(self):
        # On supprime le client et l'article créé pour le test (Leurs fonctions ont été testé ailleurs, donc pas besoin de retester ici)
        gestionnaire.SupprimerClient(self.id_client)
        gestionnaire.SupprimerItem(self.id_item)


    def test_ajout_suppression(self):
        vente = Vente(ID_DEFAUT_CREATION, self.id_client, self.id_item, 1)
        # On s'assure de mettre une quantité suffisante pour pouvoir créer la vente
        gestionnaire.ModifierQuantiteItem(self.id_item, 2)
        id = gestionnaire.VendreItem(vente.id_client, vente.id_item, vente.quantite)
        # On valide que la vente a été créée
        assert(gestionnaire.gestionVentes.VenteExiste(id))
        # On s'assure que la vente correspond à ce qui est attendu
        vente.id = id
        assert(vente == gestionnaire.gestionVentes.ObtenirUnVente(id))
        # On supprime et valide la suppression
        gestionnaire.gestionVentes.SupprimerVente(vente)
        assert(gestionnaire.gestionVentes.VenteExiste(id) is False)
    
    def test_quantite_insuffisante(self):
        gestionnaire.ModifierQuantiteItem(self.id_item, 0)
        vente = Vente(ID_DEFAUT_CREATION, self.id_client, self.id_item, 1)
        id = gestionnaire.VendreItem(vente.id_client, vente.id_item, vente.quantite)
        # On essait de vendre un item sans avoir la quantité requise, ce test doit echouer
        assert(gestionnaire.gestionVentes.VenteExiste(id) is False)
        # On supprime la vente créée
        vente.id = id
        gestionnaire.gestionVentes.SupprimerVente(vente)

    def test_quantite_item_maj_apres_vente(self):
        vente = Vente(ID_DEFAUT_CREATION, self.id_client, self.id_item, 37)
        gestionnaire.ModifierQuantiteItem(self.id_item, 100)
        # On valide que la quantité de l'item est bien 100
        item = gestionnaire.gestionProduits.ObtenirUnItem(self.id_item)
        assert(item.quantite == 100)
        # On effectue la vente de 37 unités
        id = gestionnaire.VendreItem(vente.id_client, vente.id_item, vente.quantite)
        # On valide que la quantité de l'item est bien de 63 maintenant 
        item = gestionnaire.gestionProduits.ObtenirUnItem(self.id_item)
        assert(item.quantite == 63)
        # On supprime la vente créée
        vente.id = id
        gestionnaire.gestionVentes.SupprimerVente(vente)
    


if __name__ == '__main__':
    unittest.main()