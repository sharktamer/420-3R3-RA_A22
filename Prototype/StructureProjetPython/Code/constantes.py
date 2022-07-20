# Ces données seraient idéalement dans la BD dans leur propre table,
# mais afin de simplifier le code je vais tricher en utilisant des constantes
# pour les catégories
CATEGORIE_ROCHE = 1;
CATEGORIE_ARBRE = 2;
ID_DEFAUT_CREATION = None;

# Création d'un type d'exception spécifique à ce programme.
# Cela sert à afficher les erreurs dans les validations effectuées
# lors des transactions des gestionnaires spécialisés.
# On pourrait utiliser des exceptions existantes, mais créer notre propre classe
# est une bonne pratique pour pouvoir attraper les erreurs spécifiques à la
# logique interne de notre programme plutôt que ceux du langage.
class BoutiqueException(Exception):
    pass