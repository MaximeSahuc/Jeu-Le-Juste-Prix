# Maxime Sahuc 19/05/2021 21:56
import time
import random
import threading
from tkinter import *

backgrounColor = '#78ff7c'
buttonBackgrounColor = '#bdffbf'
textColor = '#363636'

nombreATrouver = random.randint(0, 100)
remainingAttempts = 5
timer = time.time()
max_time = 60
remainingTime = max_time

gameFinished = False

class CountDown(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global remainingTime
        global gameFinished

        while remainingTime > 0 and remainingAttempts > 0 and gameFinished == FALSE:
            remainingTime = (max_time - 1) - round(time.time() - timer)
            label_remaining_time['text'] = "Temps restant: " + str(remainingTime) + "s"
            time.sleep(1)

        if(remainingTime == 0):
            label_title.configure(text="Trop tard")
            gameFinished = True
            reset()


def validerReponse():
    global remainingAttempts
    global gameFinished

    if (remainingAttempts > 0):
        if (entry.get() != ""):
            try:
                i = int(entry.get())
                remainingAttempts -= 1
                label_remaining_attempts['text'] = "Tentatives restantes: " + str(remainingAttempts)
                global nombreATrouver
                print("Le bon numero est " + str(nombreATrouver))
                if (i == nombreATrouver):
                    label_title['text'] = "C’est gagné"
                    gameFinished = True
                    reset()

                if (i > nombreATrouver):
                    label_title['text'] = "C’est moins"

                if (i < nombreATrouver):
                    label_title['text'] = "C’est plus"

            except ValueError:
                return
    else:
        gameFinished = True
        label_title.configure(text="C’est perdu")
        reset()


def reset():
    button.configure(text="Recommencer", font=("Arial", 15), bg=buttonBackgrounColor, fg=textColor,command=startGame)


def startGame():
    global nombreATrouver
    global remainingAttempts
    global timer
    global remainingTime
    global gameFinished
    gameFinished = False
    nombreATrouver = random.randint(0, 100)
    remainingAttempts = 5
    timer = time.time()
    remainingTime = max_time

    countdownThread = CountDown()
    countdownThread.start()

    entry.place(relx=0.5, rely=0.5, anchor='center')
    button.configure(text="Valider la réponse", font=("Arial", 15), bg=buttonBackgrounColor, fg=textColor, command=validerReponse)
    label_title.configure(text="")


#fenetre
window = Tk()
window.title("Juste Prix")
window.geometry("650x620")
window.minsize(650, 420)
window.maxsize(650, 420)
window.config(background=backgrounColor)

#tentatives restantes
label_remaining_attempts = Label(window, text="Tentatives restantes: " + str(remainingAttempts), font=("Arial", 15), bg=backgrounColor, fg=textColor)
label_remaining_attempts.place(relx = 1.0, rely = 0.0, anchor ='ne')

#temps restant
label_remaining_time = Label(window, text="Temps restant: " + str(remainingTime) + "s", font=("Arial", 15), bg=backgrounColor, fg=textColor)
label_remaining_time.place(relx = 0.0, rely = 0.0, anchor ='nw')

#entry
entry = Entry(window, width=50)
entry.place(relx = 0.5, rely = 2.5, anchor = 'center')

#titre
label_title = Label(window, text="Bienvenue sur le célèbre jeu du juste prix, \ntu dois deviner le prix auquel je pense, \nil se situe entre 1 et 100", font=("Arial", 20), bg=backgrounColor, fg=textColor)
label_title.place(relx = 0.5, rely = 0.3, anchor = 'center')

#bouton
button = Button(window, text="Commencer", font=("Arial", 15), bg=buttonBackgrounColor, fg=textColor, command=startGame)
button.place(relx = 0.5, rely = 0.7, anchor = 'center')

window.mainloop()