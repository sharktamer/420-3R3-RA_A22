import psycopg2

from GestionGlobale import GestionGlobale



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


#Initialisation du gestionnaire de programme 
#(C'est lui qui fourni les fonctions à l'interface et gère la communication avec la BD)
gestionnaire = GestionGlobale(connexion)

for client in gestionnaire.gestionClients.tableClient.ObtenirListeClient():
    client.AfficherConsole()

#En quittant le programme, on ferme notre connexion à la base de données
if connexion is not None:
    connexion.close()






