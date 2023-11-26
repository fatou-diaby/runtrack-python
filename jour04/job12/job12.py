def tri(liste):
    n =0
    for _ in liste:
        n += 1

    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                # Échanger les éléments si ils ne sont pas dans l'ordre croissant
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

# liste
L= [64, 34, 25, 12, 22, 11, 90]

# Afficher la liste avant le tri
print((L))

# Trier la liste en ordre croissant
tri(L)

# Afficher la liste après le tri
print((L))
