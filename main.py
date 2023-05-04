#!/usr/bin/python3

from utils import db
import affichage
import suppression
import modification
import ajout


def menu_principal(conn):
    """
    Menu principal du programme

    :param conn: Connexion à la base de données
    """
    print("---- Menu principal ----")
    print("1. Effectuer une requête SQL à la main")
    print("2. Afficher des données")
    print("3. Modifier des données")
    print("4. Supprimer des données")
    print("5. Ajouter des données")
    print("6. Quitter le programme")

    entree = input("Entrez votre choix : ")
    print("----")

    if entree == "1":
        executer_requete(conn)
    elif entree == "2":
        affichage.menu_afficher_donnees(conn)
    elif entree == "3":
        modification.menu_modifier_donnees(conn)
    elif entree == "4":
        suppression.menu_supprimer_donnees(conn)
    elif entree == "5":
        ajout.menu_ajouter_donnees(conn)
    elif entree == "6":
        # Fermeture de la connexion
        conn.close()
        exit()
    else:
        print("Choix invalide")

def executer_requete(conn):
    requete = input('Entrez une requête SQL : ')

    cur = conn.cursor()
    try:
        cur.execute(requete)
        rows = cur.fetchall()
        db.afficher_resultats(rows)
        conn.commit()
        reesayer = input("Souhaitez vous faire une autre requête ? (Y/N) : ")
        if reesayer == "Y" or reesayer == "y":
            executer_requete(conn)
    except:
        print("La requête n'est pas valide")
        executer_requete(conn)


def select_tous_les_clients(conn):
    """
    Affiche la liste de tous les bateaux.

    :param conn: Connexion à la base de données
    """
    commande = "SELECT * FROM Personnes;"
    execution = db.executer_commande_sql(conn, commande)
    for row in execution:
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


if __name__ == "__main__":
    main()
