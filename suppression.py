from utils import db
import main
from utils import const
def menu_supprimer_donnees():
    """
    Menu de suppression des données

    """
    print("---- Menu suppression ----")
    print("1. Supprimer une personne")
    print("2. Supprimer un appareil")
    print("3. Supprimer une réparation")
    print("4. Supprimer un évènement")
    print("5. Supprimer un modèle d'appareil")
    print("6. <- Retour")

    entree = input("Entrez votre choix : ")
    print("----")
    if(entree == "1"):
        supprimer_entree( "Personnes")
    elif(entree == "2"):
        supprimer_entree( "Appareils")
    elif(entree == "3"):
        supprimer_entree( "Reparations")
    elif(entree == "4"):
        supprimer_entree( "Evenements")
    elif(entree == "5"):
        supprimer_entree( "ModeleAppareils")
    elif(entree == "6"):
        main.menu_principal()
    else:
        print("Choix invalide")
        menu_supprimer_donnees()

def supprimer_entree( table):
    """
    Permet le choix d'une ligne à supprimer dans une table, ainsi que la suppression de cette ligne

    """
    commande = "SELECT * FROM " + table + ";"
    execution = db.executer_commande_sql( commande)
    if(len(execution) == 0):
        print("Il n'y a rien à supprimer")
        menu_supprimer_donnees()
        return
    db.afficher_resultats(execution)
    aSupprimer = input("Entrez le numéro " +  printDeSerie(table) + const.getSingularTableName(table) +" à supprimer : ")
    # on verifie que la ligne a supprimer existe
    if(table == "Appareils"):
        while not const.verifierSiColonneExiste(aSupprimer, execution):
            aSupprimer = input("Ce numéro de série n'existe pas, veuillez entrer un modèle valide : ")
    else:
        while not const.verifierSiColonneExiste(aSupprimer, execution):
            aSupprimer = input("Ce numéro n'existe pas, veuillez entrer un modèle valide : ")
    commande = "DELETE FROM " + table + " WHERE " + const.getPrimaryKey(table) +" = '" + aSupprimer + "';"
    if(table =="Personnes"):
        print("Attention la suppression d'une personne entraine la suppression de tous ses appareils ainsi que les réparations associées à ces appareils")
    if(table =="Appareils"):
        print("Attention la suppression d'un appareil entraine la suppression de toutes les réparations associées à cet appareil")
    if(table =="Evenements"):
        print("Attention la suppression d'un évènement entraine la suppression de toutes les réparations associées à cet évènement")
    if(table == "ModeleAppareils"):
        print("Attention la suppression d'un modèle entraine la suppression de tous les appareils associés à ce modèle ainsi que les réparations associées à ces appareils")
    entree = input("Confirmer la suppression ? (y/n) : ")
    if(entree == "y"):
        pass
    elif(entree == "n"):
        menu_supprimer_donnees()
        return
    else:
        print("Choix invalide")
        menu_supprimer_donnees()
        return
    try:
        execution = db.executer_commande_sql( commande)
        db.afficher_resultats(execution)
    except Exception as e:
        print("Erreur impossible de supprimer :", e)
    menu_supprimer_donnees()

def printDeSerie(table):
    if table == "Appareils":
        return "de série "
    else:
        return ""

