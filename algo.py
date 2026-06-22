# ================================================
# Analyse d'une phrase caractère par caractère
# ================================================
# Compteurs : longueur, mots, voyelles

phrase = input("Entrez une phrase se terminant par un point : ")

# Vérification que la phrase se termine par un point
if not phrase.endswith('.'):
    print("Erreur : la phrase doit se terminer par un point.")
else:
    longueur = 0   # Compteur 1 : nombre de caractères
    mots     = 1   # Compteur 2 : nombre de mots (1 mot minimum)
    voyelles = 0   # Compteur 3 : nombre de voyelles

    VOYELLES = "aeiouàâäéèêëîïôöùûüyAEIOUÀÂÄÉÈÊËÎÏÔÖÙÛÜY"

    # Lecture caractère par caractère
    for caractere in phrase:

        # On arrête au point final
        if caractere == '.':
            break

        # Compteur 1 : longueur (chaque caractère sauf le point)
        longueur += 1

        # Compteur 2 : mots (on compte les espaces)
        if caractere == ' ':
            mots += 1

        # Compteur 3 : voyelles
        if caractere in VOYELLES:
            voyelles += 1

    # Affichage des résultats
    print("\n========== Résultats ==========")
    print(f"Longueur de la phrase : {longueur} caractère(s)")
    print(f"Nombre de mots        : {mots} mot(s)")
    print(f"Nombre de voyelles    : {voyelles} voyelle(s)")
    print("================================")