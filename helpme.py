import string
from typing import List
import tkinter as tk
from tkinter import messagebox

alphabet: List[str] = list(string.ascii_lowercase)


def help():
    ausgabe = ' '.join(str(element) for element in alphabet)
    tk.messagebox.showinfo("Übrige Buchstaben", ausgabe)


def help_alter(char: str):
    if char in alphabet:
        for chars in range(len(alphabet)):
            if char == list(alphabet)[chars]:
                alphabet[chars] = "-"



