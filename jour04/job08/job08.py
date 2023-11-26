# Définir la liste L
L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

# la somme des valeurs paires
somme = 0

# ajouter les valeurs paires à la somme
for nombre in L:
    if nombre % 2 == 0:
        somme += nombre

# résultat
print((somme))
