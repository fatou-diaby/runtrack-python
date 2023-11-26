def my_long_word(taille_min, phrase):
    mots = []
    mot = ""

    for char in phrase:
        if char.isalnum() or char == "'":
            mot += char
        elif mot != "":
            mots.append(mot)
            mot = ""

    if mot != "":
        mots.append(mot)

    mots_plus_longs = []
    for mot in mots:
        if len(mot) > taille_min:
            mots_plus_longs.append(mot)

    return " ".join(mots_plus_longs)

# Exemple d'utilisation
taille_minimale = 3
phrase = "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"

resultat = my_long_word(taille_minimale, phrase)

print("Output :", resultat)
