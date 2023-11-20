import tkinter as tk
import sys
import window_modus_choise


def handle_yes():
    root.destroy()
    window_modus_choise.modus_choise()


def handle_no():
    root.destroy()
    sys.exit(0)


root = tk.Tk()
root.title("HANGMAN")
root.geometry("300x150")

text = "Möchtest du Hangman spielen?"
label = tk.Label(root, text=text)
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()

yes_button = tk.Button(button_frame, text="Ja", width=10, command=handle_yes)
yes_button.grid(row=0, column=0, padx=10)

no_button = tk.Button(button_frame, text="Nein", width=10, command=handle_no)
no_button.grid(row=0, column=1, padx=10)

root.mainloop()


