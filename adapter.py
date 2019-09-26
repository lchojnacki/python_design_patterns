class Figura:
    def __init__(self):
        print("Tworze obiekt klasy Figura...")
    def pobierz_polozenie(self):
        print("Metoda pobierz_polozenie klasy Figura.")
    def nadaj_polozenie(self):
        print("Metoda nadaj_polozenie klasy Figura.")
    def wyswietl(self):
        print("Metoda wyswietl klasy Figura.")
    def wypelnij(self):
        print("Metoda wypelnij klasy Figura.")
    def nadaj_kolor(self):
        print("Metoda nadaj_kolor klasy Figura.")
    def usun(self):
        print("Metoda usun klasy Figura.")

class Punkt(Figura):
    def __init__(self):
        print("Tworze obiekt klasy Punkt...")
    def wyswietl(self):
        print("Metoda wyswietl klasy Punkt.")
    def wypelnij(self):
        print("Metoda wypelnij klasy Punkt.")
    def usun(self):
        print("Metoda usun klasy Punkt.")

class Linia(Figura):
    def __init__(self):
        print("Tworze obiekt klasy Linia...")
    def wyswietl(self):
        print("Metoda wyswietl klasy Linia.")
    def wypelnij(self):
        print("Metoda wypelnij klasy Linia.")
    def usun(self):
        print("Metoda usun klasy Linia.")

class Kwadrat(Figura):
    def __init__(self):
        print("Tworze obiekt klasy Kwadrat...")
    def wyswietl(self):
        print("Metoda wyswietl klasy Kwadrat.")
    def wypelnij(self):
        print("Metoda wypelnij klasy Kwadrat.")
    def usun(self):
        print("Metoda usun klasy Kwadrat.")

class XXOkrag:
    def __init__(self):
        print("Tworze obiekt klasy XXOkrag...")
    def wyswietlaj(self):
        print("Metoda wyswietlaj klasy XXOkrag.")
    def wypelniaj(self):
        print("Metoda wypelniaj klasy XXOkrag.")
    def usuwaj(self):
        print("Metoda usuwaj klasy XXOkrag.")
    def pobierz_polozenie(self):
        print("Metoda pobierz_polozenie klasy XXOkrag.")
    def nadaj_polozenie(self):
        print("Metoda nadaj_polozenie klasy XXOkrag.")
    def ustaw_kolor(self):
        print("Metoda ustaw_kolor klasy XXOkrag.")

class Okrag(Figura):
    def __init__(self):
        self.xokrag = XXOkrag()
    def pobierz_polozenie(self):
        self.xokrag.pobierz_polozenie()
    def nadaj_polozenie(self):
        self.xokrag.nadaj_polozenie()
    def wyswietl(self):
        self.xokrag.wyswietlaj()
    def wypelnij(self):
        self.xokrag.wypelniaj()
    def nadaj_kolor(self):
        self.xokrag.ustaw_kolor()
    def usun(self):
        self.xokrag.usuwaj()

if __name__ == "__main__":

    lista_figur = [Linia(), Kwadrat(), Okrag()]

    for fig in lista_figur:
        fig.wyswietl()
