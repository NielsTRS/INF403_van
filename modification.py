from utils import db
import main
import ajout

def menu_modifier_donnees(conn):
    """
    Menu de modification des données

    :param conn: Connexion à la base de données
    """
    print("1. Modifier une personne")
    print("2. Modifier un appareil")
    print("3. Modifier un modèle d'appareil")
    print("4. Modifier une réparation")
    print("5. Modifier un évènement")
    print("6. <- Retour")
    entree = input("Entrez votre choix : ")
    print("---")
    if entree == "1":
        modifier_personne(conn)
    elif entree == "2":
        modifier_appareil(conn)
    elif entree == "3":
        modifier_modele(conn)
    elif entree == "4":
        modifier_reparation(conn)
    elif entree == "5":
        modifier_evenement(conn)
    elif entree == "6":
        main.menu_principal(conn)
    else:
        print("Choix invalide")
        menu_modifier_donnees(conn)

def modifier_personne(conn):
    """
    Fonction qui permet de modifier un champ d'une personne

    :param conn: Connexion à la base de données
    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM Personnes;"
    personnes = db.executer_commande_sql(conn, commande)
    db.afficher_resultats(personnes)
    #on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro de la personne à modifier : ")
    while not ajout.verifierSiColonneExiste(int(entreeP), personnes):    #on verifie que le numero existe bien
        print("Le numéro entré n'existe pas")
        entreeP = input("Entrez le numéro de la personne à modifier : ")
    #on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Nom")
    print("2. Prénom")
    print("3. Email")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3":    #on verifie que le choix est valide
        print("Choix invalide")
        entree = input("Entrez votre choix : ")
    if entree == "1":
        nom = input("Entrez le nouveau nom : ")
        commande = "UPDATE Personnes SET nom_personne = '" + nom + "' WHERE numero_personne = " + entreeP + ";"
    elif entree == "2":
        prenom = input("Entrez le nouveau prénom : ")
        commande = "UPDATE Personnes SET prenom_personne = '" + prenom + "' WHERE numero_personne = " + entreeP + ";"
    elif entree == "3":
        email = input("Entrez le nouvel email : ")
        commande = "UPDATE Personnes SET email_personne = '" + email + "' WHERE numero_personne = " + entreeP + ";"
    try:
        db.executer_commande_sql(conn, commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees(conn)

def modifier_appareil(conn):
    """
    Fonction qui permet de modifier un champ d'un appareil

    :param conn: Connexion à la base de données
    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM Appareils;"
    execution = db.executer_commande_sql(conn, commande)
    db.afficher_resultats(execution)
    #on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro de série de l'appareil à modifier : ")
    while not ajout.verifierSiColonneExiste(entreeP, execution):    #on verifie que le numero existe bien
        print("Le numéro de série entré n'existe pas")
        entreeP = input("Entrez le numéro de série de l'appareil à modifier : ")
    #on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Numéro de série")
    print("2. Modèle")
    print("3. Propriétaire")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3":    #on verifie que le choix est valide
        print("Choix invalide")
        entree = input("Entrez votre choix : ")
    if entree == "1":
        numeroSerie = input("Entrez le nouveau numéro de série : ")
        commande = "UPDATE Appareils SET numeroDeSerie_appareil = '" + numeroSerie + "' WHERE numeroDeSerie_appareil = '" + entreeP + "';"
    elif entree == "2":
        commande = "SELECT * FROM ModeleAppareils;"
        modeles = db.executer_commande_sql(conn, commande)
        db.afficher_resultats(modeles)
        modele = input("Entrez le nouveau modèle : ")
        while not ajout.verifierSiColonneExiste(int(modele), modeles):
            print("Le modèle entré n'existe pas")
            modele = input("Entrez le nouveau modèle : ")
        commande = "UPDATE Appareils SET numero_appareil = " + modele + " WHERE numeroDeSerie_appareil = '" + entreeP + "';"
    elif entree == "3":
        commande = "SELECT * FROM Personnes;"
        personnes = db.executer_commande_sql(conn, commande)
        db.afficher_resultats(personnes)
        proprietaire = input("Entrez le nouveau propriétaire : ")
        while not ajout.verifierSiColonneExiste(int(proprietaire), personnes):
            print("Le propriétaire entré n'existe pas")
            proprietaire = input("Entrez le nouveau propriétaire : ")
        commande = "UPDATE Appareils SET proprietaire_appareil = " + proprietaire + " WHERE numeroDeSerie_appareil = '" + entreeP + "';"
    try:
        db.executer_commande_sql(conn, commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees(conn)


def modifier_modele(conn):
    """
    Fonction qui permet de modifier un champ d'un modèle d'appareil

    :param conn: Connexion à la base de données
    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM ModeleAppareils;"
    execution = db.executer_commande_sql(conn, commande)
    db.afficher_resultats(execution)
    #on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro du modèle à modifier : ")
    while not ajout.verifierSiColonneExiste(int(entreeP), execution):    #on verifie que le numero existe bien
        print("Le numéro entré n'existe pas")
        entreeP = input("Entrez le numéro du modèle à modifier : ")
    #on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Marque")
    print("2. Modèle")
    print("3. Ram")
    print("4. Processeur")
    print("5. Type appareil")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3" and entree != "4" and entree != "5":    #on verifie que le choix est valide
        print("Choix invalide")
        entree = input("Entrez votre choix : ")
    if entree == "1":
        marque = input("Entrez la nouvelle marque : ")
        commande = "UPDATE ModeleAppareils SET marque_appareil = '" + marque + "' WHERE numero_appareil = " + entreeP + ";"
    elif entree == "2":
        modele = input("Entrez le nouveau modèle : ")
        commande = "UPDATE ModeleAppareils SET modele_appareil = '" + modele + "' WHERE numero_appareil = " + entreeP + ";"
    elif entree == "3":
        ram = input("Entrez la nouvelle ram : ")
        while not ajout.entreeEstEntier(ram):
            print("La quantité de RAM doit être un entier positif")
            ram = input("Entrez la quantité de RAM (en Go): ")
        commande = "UPDATE ModeleAppareils SET ram_appareil = " + ram + " WHERE numero_appareil = " + entreeP + ";"
    elif entree == "4":
        processeur = input("Entrez le nouveau processeur : ")
        commande = "UPDATE ModeleAppareils SET processeur_appareil = '" + processeur + "' WHERE numero_appareil = " + entreeP + ";"
    elif entree == "5":
        type = ["smartphone", "tablette", "ordinateur_portable", "ordinateur_bureau"]
        for i in range(len(type)):
            print(str(i) + ". " + type[i])
        typeAppareil = input("Entrez le nouveau type d'appareil : ")
        while not (ajout.entreeEstEntier(typeAppareil) and int(typeAppareil) >= 0 and  int(typeAppareil) < len(type)):
            print("Le type d'appareil n'existe pas, veuillez en choisir un dans la liste")
            typeAppareil = input("Entrez le type d'appareil : ")
        commande = "UPDATE ModeleAppareils SET type_appareil = '" + type[int(typeAppareil)] + "' WHERE numero_appareil = " + entreeP + ";"
    try:
        db.executer_commande_sql(conn, commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees(conn)

    