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

    if(entree == "1"):
        executer_requete(conn)
    elif(entree == "2"):
        menu_afficher_donnees(conn)
    elif(entree == "3"):
        menu_modifier_donnees(conn)
    elif(entree == "4"):
        menu_supprimer_donnees(conn)
    elif(entree == "5"):
        exit()
    else:
        print("Choix invalide")


def menu_afficher_donnees(conn):
    """
    Menu d'affichage des données

    :param conn: Connexion à la base de données
    """
    print("La fonction d'affichage des données est à implémenter")

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
        for row in rows:
            print(row)
        conn.commit()
    except:
        print("La requête n'est pas valide")
        executer_requete(conn)

    reesayer = input("Souhaitez vous faire une autre requête ? (Y/N) : ")
    if(reesayer == "Y" or reesayer == "y"):
        executer_requete(conn)




def select_tous_les_clients(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    cur = conn.cursor()
    cur.execute("""
                SELECT * 
                FROM Personnes
                """)

    rows = cur.fetchall()

    for row in rows:
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
    #Fichier incorrect
    print("Insertion d'un fichier de donnés erroné : ", end="")
    db.mise_a_jour_bd(conn, "data/insert_nok.sql")
    #On vide la base de données pour supprimer certaines entrées du fichier incorrect
    db.vider_base(conn)
    #Fichier correct
    print("Insertion d'un fichier de donnés correct : ", end="")
    db.mise_a_jour_bd(conn, "data/insert_ok.sql")


    # Afficher le menu
    while True:
        menu_principal(conn)

    #Fermeture de la connexion
    conn.close()


if __name__ == "__main__":
    main()
