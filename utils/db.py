import sqlite3


def creer_connexion(db_file):
    """Crée une connexion a la base de données SQLite spécifiée par db_file

    :param db_file: Chemin d'accès au fichier SQLite
    :return: Objet connexion ou None
    """

    try:
        conn = sqlite3.connect(db_file)
        # On active les foreign keys
        conn.execute("PRAGMA foreign_keys = 1")
        return conn
    except sqlite3.Error as e:
        print(e)

    return None


def mise_a_jour_bd(conn: sqlite3.Connection, file: str):
    """Exécute sur la base de données toutes les commandes contenues dans le
    fichier fourni en argument.

    Les commandes dans le fichier `file` doivent être séparées par un
    point-virgule.

    :param conn: Connexion à la base de données
    :type conn: sqlite3.Connection
    :param file: Chemin d'accès au fichier contenant les requêtes
    :type file: str
    """
    # Lecture du fichier et placement des requêtes dans un tableau
    sqlQueries = []

    with open(file, 'r') as f:
        createSql = f.read()
        sqlQueries = createSql.split(";")

    # Exécution de toutes les requêtes du tableau
    cursor = conn.cursor()
    try:
        for query in sqlQueries:
            cursor.execute(query)
        print("OK")
    except sqlite3.Error as e:
        print("PAS OK", e)
    # Validation des modifications
    conn.commit()


def executer_commande_sql(conn: sqlite3.Connection, commande: str) -> list:
    """
    Exécute une commande SQL et retourne le résultat sous forme de liste (pour un SELECT par exemple)

    :param commande: Commande SQL à exécuter
    :return: Liste des réultats de la commande
    """
    cursor = conn.cursor()
    cur = cursor.execute(commande)
    execution = cur.fetchall()
    if (len(execution) == 0):  # la requête ne renvoie aucun retour
        commandeSplit = commande.split(" ")
        if (commandeSplit[
            0].capitalize() == "Select"):  # si il s'agit d'une requete select qui ne renvoie aucune donnée
            print("Aucune donnée ne correspond à la requête")
            return []
        print(
            "La commande a été effectuée avec succès")  # si c'est INSERT INTO, DELETE ou UPDATE, alors il n'y a pas de retour
        return []
    else:  # si c'est une requête SELECT on renvoie les données
        colonnes = cur.description
        colonnesInsert = []
        for col in colonnes:
            colonnesInsert.append(col[0])
        tupleInsert = tuple(colonnesInsert)
        execution.insert(0, tupleInsert)
        return execution


def vider_base(conn: sqlite3.Connection):
    """
    Permet de vider la base de donnée initalisée

    :param conn: Connexion à la base de données
    """
    tables = ["Personnes", "ModeleAppareils", "Appareils", "Evenements", "Reparations"]
    cursor = conn.cursor()
    for table in tables:
        cursor.execute("DELETE FROM " + table)
    conn.commit()


def afficher_resultats(resultats: list):
    for row in resultats:
        # print('%-25s' % 'Desc', 'Test')
        for enr in row:
            print('%-20s' % enr, end="")
        print("")
