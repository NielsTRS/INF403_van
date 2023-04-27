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
    print("1. On crée la bd et on l'initialise avec des premières valeurs.")
    db.mise_a_jour_bd(conn, "data/creation.sql")
    # db.mise_a_jour_bd(conn, "data/insert_nok.sql")
    db.mise_a_jour_bd(conn, "data/insert_ok.sql")

    # Lire la BD
    print("2. Liste de tous les clients")
    select_tous_les_clients(conn)

    # Union et Jointure
    select_union(conn)
    select_jointure(conn)

    #Execution requetes
    executer_requete(conn)

    #Fermeture de la connexion
    conn.close()


if __name__ == "__main__":
    main()
