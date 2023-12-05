from time import sleep, strftime, localtime, mktime

alarm_time = None

def afficher_heure():
    current_time = strftime('%I:%M:%S %p')
    print("\r" + current_time, end="", flush=True)

    if alarm_time is not None and strftime('%I:%M:%S %p') == strftime('%I:%M:%S %p', localtime(alarm_time)):
        afficher_message_alarme()

    sleep(1)
    afficher_heure()

def regler_alarme(heure_alarme):
    global alarm_time
    alarm_time = mktime((2000, 1, 1, heure_alarme[0], heure_alarme[1], heure_alarme[2], 0, 0, -1))
    print(f'\nALARM SET ON  : {strftime("%I:%M:%S %p", localtime(alarm_time))}')

regler_alarme((8, 51, 00))

def afficher_message_alarme():
    print("\nCLOCK ! TIME TO WAKE UP BUDDY.")

while True:
    afficher_heure()
    regler_alarme(())