/* Scripts de création de BD */
CREATE TABLE Client (
    id SERIAL,
    prenom VARCHAR(64) NOT NULL,
    nom VARCHAR(64) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE Item (
    id SERIAL,
    id_categorie INTEGER NOT NULL,
    nom VARCHAR(64) NOT NULL,
    description VARCHAR(512) NOT NULL,
    prix NUMERIC NOT NULL,
    quantite INTEGER NOT NULL,
    PRIMARY KEY (id),
);

CREATE TABLE Roche (
    id_item INTEGER NOT NULL,
    poids NUMERIC NOT NULL,
    couleur VARCHAR(64),
    PRIMARY KEY (id_item),
    FOREIGN KEY (id_item) REFERENCES Item (id)
);

CREATE TABLE Arbre (
    id_item INTEGER NOT NULL,
    hauteur NUMERIC NOT NULL,
    PRIMARY KEY (id_item),
    FOREIGN KEY (id_item) REFERENCES Item (id)
);

CREATE TABLE Vente (
    id SERIAL,
    id_client INTEGER NOT NULL,
    id_item INTEGER NOT NULL,
    quantite INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id_item) REFERENCES Item (id),
    FOREIGN KEY (id_client) REFERENCES Client (id)
);