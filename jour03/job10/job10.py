def verifier_pair_impair(nombre):
    if isinstance(nombre, int) and nombre >= 0:
        if nombre % 2 == 0:
            print(f"{nombre} est un nombre entier positif et pair.")
        else:
            print(f"{nombre} est un nombre entier positif et impair.")
    else:
        print("Veuillez entrer un nombre entier positif.")


verifier_pair_impair(10)
verifier_pair_impair(7)
verifier_pair_impair(0)
verifier_pair_impair(-4)
verifier_pair_impair(3.14)  
