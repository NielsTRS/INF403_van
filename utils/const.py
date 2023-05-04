import datetime

tables = {
    "Personnes":{
        "nomSing" : "de la personne",
        "nomPlur" : "des personnes",
        "primary_key": "numero_personne",
    },
    "Appareils":{
        "nomSing" : "de l'appareil",
        "nomPlur" : "des appareils",
        "primary_key": "numeroDeSerie_appareil",
    },
    "Reparations":{
        "nomSing" : "de la réparation",
        "nomPlur" : "des réparations",
        "primary_key": "numero_reparation",
    },
    "Evenements":{
        "nomSing" : "de l'évènement",
        "nomPlur" : "des évènements",
        "primary_key": "numero_evenement",
    },
    "ModeleAppareils":{
        "nomSing" : "du modèle",
        "nomPlur" : "des modèles",
        "primary_key": "numero_appareil",
    }
}

def getSingularTableName(table):
    return tables[table]["nomSing"]

def getPluralTableName(table):
    return tables[table]["nomPlur"]

def getPrimaryKey(table):
    return tables[table]["primary_key"]


def verifierSiColonneExiste(numero, resultat):
    """
    Fonction qui vérifie si une colonne existe dans une table

    :param numero: Numéro de la colonne
    :param resultat: Resultat d'une commande SQL
    :return: True si la colonne existe, False sinon
    """
    try: 
        numero = int(numero)
    except ValueError:
        pass
    for i in range(1,len(resultat)):
        if(resultat[i][0] == numero):
            return True
    return False

def entreeEstEntier(entree):
    """
    Fonction qui vérifie si une entrée est un entier

    :param entree: Entrée à vérifier
    :return: True si l'entrée est un entier, False sinon
    """
    try:
        entierEntree = int(entree)
        if(entierEntree < 0):
            return False
        return True
    except ValueError:
        return False
    
def estPrixCorrect(prix):
    """
    Fonction qui vérifie si un prix est correct

    :param prix: Prix à vérifier
    :return: True si le prix est correct, False sinon
    """
    try:
        prixEntier = int(prix)
        if(prixEntier < 0):
            return False
        return True
    except ValueError:
        pass
    try:
        prixFlottant = float(prix)
        if(prixFlottant < 0):
            return False
        return True
    except ValueError:
        return False
    
def estDateCorrecte(date):
    """
    Fonction qui vérifie si une date est correcte

    :param date: Date à vérifier
    :return: True si la date est correcte, False sinon
    """
    try:
        datetime.datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def estHeureCorrecte(heure):
    """
    Fonction qui vérifie si une heure est correcte

    :param heure: Heure à vérifier
    :return: True si l'heure est correcte, False sinon
    """
    try:
        datetime.datetime.strptime(heure, '%H:%M')
        return True
    except ValueError:
        return False