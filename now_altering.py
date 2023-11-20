def now_altering(char: str, word: str, now: str) -> str:
    new_now = ""
    for chars in range(len(word)):
        if char == list(word)[chars]:
            new_now += char + ' '
        else:
            new_now += list((now.split(' ')))[chars] + ' '
    now = new_now.upper()
    return now
