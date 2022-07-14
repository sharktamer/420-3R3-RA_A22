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

gestionnaire = GestionGlobale(connexion)

class TestClient(unittest.TestCase):
    def test_ajout(self):
        client = Client(ID_DEFAUT_CREATION, "Carlos", "Lamarmotte")
    def test_suppression(self):
        pass

class TestItem(unittest.TestCase):
    def test_ajout(self):
        pass
    def test_suppression(self):
        pass

class TestArbre(unittest.TestCase):
    def test_ajout(self):
        pass
    def test_suppression(self):
        pass

class TestRoche(unittest.TestCase):
    def test_ajout(self):
        pass
    def test_suppression(self):
        pass

class TestVente(unittest.TestCase):
    def test_ajout(self):
        pass
    def test_suppression(self):
        pass

if __name__ == '__main__':
    unittest.main()