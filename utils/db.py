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


def vider_base(conn : sqlite3.Connection):
    """
    Permet de vider la base de donnée initalisée

    :param conn: Connexion à la base de données
    """
    tables = ["Personnes", "ModeleAppareils", "Appareils", "Evenements", "Reparations"]
    cursor = conn.cursor()
    for table in tables:
        cursor.execute("DELETE FROM " + table)
    conn.commit()


