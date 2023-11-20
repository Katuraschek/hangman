import tkinter as tk
from tkinter import ttk
import window_ratefeld


def modus_uebergabe(modus: str):
    def start():
        window_ratefeld.spielen(versuche)

    root = tk.Tk()
    root.geometry("650x300")
    root.title("HANGMAN - Regel")

    begruessung = ("________ Willkommen bei HANGMAN!!! ________")

    if modus == 'l':
        mod = "Dein Modus ist LEICHT."
        versuche = 15
    elif modus == 'm':
        mod = "Dein Modus ist MITTEL."
        versuche = 10
    elif modus == 's':
        mod = "Dein Modus ist SCHWER."
        versuche = 7

    regel = ("Hier die Spielregeln: \n 1. Tippe einen Buchstaben ein. Kommt dieser Buchstabe im gesuchten Wort "
          "vor, wird er eingetragen. \n      Kommt er nicht vor, wird dir ein Punkt abgezogen und Hangman kriegt "
          f"einen. \n 2. Hast du mehrmals als {versuche} Mal falsch geraten hast du verloren! \n "
          f"3. Konntest du das Wort mit weniger als {versuche} Fehlversuche erraten, hast du gewonnen! \n 4. Willst "
          "du wissen, welche Buchstaben du schon getippt hattest schreibe 'help' \n \n UND JETZT: VIEL SPAß!!!")

    label1 = ttk.Label(root, text=begruessung)
    label1.pack(padx=10, pady=10)

    label2 = ttk.Label(root, text=mod)
    label2.pack(padx=10, pady=10)

    label3 = ttk.Label(root, text=regel)
    label3.pack(padx=10, pady=10)

    button = ttk.Button(root, text="Los Geht's!", command=start)
    button.pack(padx=10, pady=10)

    root.mainloop()