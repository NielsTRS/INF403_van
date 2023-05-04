from utils import db
import main
from utils import const


def menu_supprimer_donnees(conn):
    """
    Menu de suppression des données

    :param conn: Connexion à la base de données
    """
    print("---- Menu suppression ----")
    print("1. Supprimer une personne")
    print("2. Supprimer un appareil")
    print("3. Supprimer une réparation")
    print("4. Supprimer un évènement")
    print("5. <- Retour")

    entree = input("Entrez votre choix : ")
    print("----")
    if(entree == "1"):
        supprimer_entree(conn, "Personnes")
    elif(entree == "2"):
        supprimer_entree(conn, "Appareils")
    elif(entree == "3"):
        supprimer_entree(conn, "Reparations")
    elif(entree == "4"):
        supprimer_entree(conn, "Evenements")
    elif(entree == "5"):
        main.menu_principal(conn)
    else:
        print("Choix invalide")
        menu_supprimer_donnees(conn)

def supprimer_entree(conn, table):
    """
    Permet le choix d'une ligne à supprimer dans une table, ainsi que la suppression de cette ligne

    :param conn: Connexion à la base de données
    """
    commande = "SELECT * FROM " + table + ";"
    execution = db.executer_commande_sql(conn, commande)
    db.afficher_resultats(execution)
    aSupprimer = input("Entrez le numéro " +  printDeSerie(table) + const.getSingularTableName(table) +" à supprimer : ")
    commande = "DELETE FROM " + table + " WHERE " + const.getPrimaryKey(table) +" = '" + aSupprimer + "';"
    if(table =="Personnes"):
        print("Attention la suppression d'une personne entraine la suppression de tous ses appareils ainsi que les réparations associées à ces appareils")
    if(table =="Appareils"):
        print("Attention la suppression d'un appareil entraine la suppression de toutes les réparations associées à cet appareil")
    if(table =="Evenements"):
        print("Attention la suppression d'un évènement entraine la suppression de toutes les réparations associées à cet évènement")
    entree = input("Confirmer la suppression ? (y/n) : ")
    if(entree == "y"):
        pass
    elif(entree == "n"):
        menu_supprimer_donnees(conn)
        return
    else:
        print("Choix invalide")
        menu_supprimer_donnees(conn)
        return
    try:
        execution = db.executer_commande_sql(conn, commande)
        db.afficher_resultats(execution)
    except Exception as e:
        print("Erreur impossible de supprimer :", e)
    menu_supprimer_donnees(conn)

def printDeSerie(table):
    if table == "Appareils":
        return "de série "
    else:
        return ""

