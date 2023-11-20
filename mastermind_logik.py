import random
import sys
from stringcolor import *
from colorama import Fore
random.seed()

farben_dict = {
    "rot": Fore.RED,
    "blau": Fore.BLUE,
    "gruen": Fore.GREEN,
    "gelb": Fore.YELLOW,
    " X ": Fore.WHITE
}


# Zufällige anordnung erstellen
def erstellen() -> list:
    farben = list(farben_dict.keys())
    anordnung = random.sample(farben*2, k=6)
    return anordnung


# Versteckte Anordnung ausgeben
def initiale_anordnung(anordnung: list) -> list:
    anordnung_versteckt = []
    for _ in range(len(anordnung)):
        anordnung_versteckt.append(" X ")
    return anordnung_versteckt


# Anordnung raten
def raten() -> list:
    print("")
    vermutung = input("Gebe deine Vermutung an:\n")
    vermutung_liste = vermutung.split()
    return vermutung_liste


# Anordnung mit Vermutung vergleichen
def vergleich(anordnung: list, vermutung: list) -> list:
    if vermutung == anordnung:
        print("-"*35, "GEWONNEN", "-"*35)
        sys.exit()

    aktueller_abgleich = []
    for index, element in enumerate(vermutung):
        if element in anordnung[index]:
            aktueller_abgleich.append(element)
        else:
            aktueller_abgleich.append(" X ")
    return aktueller_abgleich


def farbig_ausgeben(liste: list):
    farbige_anordnung = liste
    for farbe in farbige_anordnung:
        print(farben_dict[farbe] + farbe + Fore.RESET, end="  ")


def starten():
    ratekombi = erstellen()
    print("  ".join(initiale_anordnung(ratekombi)))

    while True:
        geraten = raten()
        abgleich = vergleich(ratekombi, geraten)
        farbig_ausgeben(abgleich)


if __name__ == "__main__":
    print(cs("Let's play!", "orchid"))
    starten()
