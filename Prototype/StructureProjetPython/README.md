# Projet template pour une architecture simple en python d'un programme de gestion qui se connecte à une BD
## Avant la première exécution, ne pas oublier d'installer les dépendances :
- Ouvrez un invite de commande
- Placer vous dans le répertoire "Code" avec la commande cd
- Exécutez la commande : pip install -r "requirements.txt"
- Si vous ajouter des paquets supplémentaires, il est important de mettre ce fichier à jour.

## Si vous avec des problèmes de "module not found" :
- Ouvrez un invite de commande
- Placez-vous dans le répertoire "Code" avec la commande cd
- Exécutez la commande : export PYTHONPATH=.
- Cette commande indique à Python de chercher des modules dans ce dossier en plus de ceux de base

## Pour exécuter le programme, je vous recommande de procéder ainsi (Cela évite des problèmes potentiels avec la structure des imports dans la projet) :
- Ouvrez un invite de commande
- Placez-vous dans le répertoire "Code" avec la commande cd
- Pour le programme, exécutez la commande : python app.y
- Pour les tests, exécutez la commande : python Tests/tests.py