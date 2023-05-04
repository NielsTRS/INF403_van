INSERT INTO Personnes
VALUES (1, 'Bernard', 'Jean', 'jean.bernard@gmail.com');

INSERT INTO Personnes 
VALUES (2, 'Martin', 'Jacques', 'jacques@martin.com');

INSERT INTO ModeleAppareils 
VALUES (1, 'Xiaomi', 'Redmi Note 7', 4, 'Snapdragon 660', 'smartphone');

INSERT INTO ModeleAppareils
VALUES (2, 'Apple', 'Macbook Pro', 16, 'Apple M2', 'ordinateur_portable');

INSERT INTO Appareils
VALUES ("MG4HQ1", 1, 1);

INSERT INTO Appareils
VALUES ("ABC123", 2, 2);

INSERT INTO Appareils
VALUES ("ABC345", 2, 2);

INSERT INTO Evenements
VALUES (1, '2023-05-01', '14:00', '17:00' , 'Grenoble');

INSERT INTO Evenements
VALUES (2, '2023-01-01', '11:00', '15:00' , 'Paris');

INSERT INTO Evenements
VALUES (3, '2022-12-10', '08:00', '12:00' , 'Lyon');

INSERT INTO Reparations ('appareil_repare', 'evenement_reparation', 'prix_reparation', 'duree_reparation', 'description_reparation')
VALUES ("MG4HQ1", 1, 20, 20, 'Remplacement ram');

INSERT INTO Reparations ('appareil_repare', 'evenement_reparation', 'prix_reparation', 'duree_reparation', 'description_reparation')
VALUES ("ABC123", 1, 50, 30, 'Remplacement batterie');

INSERT INTO Reparations ('appareil_repare', 'evenement_reparation', 'prix_reparation', 'duree_reparation', 'description_reparation')
VALUES ("ABC123", 2, 100, 50, 'Remplacement écran');