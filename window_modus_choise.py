import tkinter as tk
from tkinter import ttk
import windows_spielregel


def modus_choise():
    root = tk.Tk()
    root.geometry("260x200")
    root.title("HANGMAN - Modus")

    def set_modus():
        mod = radio_modus.get()
        root.destroy()
        windows_spielregel.modus_uebergabe(mod)

    # Radiobutton: Auswahl-button
    label = ttk.Label(root, text="In welchem Modus möchtest du spielen?")
    label.pack(padx=10, pady=10)

    radio_modus = tk.StringVar()
    radio_modus.set("leicht")

    modi = ["leicht", "mittel", "schwer"]

    for modus in modi:
        ttk.Radiobutton(root, text=modus, variable=radio_modus, value=modus[0]).pack(padx=10, pady=10, anchor="w")

    button = ttk.Button(root, text="OK", command=set_modus)
    button.pack()

    root.mainloop()
