import random
random.seed()


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


def choose_word() -> str:
    nr = random.randint(0, len(words) - 1)
    word = words[nr].lower()
    return word


def hidden_word(word:str) -> str:
    now = ""
    for _ in word:
        now += "_ "
    return now
