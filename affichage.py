from utils import db
import main


def menu_afficher_donnees():
    """
    Menu d'affichage des données

    """
    print("---- Menu affichage ----")
    print("1. Afficher une table")
    print("2. Afficher la liste des réparations")
    print("3. <- Retour")

    entree = input("Entrez votre choix : ")
    print("----")
    if entree == "1":
        afficher_tables()
    elif entree == "2":  # afficher la liste des réparations de smartphone
        afficher_reparations()
    elif entree == "3":
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