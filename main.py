fichier = r"F:\udemy\prenoms.txt"

prenoms_uniques = set()  # Ensemble pour stocker les prénoms uniques

with open(fichier, 'r', encoding="utf-8") as f:
    lignes = f.readlines()  # Lis toutes les lignes du fichier

# Traitement et stockage des prénoms uniques
for ligne in lignes:
    # Découpe les prénoms séparés par des virgules
    prenoms = ligne.strip().split(",")  
    for prenom in prenoms:
        # Nettoie chaque prénom, supprime les espaces inutiles et les caractères indésirables
        prenom_nettoye = prenom.strip(" .\n")  # Enlève les espaces, points et sauts de ligne
        if prenom_nettoye:  # Vérifie que le prénom n'est pas vide
            prenoms_uniques.add(prenom_nettoye)

# Affichage des prénoms uniques triés avec numérotation
for i, prenom in enumerate(sorted(prenoms_uniques), start=1):
    print(i, prenom)
