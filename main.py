#!/usr/bin/python3

from utils import db


def menu_principal(conn):
    """
    Menu principal du programme

    :param conn: Connexion à la base de données
    """
    print("---- Menu ----")
    print("1. Effectuer une requête SQL à la main")
    print("2. Afficher des données")
    print("3. Modifier des données")
    print("4. Supprimer des données")
    print("5. Quitter le programme")

    entree = input("Entrez votre choix : ")
    print("----")

    if (entree == "1"):
        executer_requete(conn)
    elif (entree == "2"):
        menu_afficher_donnees(conn)
    elif (entree == "3"):
        menu_modifier_donnees(conn)
    elif (entree == "4"):
        select_tous_les_clients(conn)
        #menu_supprimer_donnees(conn)
    elif (entree == "5"):
        exit()
    else:
        print("Choix invalide")


def menu_afficher_donnees(conn):
    """
    Menu d'affichage des données

    :param conn: Connexion à la base de données
    """
    print("---- Menu affichage ----")
    print("1. Afficher une table")
    print("2. Afficher la liste des réparations")
    print("3. <- Retour")

    entree = input("Entrez votre choix : ")
    print("----")
    if(entree == "1"):
        afficher_tables(conn)
    elif(entree == "2"):       #afficher la liste des réparations de smartphone
        afficher_reparations(conn)
    elif(entree == "3"):
        menu_principal(conn)
    else:
        print("Entrée invalide")
        menu_afficher_donnees(conn)


def afficher_tables(conn):
    """
    Affiche la liste des tables de la base de données

    :param conn: Connexion à la base de données
    """
    tables = ["Reparations", "Evenements","Appareils", "ModeleAppareils", "Personnes"]
    for (i,table) in enumerate(tables):
        print(i,":", table)
    entree = input("Nom de la table à afficher : ")
    if(entree in ["0", "1", "2", "3", "4"]):  #l'utilisateur a choisi une table qui existe
        commande = "SELECT * FROM " + tables[int(entree)] + ";"
        execution = db.executer_commande_sql(conn, commande)
        db.afficher_resultats(execution)
        menu_afficher_donnees(conn)
    else:           # l'utilisateur a choisi une table qui n'existe pas
        print("Entrée invalide")
        afficher_tables(conn)


def afficher_reparations(conn):
    """
    Permet l'affiche des réparations, avec possibilité de filtrer par type d'appareil

    :param conn : Connexion à la base de données
    """
    print("Afficher les réparations de : ")
    types = ["smartphone", "tablette", "ordinateur_portable", "ordinateur_bureau", "toutes les réparations"]
    for (i, type) in enumerate(types):
        print(i, ":", type)
    entree = input("Entrez votre choix : ")
    if(entree in ["0", "1", "2", "3"]):
        commande = """SELECT appareil_repare AS numeroDeSerie, prix_reparation, duree_reparation, description_reparation, marque_appareil, modele_appareil FROM Reparations R 
        JOIN Appareils A ON R.appareil_repare = A.numeroDeSerie_appareil 
        JOIN ModeleAppareils M USING(numero_appareil)
        WHERE type_appareil = '""" + types[int(entree)] + "';"
        execution = db.executer_commande_sql(conn, commande)
        db.afficher_resultats(execution)
    elif(entree == "4"):
        commande = """SELECT appareil_repare AS numeroDeSerie, prix_reparation, duree_reparation, description_reparation, marque_appareil, modele_appareil, type_appareil FROM Reparations R 
        JOIN Appareils A ON R.appareil_repare = A.numeroDeSerie_appareil 
        JOIN ModeleAppareils M USING(numero_appareil);"""
        execution = db.executer_commande_sql(conn, commande)
        db.afficher_resultats(execution)
    else:
        print("Entrée incorrecte")
        afficher_reparations(conn)
    menu_afficher_donnees(conn)



def menu_modifier_donnees(conn):
    """
    Menu de modification des données

    :param conn: Connexion à la base de données
    """
    print("La fonction de modification des données est à implémenter")


def menu_supprimer_donnees(conn):
    """
    Menu de suppression des données

    :param conn: Connexion à la base de données
    """
    print("La fonction de suppression des données est à implémenter")


def executer_requete(conn):
    requete = input('Entrez une requête SQL : ')

    cur = conn.cursor()
    try:
        cur.execute(requete)
        rows = cur.fetchall()
        db.afficher_resultats(rows)
        conn.commit()
        reesayer = input("Souhaitez vous faire une autre requête ? (Y/N) : ")
        if (reesayer == "Y" or reesayer == "y"):
            executer_requete(conn)
    except:
        print("La requête n'est pas valide")
        executer_requete(conn)


def select_tous_les_clients(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    commande = "SELECT * FROM Reparations WHERE duree_reparation = 'sma';"
    execution = db.executer_commande_sql(conn, commande)
    for row in execution:
        print(row)


def select_union(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def select_jointure(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * FROM 
                Personnes P
                JOIN Appareils A JOIN ModeleAppareils M
                ON (P.numero_personne = A.proprietaire_appareil AND A.numero_appareil = M.numero_appareil)
                """)

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    # Nom de la BD à créer
    db_file = "data/van.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)

    # Remplir la BD
    print("Création la bd : ", end="")
    db.mise_a_jour_bd(conn, "data/creation.sql")
    # Fichier incorrect
    print("Insertion d'un fichier de donnés erroné : ", end="")
    db.mise_a_jour_bd(conn, "data/insert_nok.sql")
    # On vide la base de données pour supprimer certaines entrées du fichier incorrect
    db.vider_base(conn)
    # Fichier correct
    print("Insertion d'un fichier de donnés correct : ", end="")
    db.mise_a_jour_bd(conn, "data/insert_ok.sql")

    # Afficher le menu
    while True:
        menu_principal(conn)

    # Fermeture de la connexion
    conn.close()


if __name__ == "__main__":
    main()
