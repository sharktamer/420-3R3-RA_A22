# Ces données serait idéalement dans la BD dans leur propre table,
# mais afin de simplifier le code je vais tricher en utilisant des constantes
# pour les catégorie

CATEGORIE_ROCHE = 1;
CATEGORIE_ARBRE = 2;
ID_DEFAUT_CREATION = None;

class BoutiqueException(Exception):
    pass