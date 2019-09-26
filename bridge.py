from abc import ABC, abstractmethod # moduł Abstract Base Class

class Biblioteka(ABC):

    @abstractmethod
    def rysuj_linie(self, x1, y1, x2, y2):
        print("Ta metoda nie powinna dać się wykonać")

    @abstractmethod
    def rysuj_okrag(self, x, y, r):
        print("Ta metoda nie powinna dać się wykonać")

class BibliotekaV1(Biblioteka):
    def rysuj_linie(self, x1, y1, x2, y2):
        BG1().rysuj_linie(x1, y1, x2, y2)
    def rysuj_okrag(self, x, y, r):
        BG1().rysuj_okrag(x, y, r)

class BG1:
    def rysuj_linie(self, x1, y1, x2, y2):
        print("Metoda rysuj_linie z biblioteki BG1; parametry: " + str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2))

    def rysuj_okrag(self, x, y, r):
        print("Metoda rysuj_okrag z biblioteki BG1; parametry: " + str(x) + ", " + str(y) + ", " + str(r))

class BibliotekaV2(Biblioteka):
    def rysuj_linie(self, x1, y1, x2, y2):
        BG2().narysuj_linie(x1, y1, x2, y2)

    def rysuj_okrag(self, x, y, r):
        BG2().narysuj_okrag(x, y, r)

class BG2:
    def narysuj_linie(self, x1, y1, x2, y2):
        print("Metoda narysuj_linie z biblioteki BG2; parametry: " + str(x1) + ", " + str(y1) + ", " + str(x2) + ", " + str(y2))

    def narysuj_okrag(self, x, y, r):
        print("Metoda narysuj_okrag z biblioteki BG2; parametry: " + str(x) + ", " + str(y) + ", " + str(r))

class Figura(ABC):
    def __init__(self, biblioteka):
        self._biblioteka = biblioteka

    @abstractmethod
    def rysuj(self):
        print("Ta metoda nie powinna dać się wykonać")

    def rysuj_linie(self, x1, y1, x2, y2):
        self._biblioteka.rysuj_linie(x1, y1, x2, y2)
    
    def rysuj_okrag(self, x, y, r):
        self._biblioteka.rysuj_okrag(x, y, r)

class Prostokat(Figura):
    def __init__(self, biblioteka, x1, y1, x2, y2):
        super(Prostokat, self).__init__(biblioteka)
        self._biblioteka = biblioteka
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
    
    def rysuj(self):
        super(Prostokat, self).rysuj_linie(self._x1, self._y1, self._x2, self._y1)
        super(Prostokat, self).rysuj_linie(self._x2, self._y1, self._x2, self._y2)
        super(Prostokat, self).rysuj_linie(self._x2, self._y2, self._x1, self._y2)
        super(Prostokat, self).rysuj_linie(self._x1, self._y2, self._x1, self._y1)

class Okrag(Figura):
    def __init__(self, biblioteka, x, y, r):
        super(Okrag, self).__init__(biblioteka)
        self._biblioteka = biblioteka
        self._x = x
        self._y = y
        self._r = r
    
    def rysuj(self):
        super(Okrag, self).rysuj_okrag(self._x, self._y, self._r)

if __name__ == '__main__':

    p1 = Prostokat(BibliotekaV1(), 2, 3, 4, 5)
    p2 = Prostokat(BibliotekaV2(), 6, 7, 8, 9)
    o1 = Okrag(BibliotekaV1(), 0, 0, 5)
    o2 = Okrag(BibliotekaV2(), 5, 7, 4)

    figury = [p1, p2, o1, o2]

    for f in figury:
        f.rysuj()