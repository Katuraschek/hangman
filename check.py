def check(versuche: int, word: str, now: str) -> str:
    if versuche == 0:
        return("_________________Leider verloren!_________________\n"
        "                      +---+--\n"
        "                             |   |\n"
        "                           O   |\n"
        "                          /|\  |\n"
        "                          / \  |\n"
        "                                 |\n"
               "\n"
        f"        Das gesuchte Wort war {word.upper()}!\n")

    if "_" not in now and versuche != 0:
        return("\n"
        "********** GEWONNEN!!! **********\n"
        "\n"
        f"Das gesuchte Wort war {word.upper()}!\n"
        "\n")

    else:
        return""