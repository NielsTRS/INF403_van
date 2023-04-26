DROP TABLE IF EXISTS Personnes;
DROP TABLE IF EXISTS ModeleAppareils;
DROP TABLE IF EXISTS Appareils;
DROP TABLE IF EXISTS Reparations;
DROP TABLE IF EXISTS Evenements;


CREATE TABLE Personnes (
  numero_personne INT NOT NULL,
  nom_personne VARCHAR(255) NOT NULL,
  prenom_personne VARCHAR(255) NOT NULL,
  email_personne VARCHAR(255),
  PRIMARY KEY (numero_personne)
);

CREATE TABLE ModeleAppareils (
  numero_appareil INT NOT NULL,
  marque_appareil VARCHAR(255) NOT NULL,
  modele_appareil VARCHAR(255) NOT NULL,
  ram_appareil INT,
  processeur_appareil VARCHAR(255),
  type_appareil VARCHAR(255) CHECK(type_appareil IN ('smartphone', 'tablette', 'ordinateur_portable', 'ordinateur_bureau')),
  PRIMARY KEY (numero_appareil)
);

CREATE TABLE Appareils (
  numeroDeSerie_appareil INT NOT NULL,
  numero_appareil INT NOT NULL,
  proprietaire_appareil INT NOT NULL,
  PRIMARY KEY (numeroDeSerie_appareil),
  FOREIGN KEY (numero_appareil) REFERENCES ModeleAppareils(numero_appareil),
  FOREIGN KEY (proprietaire_appareil) REFERENCES Personnes(numero_personne)
);

CREATE TABLE Reparations (
  numero_reparation INT NOT NULL,
  appareil_repare INT NOT NULL,
  evenement_reparation INT NOT NULL,
  prix_reparation DECIMAL(10, 2),
  duree_reparation INT,
  description_reparation VARCHAR(255),
  PRIMARY KEY (numero_reparation),
  FOREIGN KEY (appareil_repare) REFERENCES Appareils(numeroDeSerie_appareil),
  FOREIGN KEY (evenement_reparation) REFERENCES Evenements(numero_evenement)
);

CREATE TABLE Evenements (
  numero_evenement INT NOT NULL,
  dateDebut_evenement DATE,
  dateFin_evenement DATE,
  ville_evenement VARCHAR(255),
  PRIMARY KEY (numero_evenement)
);
