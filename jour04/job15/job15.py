def arrondir_et_trier(liste):
    # Arrondir les nombres de la liste
    liste_arrondie = []
    for nombre in liste:
        nombre_arrondi = int(nombre + 0.5)  # Technique d'arrondi simple
        liste_arrondie.append(nombre_arrondi)

    # Trier la liste arrondie
    liste_triee = []
    while liste_arrondie:
        minimum = liste_arrondie[0]
        for nombre in liste_arrondie:
            if nombre < minimum:
                minimum = nombre
        liste_triee.append(minimum)
        liste_arrondie.remove(minimum)

    return liste_triee

# Exemple d'utilisation
ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

resultat = arrondir_et_trier(ma_liste)

print("Liste arrondie et triée :", resultat)
