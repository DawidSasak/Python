import sys

print("Kalkulator")

def kontynuuj():
    c = input("Czy chcesz kontynuować? (Tak/Nie): ")
    if c == ("Tak") or c == ("tak") or c == ("t"):
        kalkulator()

    if c == ("Nie") or c == ("nie") or c == ("n"):
        sys.exit()

def kalkulator():
    z = input("Wybierz rodzaj działania\nA. Dodawanie\nB. Odejmowanie\nC. Mnożenie\nD. Dzielenie\nE. Potęgowanie\n: ")
    if z == ("A") or z == ("a"):
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik: ", float(x) + float(y))
        kontynuuj()

    if z == ("B") or z == ("b"):
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik: ", float(x) - float(y))
        kontynuuj()

    if z == ("C") or z == ("c"):
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik: ", float(x) * float(y))
        kontynuuj()

    if z == ("D") or z == ("d"):
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik: ", float(x) / float(y))
        kontynuuj()

    if z == ("E") or z == ("e"):
        x = input("Podaj liczbę x: ")
        y = input("Podaj liczbę y: ")
        print("Wynik: ", float(x) ** float(y))
        kontynuuj()

kalkulator()
