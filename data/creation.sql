DROP VIEW IF EXISTS Reparations_view;
DROP TABLE IF EXISTS Reparations;
DROP TABLE IF EXISTS Evenements;
DROP TABLE IF EXISTS Appareils;
DROP TABLE IF EXISTS ModeleAppareils;
DROP TABLE IF EXISTS Personnes;

CREATE TABLE Personnes
(
    numero_personne INTEGER      NOT NULL,
    nom_personne    VARCHAR(255) NOT NULL,
    prenom_personne VARCHAR(255) NOT NULL,
    email_personne  VARCHAR(255),
    CONSTRAINT pk_pers_num PRIMARY KEY (numero_personne AUTOINCREMENT)
);

CREATE TABLE ModeleAppareils
(
    numero_appareil     INTEGER      NOT NULL,
    marque_appareil     VARCHAR(255) NOT NULL,
    modele_appareil     VARCHAR(255) NOT NULL,
    ram_appareil        INTEGER,
    processeur_appareil VARCHAR(255),
    type_appareil       VARCHAR(255),
    CONSTRAINT ck_modele_type CHECK (type_appareil IN
                                     ('smartphone', 'tablette', 'ordinateur_portable', 'ordinateur_bureau')),
    CONSTRAINT pk_modele_num PRIMARY KEY (numero_appareil AUTOINCREMENT)
);

CREATE TABLE Appareils
(
    numeroDeSerie_appareil VARCHAR(255) NOT NULL,
    numero_appareil        INTEGER      NOT NULL,
    proprietaire_appareil  INTEGER      NOT NULL,
    CONSTRAINT pk_app_num_serie PRIMARY KEY (numeroDeSerie_appareil),
    CONSTRAINT fk_app_num FOREIGN KEY (numero_appareil) REFERENCES ModeleAppareils (numero_appareil),
    CONSTRAINT fk_app_pers FOREIGN KEY (proprietaire_appareil) REFERENCES Personnes (numero_personne)
);

CREATE TABLE Reparations
(
    numero_reparation      INTEGER      NOT NULL,
    appareil_repare        VARCHAR(255) NOT NULL,
    evenement_reparation   INTEGER      NOT NULL,
    prix_reparation        DECIMAL(10, 2),
    duree_reparation       INTEGER,
    description_reparation VARCHAR(255),
    CONSTRAINT pk_rep_num PRIMARY KEY (numero_reparation AUTOINCREMENT),
    CONSTRAINT fk_rep_num_app FOREIGN KEY (appareil_repare) REFERENCES Appareils (numeroDeSerie_appareil),
    CONSTRAINT fk_rep_even FOREIGN KEY (evenement_reparation) REFERENCES Evenements (numero_evenement)
);

CREATE TABLE Evenements
(
    numero_evenement  INTEGER NOT NULL,
    date_evenement DATE,
    heureDebut_evenement TIME,
    heureFin_evenement  TIME,
    ville_evenement     VARCHAR(255),
    CONSTRAINT pk_even_num PRIMARY KEY(numero_evenement AUTOINCREMENT)
);

CREATE VIEW Reparations_view
            (
             client_nom,
             numeroDeSerie,
             prix,
             duree,
             description,
             marque_appareil,
             modele_appareil,
             type_appareil
                )
AS
SELECT nom_personne    AS client_nom,
       appareil_repare AS numeroDeSerie,
       prix_reparation AS prix,
       duree_reparation AS duree,
       description_reparation AS description,
       marque_appareil,
       modele_appareil,
       type_appareil
FROM Reparations R
         JOIN Appareils A ON R.appareil_repare = A.numeroDeSerie_appareil
         JOIN Personnes P ON A.proprietaire_appareil = P.numero_personne
         JOIN ModeleAppareils M USING (numero_appareil);
