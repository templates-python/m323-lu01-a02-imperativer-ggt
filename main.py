def ggt(a, b):
    while b != 0:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    zahl1 = 56
    zahl2 = 48
    resultat = ggt(zahl1, zahl2)
    print(
        f"Der GGT von {zahl1} und {zahl2} ist {resultat}"
    )  # Ausgabe: Der GGT von 56 und 48 ist 8
