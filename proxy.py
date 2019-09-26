import math


"""
Uwaga: Proxy i Calculator powinny dziedziczyć z tej samej klasy-matki
"""


class Proxy:
    def __init__(self):
        self.memory = {}

    def square_equation(self, a, b, c):
        try:
            print(str(a) + "x^2 + " + str(b) + "x + " + str(c))
            print("Szukam rozwiązania w proxy...")
            return self.memory[(a, b, c)]
        except KeyError:
            print("Nie znaleziono rozwiązania w bazie. Nastąpi obliczenie wyniku.")
            self.memory[(a, b, c)] = Calculator.square_equation(a, b, c)
            return self.memory[(a, b, c)]


class Calculator:
    @staticmethod
    def square_equation(a, b, c):
        delta = (b * b) - (4 * a * c)
        if delta > 0:
            sq = math.sqrt(delta)
            x1 = (-b - sq) / (2 * a)
            x2 = (-b + sq) / (2 * a)
            return x1, x2
        elif delta == 0:
            x = -b / (2 * a)
            return x
        else:
            return "Brak miejsc zerowych"


if __name__ == '__main__':
    proxy = Proxy()
    print(proxy.square_equation(2, 1, 2))
    print()
    print(proxy.square_equation(2, 1, 2))
    print()
    print(proxy.square_equation(1, 2, 1))
    print()
    print(proxy.square_equation(1, 2, 1))
    print()
    print(proxy.square_equation(-1, 3, 4))
    print()
    print(proxy.square_equation(-1, 3, 4))
    print()
    print("Zapamiętane rozwiązania:")
    print(proxy.memory)
