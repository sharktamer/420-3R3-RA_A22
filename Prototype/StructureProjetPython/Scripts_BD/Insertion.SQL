/* Scripts d'insertion des données de base de la BD */
INSERT INTO Client (id, prenom, nom) 
VALUES
(1, 'Mathieu', 'Morissette'),
(2, 'Simone', 'Lemieux'),
(3, 'Jean', 'Tremblay');

INSERT INTO Item (id, id_categorie, nom, description, prix, quantite) 
VALUES
(1, 1, 'Météorite', 'Une grosse roche venue de l''espace Wow!', 799.99, 23),
(2, 1, 'Caillou', 'Aussi le nom d''une excellente série pour enfant!', 9.25, 111),
(3, 2, 'Bouleau', 'Son écorce est incroyable pour allumer un feu.', 112.13, 8),
(4, 2, 'Érable', 'Source #1 du sirop d''érable!', 234.72, 37),
(5, 2, 'Sapin', 'Attention, ça pique...', 87.02, 49);

INSERT INTO Roche (id_item, poids, couleur)
VALUES
(1, 5000, 'Orange'),
(2, 3, 'Gris');

INSERT INTO Arbre (id_item, hauteur)
VALUES
(3, 12),
(4, 25),
(5, 42);

INSERT INTO Vente (id_client, id_item, quantite)
VALUES
(1, 1, 2),
(1, 4, 3),
(2, 5, 11),
(2, 5, 1),
(3, 3, 7),
(3, 2, 8);