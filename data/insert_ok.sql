INSERT INTO Personnes
VALUES (1, 'Bernard', 'Jean', 'jean.bernard@gmail.com');

INSERT INTO Personnes 
VALUES (2, 'Martin', 'Martin', 'martin@martin.com');

INSERT INTO ModeleAppareils 
VALUES (1, 'Xiaomi', 'Redmi Note 7', 4, 'Snapdragon 660', 'smartphone');

INSERT INTO ModeleAppareils
VALUES (2, 'Apple', 'Macbook Pro', 6, 'Apple M2', 'ordinateur_portable');

INSERT INTO Appareils
VALUES ("MG4HQ1", 1, 1);

INSERT INTO Appareils
VALUES ("ABC123", 2, 2);

INSERT INTO Evenements
VALUES (1, '2023-05-01', '14:00', '17:00' , 'Grenoble');

INSERT INTO Reparations ('appareil_repare', 'evenement_reparation', 'prix_reparation', 'duree_reparation', 'description_reparation')
VALUES ("MG4HQ1", 1, 20.99, 20, 'Remplacement de ram');

INSERT INTO Reparations ('appareil_repare', 'evenement_reparation', 'prix_reparation', 'duree_reparation', 'description_reparation')
VALUES ("ABC123", 1, 50.99, 50, 'Remplacement de batterie');