from utils import db
import main


def menu_afficher_donnees():
    """
    Menu d'affichage des données

    """
    print("---- Menu affichage ----")
    print("1. Afficher une table")
    print("2. Afficher la liste des réparations")
    print("3. Afficher la liste des appareils n'ayant jamais eu de réparation")
    print("4. Afficher la liste de tous les appareils rassemblés par propriétaire")
    print("5. Afficher le nombre d'appareils de chaque personne")
    print("6. Afficher le nombre de réparation subis par chaque appareil")
    print("7. <- Retour")

    entree = input("Entrez votre choix : ")
    print("----")
    if entree == "1":
        afficher_tables()
    elif entree == "2":  # afficher la liste des réparations de smartphone
        afficher_reparations()
    elif entree == "3":
        commande = """WITH NonRepares AS (SELECT numeroDeSerie_appareil FROM Appareils A
                        EXCEPT 
                        SELECT appareil_repare AS numeroDeSerie_appareil FROM Reparations)
                        SELECT NR.numeroDeSerie_appareil, MA.marque_appareil, MA.modele_appareil FROM NonRepares NR JOIN Appareils A ON NR.numeroDeSerie_appareil = A.numeroDeSerie_appareil
                        JOIN ModeleAppareils MA ON A.numero_appareil = MA.numero_appareil;
                        """  # cette requete a été volontrairement compliquée pour utiliser "EXCEPT" comme opérateur ensembliste. Elle aurait pu être bien simplifiée
        execution = db.executer_commande_sql(commande)
        db.afficher_resultats(execution)
        menu_afficher_donnees()
    elif entree == "4":
        commande = """SELECT P.nom_personne, P.prenom_personne, A.numeroDeSerie_appareil, MA.marque_appareil, MA.modele_appareil FROM Personnes P
                        JOIN Appareils A ON P.numero_personne = A.proprietaire_appareil
                        JOIN ModeleAppareils MA ON A.numero_appareil = MA.numero_appareil
                        ORDER BY P.nom_personne;
                        """
                    # on affiche les appareils de chaque personne, en triant par nom de personne par ordre alphabétique
        execution = db.executer_commande_sql(commande)
        db.afficher_resultats(execution)
        menu_afficher_donnees()
    elif entree == "5":
        commande = """SELECT P.nom_personne, P.prenom_personne, P.email_personne, count(email_personne) AS nombreAppareils FROM Appareils A
                    JOIN Personnes P ON A.proprietaire_appareil = P.numero_personne 
                    GROUP BY email_personne;
                    """
                    # on compte le nombre d'appareils de chaque personne, et on affiche le résultat
        execution = db.executer_commande_sql(commande)
        db.afficher_resultats(execution)
        menu_afficher_donnees()
    elif entree == "6":
        commande = """SELECT A.numeroDeSerie_appareil, MA.marque_appareil, MA.modele_appareil, count(numeroDeSerie_appareil) AS nombreReparations FROM Appareils A
                    JOIN Reparations R ON A.numeroDeSerie_appareil = R.appareil_repare
                    JOIN ModeleAppareils MA ON A.numero_appareil = MA.numero_appareil
                    GROUP BY numeroDeSerie_appareil
                    UNION
                    SELECT A.numeroDeSerie_appareil, MA.marque_appareil, MA.modele_appareil, 0 AS nombreReparations  FROM Appareils A
                    JOIN ModeleAppareils MA USING (numero_appareil)
                    WHERE A.numeroDeSerie_appareil NOT IN (SELECT appareil_repare FROM Reparations)
                    ORDER BY nombreReparations DESC;
                    """ #on recupere les appareils ayant subi des reparations, et on ajoute les appareils n'ayant jamais subi de reparations, puis on trie par ordre décroissant du nombre de reparations
        execution = db.executer_commande_sql(commande)
        db.afficher_resultats(execution)
        menu_afficher_donnees()
    elif entree == "7": #retour au menu principal
        main.menu_principal()
    else:
        print("Entrée invalide")
        menu_afficher_donnees()

def afficher_tables():
    """
    Affiche la liste des tables de la base de données

    """
    tables = ["Reparations", "Evenements", "Appareils", "ModeleAppareils", "Personnes"]
    for (i, table) in enumerate(tables):
        print(i, ":", table)
    entree = input("Nom de la table à afficher : ")
    if entree in ["0", "1", "2", "3", "4"]:  # l'utilisateur a choisi une table qui existe
        commande = "SELECT * FROM " + tables[int(entree)] + ";"
        execution = db.executer_commande_sql(commande)
        db.afficher_resultats(execution)
        menu_afficher_donnees()
    else:  # l'utilisateur a choisi une table qui n'existe pas
        print("Entrée invalide")
        afficher_tables()


def afficher_reparations():
    """
    Permet l'affiche des réparations, avec possibilité de filtrer par type d'appareil
    """
    print("Afficher les réparations de : ")
    types = ["smartphone", "tablette", "ordinateur_portable", "ordinateur_bureau", "toutes les réparations"]
    for (i, type) in enumerate(types):
        print(i, ":", type)
    entree = input("Entrez votre choix : ")
    if entree in ["0", "1", "2", "3"]:
        commande = """SELECT * FROM Reparations_view
        WHERE type_appareil = '""" + types[int(entree)] + "';"
        execution = db.executer_commande_sql( commande)
        db.afficher_resultats(execution)
    elif entree == "4":
        commande = """SELECT * FROM Reparations_view"""
        execution = db.executer_commande_sql(commande)
        db.afficher_resultats(execution)
    else:
        print("Entrée incorrecte")
        afficher_reparations()
    menu_afficher_donnees()