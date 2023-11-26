def time_to_text(minutes):
    if isinstance(minutes, int) and minutes >= 0:
        heures = minutes // 60
        minutes_restantes = minutes % 60

        if heures == 0:
            if minutes == 1:
                print(f"{minutes} minute")
            else:
                print(f"{minutes} minutes")
        elif heures == 1:
            if minutes_restantes == 0:
                print(f"{heures} heure")
            elif minutes_restantes == 1:
                print(f"{heures} heure et {minutes_restantes} minute")
            else:
                print(f"{heures} heure et {minutes_restantes} minutes")
        else:
            if minutes_restantes == 0:
                print(f"{heures} heures")
            elif minutes_restantes == 1:
                print(f"{heures} heures et {minutes_restantes} minute")
            else:
                print(f"{heures} heures et {minutes_restantes} minutes")
    else:
        print("Veuillez entrer un nombre entier positif.")


time_to_text(90)
time_to_text(120)
time_to_text(754)
time_to_text(251)
time_to_text(-5)  
