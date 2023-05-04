from utils import db, const
import main


def menu_ajouter_donnees():
    """
    Menu d'ajout des données
    """
    print("---- Menu ajout ----")
    print("1. Ajouter une personne")
    print("2. Ajouter un appareil")
    print("3. Ajouter un modèle d'appareil")
    print("4. Ajouter une réparation")
    print("5. Ajouter un évènement")
    print("6. <- Retour")
    entree = input("Entrez votre choix : ")
    print("----")
    if(entree == "1"):
        ajouter_personne()
    elif(entree == "2"):
        ajouter_appareil()
    elif(entree == "3"):
        ajouter_modeleAppareil()
    elif(entree == "4"):
        ajouter_reparation()
    elif(entree == "5"):
        ajouter_evenement()
    elif(entree == "6"):
        main.menu_principal()
    else:
        print("Choix invalide")
        menu_ajouter_donnees()

def ajouter_personne():
    """
    Fonction qui demande les attributs d'une personne (nom, prenom...) et qui l'ajoute dans la base de données
    """
    nom = input("Entrez le nom de la personne : ")
    prenom = input("Entrez le prénom de la personne : ")
    mail = input("Entrez le mail de la personne : ")
    commande = "INSERT INTO Personnes (nom_personne, prenom_personne, email_personne) VALUES ('" + nom + "', '" + prenom + "', '" + mail + "');"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        if(str(e) == "UNIQUE constraint failed: Personnes.email_personne"):
            print("Erreur : cette adresse e-mail est déjà utilisée")
        else:
            print("Erreur lors de l'insertion de la personne :", e)
    menu_ajouter_donnees()

def ajouter_appareil():
    """
    Fonction qui demande les attributs d'un appareil (numéro de série, modèle d'appareil...) et qui l'ajoute dans la base de données
    """
    # on choisit d'abord le modèle d'appareil
    commande = "SELECT * FROM ModeleAppareils;"
    execution = db.executer_commande_sql(commande)
    if(len(execution) == 0):
        print("Il n'y a pas de modèles d'appareils dans la base de données, veuillez en ajouter un d'abord")
        return
    db.afficher_resultats(execution)
    modele = input("Entrez le modèle de l'appareil : ")
    while not const.verifierSiColonneExiste(modele, execution):
        print("Le modèle n'existe pas, veuillez en choisir un dans la liste")
        modele = input("Entrez le modèle de l'appareil : ")
    # on choisit ensuite le propriétaire de l'appareil
    commande = "SELECT * FROM Personnes;"
    execution = db.executer_commande_sql(commande)
    if(len(execution) == 0):
        print("Il n'y a pas aucune personne enregistrée dans la base de données, veuillez en ajouter une d'abord pour pouvoir affecter un propriétaire à l'appareil")
        return
    db.afficher_resultats(execution)
    proprietaire = input("Entrez le propriétaire de l'appareil : ")
    while not const.verifierSiColonneExiste(modele, execution):
        print("Le propriétaire n'existe pas, veuillez en choisir un dans la liste")
        modele = input("Entrez le modèle de l'appareil : ")
    # on demande le numéro de série
    numSerie = input("Entrez le numéro de série de l'appareil : ")
    commande = "INSERT INTO Appareils VALUES ('"+ numSerie +"', '"+ modele +"', '"+ proprietaire +"');"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        if(str(e) == "UNIQUE constraint failed: Appareils.numeroDeSerie_appareil"):
            print("Erreur : ce numéro de série est déjà utilisé")
        else:
            print("Erreur lors de l'insertion de l'appareil :", e)
    menu_ajouter_donnees()

def ajouter_modeleAppareil():
    """
    Fonction qui demande les attributs d'un modèle d'appareil (marque, modèle...) et qui l'ajoute dans la base de données
    """
    marque = input("Entrez la marque  : ")
    modele = input("Entrez le modèle  : ")
    ram = input("Entrez la quantité de RAM (en Go): ")
    while not const.entreeEstEntier(ram):
        print("La quantité de RAM doit être un entier positif")
        ram = input("Entrez la quantité de RAM (en Go): ")
    processeur = input("Entrez le processeur : ")
    type = ["smartphone", "tablette", "ordinateur_portable", "ordinateur_bureau"]
    for i in range(len(type)):
        print(str(i) + ". " + type[i])
    typeAppareil = input("Entrez le type d'appareil : ")
    while not (const.entreeEstEntier(typeAppareil) and int(typeAppareil) >= 0 and  int(typeAppareil) < len(type)):
        print("Le type d'appareil n'existe pas, veuillez en choisir un dans la liste")
        typeAppareil = input("Entrez le type d'appareil : ")
    commande = "INSERT INTO ModeleAppareils ('marque_appareil', 'modele_appareil', 'ram_appareil', 'processeur_appareil', 'type_appareil') VALUES ('"+ marque +"', '"+ modele +"', "+ ram +", '"+ processeur +"', '"+ type[int(typeAppareil)] +"');"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
            print("Erreur lors de l'insertion de l'appareil :", e)
    menu_ajouter_donnees()

def ajouter_reparation():
    """
    Fonction qui demande les attributs d'une réparation (date, appareil...) et qui l'ajoute dans la base de données
    """
    # on choisit d'abord l'appareil réparé
    commande = "SELECT * FROM Appareils;"
    execution = db.executer_commande_sql(commande)
    if(len(execution) == 0):
        print("Il n'y a pas d'appareils à réparer dans la base de données, veuillez en ajouter un d'abord")
        return
    db.afficher_resultats(execution)
    modele = input("Entrez le numéro de série de l'appareil réparé : ")
    while not const.verifierSiColonneExiste(modele, execution):
        print("Le modèle n'existe pas, veuillez en choisir un dans la liste")
        modele = input("Entrez le numéro de série de l'appareil réparé : ")
    # on choisit ensuite à quel évènement l'appareil a été réparé
    commande = "SELECT * FROM Evenements;"
    execution = db.executer_commande_sql(commande)
    if(len(execution) == 0):
        print("Il n'y a pas d'évènements dans la base de données, veuillez en ajouter un d'abord")
        return
    db.afficher_resultats(execution)
    evenement = input("Entrez le numéro de l'évènement où l'appareil a été réparé : ")
    while not const.verifierSiColonneExiste(evenement, execution):
        print("L'évènement n'existe pas, veuillez en choisir un dans la liste")
        evenement = input("Entrez l'évènement où l'appareil a été réparé : ")
    prix = input ("Entrez le prix de la réparation : ")
    while not const.estPrixCorrect(prix):
        print("Le n'est pas correct")
        prix = input ("Entrez le prix de la réparation : ")
    duree = input ("Entrez la durée de la réparation (en minutes) : ")
    while not const.entreeEstEntier(duree):
        print("La durée doit être un entier positif")
        duree = input ("Entrez la durée de la réparation (en minutes) : ")
    description = input ("Entrez une description de la réparation : ")
    commande = "INSERT INTO Reparations ('appareil_repare', 'evenement_reparation', 'prix_reparation', 'duree_reparation', 'description_reparation') VALUES ('"+ modele +"', "+ evenement +", "+ prix +", "+ duree +", '"+ description +"');"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        print("Erreur lors de l'insertion de la réparation :", e)
    menu_ajouter_donnees()
    

def ajouter_evenement():
    """
    Fonction qui demande les attributs d'un évènement (date, ville...) et qui l'ajoute dans la base de données
    """
    date = input("Entrez la date de l'évènement (format : AAAA-MM-JJ) : ")
    while not const.estDateCorrecte(date):
        print("La date n'est pas correcte")
        date = input("Entrez la date de l'évènement (format : AAAA-MM-JJ) : ")
    heureDebut = input("Entrez l'heure de début de l'évènement (format : HH:MM) : ")
    while not const.estHeureCorrecte(heureDebut):
        print("L'heure de début n'est pas correcte")
        heureDebut = input("Entrez l'heure de début de l'évènement (format : HH:MM) : ")
    heureFin = input("Entrez l'heure de fin de l'évènement (format : HH:MM) : ")
    while not const.estHeureCorrecte(heureFin):
        print("L'heure de fin n'est pas correcte")
        heureFin = input("Entrez l'heure de fin de l'évènement (format : HH:MM) : ")
    ville = input("Entrez la ville de l'évènement : ")
    commande = "INSERT INTO Evenements ('date_evenement', 'heureDebut_evenement', 'heureFin_evenement', 'ville_evenement') VALUES ('"+ date +"', '"+ heureDebut +"', '"+ heureFin +"', '"+ ville +"');"
    try:
        db.executer_commande_sql(commande)
    except Exception as e:
        print("Erreur lors de l'insertion de l'évènement :", e)
    menu_ajouter_donnees()

    
