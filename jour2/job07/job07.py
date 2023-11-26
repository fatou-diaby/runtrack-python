chaine = "abcdefghijklmnopqrstuvwxyz" * 10

nb_caracteres = 1
indice = 0

while indice < len(chaine):
    print(chaine[indice:indice + nb_caracteres])
    indice += nb_caracteres
    nb_caracteres += 1

