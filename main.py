#!/usr/bin/python3

from utils import db


def executer_requete(conn):
    requetes = input('Entrez une ou plusieurs requetes :')
    requetes = requetes.split(";")

    cur = conn.cursor()
    for requete in requetes:
        cur.execute(requete)
        rows = cur.fetchall()
        for row in rows:
            print(row)

    conn.commit()


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


def main():
    # Nom de la BD à créer
    db_file = "data/van.db"

    # Créer une connexion a la BD
    conn = db.creer_connexion(db_file)
    # Remplir la BD
    print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, "data/creation.sql")
    # db.mise_a_jour_bd(conn, "data/insert_nok.sql")
    db.mise_a_jour_bd(conn, "data/insert_ok.sql")

    # Lire la BD
    print("2. Liste de tous les clients")
    select_tous_les_clients(conn)

    # test
    executer_requete(conn)


if __name__ == "__main__":
    main()
