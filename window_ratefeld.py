import sys
import tkinter as tk
from tkinter import ttk
import wortwahl
import now_altering
import check
import helpme


def spielen(versuche: int):
    counter = versuche

    def help_me():
        helpme.help()

    def raten():
        nonlocal counter

        char = buchstaben_eingabe.get().lower()[0]
        helpme.help_alter(char)
        buchstaben_eingabe.delete(0, 'end')

        if len(char) > 0:
            if char in word:
                ergebnis.set(f"Sehr gut! {char.upper()} ist vorhanden.")
                word_hidden.set(now_altering.now_altering(char, word, word_hidden.get()))
            else:
                ergebnis.set(f"Leider ist {char.upper()} nicht vorhanden!")
                counter -= 1
                label4.config(text=f"Noch {counter} Versuche")

                if counter == 0:
                    buchstaben_eingabe.configure(state='disabled')

        spielausgang.set(check.check(counter, word, word_hidden.get()))

    top = tk.Toplevel()
    top.geometry("300x400")
    top.title("HANGMAN - SPIEL")

    word = wortwahl.choose_word()
    ergebnis = tk.StringVar()
    word_hidden = tk.StringVar(value=wortwahl.hidden_word(word))
    spielausgang = tk.StringVar(value=check.check(counter, word, str(word_hidden)))

    # Entryfield
    buchstaben_eingabe = tk.Entry(top)
    buchstaben_eingabe.pack(padx=10, pady=10)

    # Button
    button_frame = tk.Frame(top)
    button_frame.pack(padx=10, pady=10)

    button = ttk.Button(button_frame, text="Rate", width=10, command=raten)
    button.pack()

    # Hilfe Button
    button_help = ttk.Button(top, text="Help", width=10, command=help_me)
    button_help.pack(side="bottom", anchor="se")


    # Ausgabefelder
    label1 = ttk.Label(top, textvariable=ergebnis)
    label1.pack(padx=10, pady=10)

    label2 = ttk.Label(top, textvariable=word_hidden)
    label2.pack(padx=10, pady=10)

    label4 = ttk.Label(top)
    label4.pack(padx=10, pady=10)

    # Ausgabefeld - Spielende
    label3 = ttk.Label(top, textvariable=spielausgang)
    label3.pack(padx=10, pady=10)

    top.mainloop()

