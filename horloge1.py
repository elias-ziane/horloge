from time import strftime, localtime, mktime, sleep

def afficher_heure():
    while True:
        current_time = strftime('%H:%M:%S %p')
        print(current_time)

        # Vérifie si l'alarme est définie et si l'heure actuelle correspond à l'heure de l'alarme
        if alarm_time is not None and strftime('%H:%M:%S') == strftime('%H:%M:%S', localtime(alarm_time)):
            afficher_message_alarme()

        sleep(1)  # Met à jour toutes les 1 seconde

def regler_alarme(heure_alarme):
    global alarm_time
    alarm_time = mktime((2000, 1, 1, heure_alarme[0], heure_alarme[1], heure_alarme[2], 0, 0, -1))
    print(f'Alarme réglée à {strftime("%H:%M:%S", localtime(alarm_time))}')

def afficher_message_alarme():
    # Affiche un message lorsque l'heure actuelle correspond à l'heure de l'alarme
    print("Il est temps !")

def get_heure_alarme():
    # Fonction pour obtenir l'heure de l'alarme sous forme de tuple
    user_input = input("Entrez l'heure de l'alarme (HH:MM:SS): ")

    # Vérifiez si l'utilisateur a saisi une valeur et si elle est au bon format
    if user_input and len(user_input.split(':')) == 3:
        # Convertissez la saisie de l'utilisateur en tuple d'entiers (heures, minutes, secondes)
        return tuple(map(int, user_input.split(':')))
    else:
        # Affichez un message d'erreur si l'entrée est incorrecte
        print("Format d'heure incorrect. Réglez à nouveau l'alarme.")
        return None

if __name__ == "__main__":
    alarm_time = None  # Initialise l'heure de l'alarme à None

    try:
        afficher_heure()
    except KeyboardInterrupt:
        print("\nProgramme terminé.")
