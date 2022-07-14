import psycopg2
import argparse

from gestionGlobale import GestionGlobale

################
# Initialisaton
################
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

# Initialisation du gestionnaire globale
# C'est cet objet qui contient toutes les fonctions disponible à l'interface (visuelle ou command line)
gestionnaire = GestionGlobale(connexion)

###############
# Interface Command Line
###############
################
# Pour ce modèle de base de structure de projet python j'ai inclus une interface
# en command line. La logique de l'architecture est que chaque composante est
# séparée. Pour faire une interface graphique, il suffirait juste d'initier une
# connexion et un gestionnaire. On asscocierait ensuite des événements aux fonctions
# du gestionnaire et le reste du programme continuerait à fonctionner sans qu'aucun
# changement au backend soit nécessaire.
# Idée d'interface python : pyQt5, tkinter
# Idée web : Transformer cette app en contrôleur web REST avec par exemple Flask
#           et effectuer des requêtes http pour créer une interface web.
################

# 1. Définition des commandes du programme
interpreteur = argparse.ArgumentParser(prog='App', usage='%(prog)s [options] parametres', description="Interface textuelle pour gerer l'application")
sousInterpreteur = interpreteur.add_subparsers(dest='command')

listc = sousInterpreteur.add_parser('listc', help='Affiche la liste des clients')
listi = sousInterpreteur.add_parser('listi', help='Affiche la liste des items')

addc = sousInterpreteur.add_parser('addc', help='Ajoute un client')
addc.add_argument('--prenom', type=str, required=True)
addc.add_argument('--nom', type=str, required=True)

delc = sousInterpreteur.add_parser('delc', help='Supprime un client')
delc.add_argument('--id', type=int, required=True)

addr = sousInterpreteur.add_parser('addr', help='Ajoute une nouvelle roche')
addr.add_argument('--nom', type=str, required=True)
addr.add_argument('--description', type=str, required=True)
addr.add_argument('--prix', type=float, required=True)
addr.add_argument('--poids', type=int, required=True)
addr.add_argument('--couleur', type=str, required=True)

adda = sousInterpreteur.add_parser('adda', help='Ajoute un nouvel arbre')
adda.add_argument('--nom', type=str, required=True)
adda.add_argument('--description', type=str, required=True)
adda.add_argument('--prix', type=float, required=True)
adda.add_argument('--hauteur', type=int, required=True)

deli = sousInterpreteur.add_parser('deli', help='Supprime un item')
deli.add_argument('--id', type=int, required=True)

buy = sousInterpreteur.add_parser('buy', help='Modifie la quantite d''un item')
buy.add_argument('--id', type=int, required=True)
buy.add_argument('--qt', type=int, required=True)

sell = sousInterpreteur.add_parser('sell', help='Vente d''un item')
sell.add_argument('--iditem', type=int, required=True)
sell.add_argument('--idclient', type=int, required=True)
sell.add_argument('--qt', type=int, required=True)

arguments = interpreteur.parse_args()

# 2. Interpretation des commandes passées au programme (Envoi à la bonne fonction)
if (arguments.command == "listc"):
    gestionnaire.AfficherListeClientConsole()
elif (arguments.command == "listi"):
    gestionnaire.AfficherListeItemConsole()
elif (arguments.command == "listv"):
    gestionnaire.AfficherListeVenteConsole()
elif (arguments.command == "addc"):
    gestionnaire.AjouterClient(arguments.prenom, arguments.nom)
elif (arguments.command == "delc"):
    gestionnaire.SupprimerClient(arguments.id)
elif (arguments.command == "addr"):
    gestionnaire.AjouterRoche(arguments.nom, arguments.description, arguments.prix, arguments.poids, arguments.couleur)
elif (arguments.command == "adda"):
    gestionnaire.AjouterArbre(arguments.nom, arguments.description, arguments.prix, arguments.hauteur)
elif (arguments.command == "deli"):
    gestionnaire.SupprimerItem(arguments.id)
elif (arguments.command == "buy"):
    gestionnaire.ModifierQuantiteItem(arguments.id, arguments.qt)
elif (arguments.command == "sell"):
    gestionnaire.VendreItem(arguments.iditem, arguments.idclient, arguments.qt)

################
# Fin
################
#En quittant le programme, on ferme notre connexion à la base de données
if connexion is not None:
    connexion.close()






