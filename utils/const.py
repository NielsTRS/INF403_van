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
