import random
import sys


class Hangman:
    words = [
        "Hund", "Katze", "Haus", "Auto", "Baum", "Tisch", "Stuhl", "Buch", "Blume", "Telefon",
        "Schuh", "Wald", "Berg", "Himmel", "Sonne", "Mond", "Stadt", "Land", "Meeresfruechte",
        "Fisch", "Vogel", "Fluss", "Ozean", "Strand", "Blatt", "Gras", "Wiese",
        "Park", "Blume", "Rose", "Tulpe", "Lilie", "Orchidee", "Kaktus", "Diamant", "Gold", "Silber",
        "Juwel", "Uhr", "Kette", "Armband", "Ring", "Muetze", "Hut", "Handschuhe", "Schal", "Jacke",
        "Hose", "Kleid", "Rock", "Bluse", "Pulli", "Shirt", "Anzug", "Krawatte", "Hemd", "Mantel",
        "Bademantel", "Bikini", "Badehose", "Handtuch", "Zahnbuerste", "Zahnpasta", "Seife", "Shampoo", "Spuelung",
        "Conditioner",
        "Duschgel", "Deodorant", "Parfuem", "Nagellack", "Pinzette", "Rasierer", "Rasierklinge", "Aftershave",
        "Bodylotion", "Creme",
        "Maskara", "Foundation", "Lidschatten", "Lippenstift", "Puder", "Sonnencreme", "Handcreme"
    ]

    def __init__(self, versuche):
        word = self.choose_word()
        self.word = word
        self.now = "_ " * len(word)
        self.versuche = versuche
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                         'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                         's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        self.printer()

    def choose_word(self) -> str:
        nr = random.randint(0, len(self.words)-1)
        return self.words[nr].lower()

    def printer(self) -> None:
        print(" ")
        print(self.now.capitalize())
        print(" ")

    def help(self) -> None:
        ausgabe = ' '.join(str(element) for element in self.alphabet)
        print(ausgabe)

    def help_alter(self, char: str):
        if char in self.alphabet:
            for chars in range(len(self.alphabet)):
                if char == list(self.alphabet)[chars]:
                    self.alphabet[chars] = "-"

    def check(self):
        if self.versuche == 0:
            print("_________________Leider verloren!_________________")
            print("+---+--")
            print("  |   |")
            print("  O   |")
            print(" /|\  |")
            print(" / \  |")
            print("      |")
            print(f"Das gesuchte Wort war {self.word.upper()}!")
            gaming()
        if "_" not in self.now and self.versuche != 0:
            print("")
            print("********** GEWONNEN!!! **********")
            print("")
            print(f"Das gesuchte Wort war {self.word.upper()}!")
            print("")
            gaming()

    def guess(self, char: str) -> None:
        self.help_alter(char)

        if char in self.word:
            new_now = ""
            for chars in range(len(self.word)):
                if char == list(self.word)[chars]:
                    new_now += char + ' '
                else:
                    new_now += list((self.now.split(' ')))[chars] + ' '
            self.now = new_now
            self.check()
        else:
            self.hang()
        self.printer()

    def hang(self):
        self.versuche -= 1
        self.check()
        print(f"Oh Oh! Du hast nur noch {self.versuche} Versuche!")


def gaming():
    while True:
        choise = input("Möchtest du Hangmanspielen? y/n: ")
        if choise == "n":
            print("Tschüss!")
            sys.exit(0)

        if choise == "y":
            modus = input("In welchem Modus möchtest du Spielen? \n "
                          "1. LEICHT (tippe 'l') \n"
                          "2. MITTEL (tippe 'm') \n"
                          "3. SCHWER (tippe 's') \n"
                          "")
            print("")

            print("________ Willkommen bei HANGMAN!!! ________")
            if modus == 'l':
                print("Dein Modus ist LEICHT.")
                versuche = 15
            elif modus == 'm':
                print("Dein Modus ist MITTEL.")
                versuche = 10
            elif modus == 's':
                print("Dein Modus ist SCHWER.")
                versuche = 7
            else:
                print("Der Modus wurde auf LEICHT gesetzt")
                versuche = 15
            print("Hier die Spielregeln: \n 1. Tippe einen Buchstaben ein. Kommt dieser Buchstabe im gesuchten Wort "
                  "vor, wird er eingetragen. Kommt er nicht vor, wird dir ein Punkt abgezogen und Hangman kriegt "
                  f"einen. \n 2. Hast du mehrmals als {versuche} Mal falsch geraten hast du verloren! \n "
                  f"3. Konntest du das Wort mit weniger als {versuche} Fehlversuche erraten, hast du gewonnen! \n 4. Willst "
                  "du wissen, welche Buchstaben du schon getippt hattest schreibe 'help' \n UND JETZT: VIEL SPAß!!!")
            print("")
            print("Hier kommt dein Wort:")
            print("")
            spiel = Hangman(versuche)

            while True:
                char = input("Rate den Buchstaben: ")
                if len(char) == 1:
                    spiel.guess(char.lower())
                elif char == "help":
                    spiel.help()
        else:
            print("Du kannst nur zwischen y und n wählen.")


gaming()
