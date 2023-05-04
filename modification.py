from utils import db, const
import main


def menu_modifier_donnees():
    """
    Menu de modification des données
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
        modifier_personne()
    elif entree == "2":
        modifier_appareil()
    elif entree == "3":
        modifier_modele()
    elif entree == "4":
        modifier_reparation()
    elif entree == "5":
        modifier_evenement()
    elif entree == "6":
        main.menu_principal()
    else:
        print("Choix invalide")
        menu_modifier_donnees()


def modifier_personne():
    """
    Fonction qui permet de modifier un champ d'une personne
    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM Personnes;"
    personnes = db.executer_commande_sql(commande)
    db.afficher_resultats(personnes)
    # on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro de la personne à modifier : ")
    while not const.verifierSiColonneExiste(entreeP, personnes):  # on verifie que le numero existe bien
        print("Le numéro entré n'existe pas")
        entreeP = input("Entrez le numéro de la personne à modifier : ")
    # on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Nom")
    print("2. Prénom")
    print("3. Email")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3":  # on verifie que le choix est valide
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
        db.executer_commande_sql(commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees()


def modifier_appareil():
    """
    Fonction qui permet de modifier un champ d'un appareil
    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM Appareils;"
    execution = db.executer_commande_sql(commande)
    db.afficher_resultats(execution)
    # on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro de série de l'appareil à modifier : ")
    while not const.verifierSiColonneExiste(entreeP, execution):  # on verifie que le numero existe bien
        print("Le numéro de série entré n'existe pas")
        entreeP = input("Entrez le numéro de série de l'appareil à modifier : ")
    # on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Numéro de série")
    print("2. Modèle")
    print("3. Propriétaire")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3":  # on verifie que le choix est valide
        print("Choix invalide")
        entree = input("Entrez votre choix : ")
    if entree == "1":
        numeroSerie = input("Entrez le nouveau numéro de série : ")
        commande = "UPDATE Appareils SET numeroDeSerie_appareil = '" + numeroSerie + "' WHERE numeroDeSerie_appareil = '" + entreeP + "';"
    elif entree == "2":
        commande = "SELECT * FROM ModeleAppareils;"
        modeles = db.executer_commande_sql(commande)
        db.afficher_resultats(modeles)
        modele = input("Entrez le nouveau modèle : ")
        while not const.verifierSiColonneExiste(modele, modeles):
            print("Le modèle entré n'existe pas")
            modele = input("Entrez le nouveau modèle : ")
        commande = "UPDATE Appareils SET numero_appareil = " + modele + " WHERE numeroDeSerie_appareil = '" + entreeP + "';"
    elif entree == "3":
        commande = "SELECT * FROM Personnes;"
        personnes = db.executer_commande_sql(commande)
        db.afficher_resultats(personnes)
        proprietaire = input("Entrez le nouveau propriétaire : ")
        while not const.verifierSiColonneExiste(proprietaire, personnes):
            print("Le propriétaire entré n'existe pas")
            proprietaire = input("Entrez le nouveau propriétaire : ")
        commande = "UPDATE Appareils SET proprietaire_appareil = " + proprietaire + " WHERE numeroDeSerie_appareil = '" + entreeP + "';"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees()


def modifier_modele():
    """
    Fonction qui permet de modifier un champ d'un modèle d'appareil

    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM ModeleAppareils;"
    execution = db.executer_commande_sql(commande)
    db.afficher_resultats(execution)
    # on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro du modèle à modifier : ")
    while not const.verifierSiColonneExiste(entreeP, execution):  # on verifie que le numero existe bien
        print("Le numéro entré n'existe pas")
        entreeP = input("Entrez le numéro du modèle à modifier : ")
    # on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Marque")
    print("2. Modèle")
    print("3. Ram")
    print("4. Processeur")
    print("5. Type appareil")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3" and entree != "4" and entree != "5":  # on verifie que le choix est valide
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
        while not const.entreeEstEntier(ram):
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
        while not (const.entreeEstEntier(typeAppareil) and 0 <= int(typeAppareil) < len(type)):
            print("Le type d'appareil n'existe pas, veuillez en choisir un dans la liste")
            typeAppareil = input("Entrez le type d'appareil : ")
        commande = "UPDATE ModeleAppareils SET type_appareil = '" + type[
            int(typeAppareil)] + "' WHERE numero_appareil = " + entreeP + ";"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees()


def modifier_reparation():
    """
    Fonction qui permet de modifier un champ d'une réparation

    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM Reparations;"
    execution = db.executer_commande_sql(commande)
    db.afficher_resultats(execution)
    # on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro de la réparation à modifier : ")
    while not const.verifierSiColonneExiste(entreeP, execution):  # on verifie que le numero existe bien
        print("Le numéro entré n'existe pas")
        entreeP = input("Entrez le numéro du modèle de la réparation : ")
    # on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Appareil réparé")
    print("2. Evènement (lors duquel la réparation a eu lieu)")
    print("3. Prix de la réparation")
    print("4. Durée de la réparation")
    print("5. Description de la réparation")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3" and entree != "4" and entree != "5":  # on verifie que le choix est valide
        print("Choix invalide")
        entree = input("Entrez votre choix : ")
    if entree == "1":
        commande = "SELECT * FROM Appareils;"
        appareils = db.executer_commande_sql(commande)
        db.afficher_resultats(appareils)
        appareilSel = input("Entrez le numéro de série du nouvel appareil : ")
        while not const.verifierSiColonneExiste(appareilSel, appareils):
            print("Le numéro de série entré n'existe pas")
            appareilSel = input("Entrez le numéro de série du nouvel appareil : ")
        commande = "UPDATE Reparations SET appareil_repare = '" + appareilSel + "' WHERE numero_reparation = " + entreeP + ";"
    elif entree == "2":
        commande = "SELECT * FROM Evenements;"
        evenements = db.executer_commande_sql(commande)
        db.afficher_resultats(evenements)
        evenementSel = input("Entrez le numéro de l'évènement : ")
        while not const.verifierSiColonneExiste(evenementSel, evenements):
            print("Le numéro de l'évènement entré n'existe pas")
            evenementSel = input("Entrez le numéro de l'évènement : ")
        commande = "UPDATE Reparations SET evenement_reparation = " + evenementSel + " WHERE numero_reparation = " + entreeP + ";"
    elif entree == "3":
        prix = input("Entrez le nouveau prix : ")
        while not const.entreeEstEntier(prix):
            print("Le prix doit être un entier positif")
            prix = input("Entrez le nouveau prix : ")
        commande = "UPDATE Reparations SET prix_reparation = " + prix + " WHERE numero_reparation = " + entreeP + ";"
    elif entree == "4":
        duree = input("Entrez la nouvelle durée (en min) : ")
        while not const.entreeEstEntier(duree):
            print("La durée doit être un entier positif")
            duree = input("Entrez la nouvelle durée : ")
        commande = "UPDATE Reparations SET duree_reparation = " + duree + " WHERE numero_reparation = " + entreeP + ";"
    elif entree == "5":
        description = input("Entrez la nouvelle description : ")
        commande = "UPDATE Reparations SET description_reparation = '" + description + "' WHERE numero_reparation = " + entreeP + ";"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees()


def modifier_evenement():
    """
    Fonction qui permet de modifier un champ d'un évènement

    """
    # on recupere d'abord déjà la liste des personnes pour choisir laquelle on veut modifier
    commande = "SELECT * FROM Evenements;"
    execution = db.executer_commande_sql(commande)
    db.afficher_resultats(execution)
    # on recupere ensuite le numero de la personne à modifier
    entreeP = input("Entrez le numéro de l'évènement à modifier : ")
    while not const.verifierSiColonneExiste(entreeP, execution):  # on verifie que le numero existe bien
        print("Le numéro entré n'existe pas")
        entreeP = input("Entrez le numéro de l'évènement à modifier : ")
    # on recupere ensuite le champ à modifier
    print("Quel champ voulez-vous modifier ?")
    print("1. Date de l'évènement")
    print("2. Heure de début de l'évènement")
    print("3. Heure de fin de l'évènement")
    print("4. Ville de l'évènement")
    entree = input("Entrez votre choix : ")
    while entree != "1" and entree != "2" and entree != "3" and entree != "4":  # on verifie que le choix est valide
        print("Choix invalide")
        entree = input("Entrez votre choix : ")
    if entree == "1":
        date = input("Entrez la nouvelle date (au format YYYY-MM-DD) : ")
        while not const.entreeEstDate(date):
            print("La date doit être au format YYYY-MM-DD")
            date = input("Entrez la nouvelle date : ")
        commande = "UPDATE Evenements SET date_evenement = '" + date + "' WHERE numero_evenement = " + entreeP + ";"
    elif entree == "2":
        heureDebut = input("Entrez la nouvelle heure de début (au format HH:MM) : ")
        while not const.entreeEstHeure(heureDebut):
            print("L'heure doit être au format HH:MM")
            heureDebut = input("Entrez la nouvelle heure de début : ")
        commande = "UPDATE Evenements SET heureDebut_evenement = '" + heureDebut + "' WHERE numero_evenement = " + entreeP + ";"
    elif entree == "3":
        heureFin = input("Entrez la nouvelle heure de fin (au format HH:MM) : ")
        while not const.entreeEstHeure(heureFin):
            print("L'heure doit être au format HH:MM")
            heureFin = input("Entrez la nouvelle heure de fin : ")
        commande = "UPDATE Evenements SET heureFin_evenement = '" + heureFin + "' WHERE numero_evenement = " + entreeP + ";"
    elif entree == "4":
        ville = input("Entrez la nouvelle ville : ")
        commande = "UPDATE Evenements SET ville_evenement = '" + ville + "' WHERE numero_evenement = " + entreeP + ";"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        print("Erreur lors de la modification", e)
    menu_modifier_donnees()
