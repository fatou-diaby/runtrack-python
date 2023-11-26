#liste 
L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Initialiser le produit
produit = 1

# Parcourir la liste et multiplier les valeurs dans l'intervalle [25, 90]
for nombre in L:
    if 25 <= nombre <= 90:
        produit *= nombre

# Afficher le résultat
print("Le produit des valeurs dans l'intervalle [25, 90] est :", produit)
