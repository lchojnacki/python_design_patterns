class Konfiguracja:
    def pobierz_potwierdzenie(self, numer):
        if numer == 1:
            return DekoratorNaglowka1(DekoratorNaglowka2(DekoratorStopki1(Potwierdzenie())))
        else:
            return DekoratorNaglowka1(DekoratorStopki2(DekoratorStopki1(Potwierdzenie())))
        

class Komponent:
    def __init__(self):
        self.konf = Konfiguracja()

    def drukuj(self, numer):
        self.konf.pobierz_potwierdzenie(numer).drukuj()


class Potwierdzenie(Komponent):
    def __init__(self):
        self.tekst = "POTWIERDZENIE"

    def drukuj(self):
        print(self.tekst)
    
class DekoratorPotwierdzenia(Komponent):
    def __init__(self, komponent):
        self.moj_komponent = komponent

    def drukuj(self):
        if (self.moj_komponent):
            self.moj_komponent.drukuj()

class DekoratorNaglowka1(DekoratorPotwierdzenia):
    def __init__(self, obj):
        self.naglowek = Naglowek1()
        self.obj = obj

    def drukuj_naglowek(self):
        self.naglowek.drukuj()

    def drukuj(self):
        self.drukuj_naglowek()
        self.obj.drukuj()

class DekoratorNaglowka2(DekoratorPotwierdzenia):
    def __init__(self, obj):
        self.naglowek = Naglowek2()
        self.obj = obj

    def drukuj_naglowek(self):
        self.naglowek.drukuj()

    def drukuj(self):
        self.drukuj_naglowek()
        self.obj.drukuj()

class DekoratorStopki1(DekoratorPotwierdzenia):
    def __init__(self, obj):
        self.stopka = Stopka1()
        self.obj = obj

    def drukuj_stopke(self):
        self.stopka.drukuj()

    def drukuj(self):
        self.obj.drukuj()
        self.drukuj_stopke()

class DekoratorStopki2(DekoratorPotwierdzenia):
    def __init__(self, obj):
        self.stopka = Stopka2()
        self.obj = obj

    def drukuj_stopke(self):
        self.stopka.drukuj()

    def drukuj(self):
        self.obj.drukuj()
        self.drukuj_stopke()

class Naglowek1(DekoratorPotwierdzenia):
    def __init__(self):
        self.tekst = "NAGŁÓWEK 1"

    def drukuj(self):
        print(self.tekst)
    
class Naglowek2(DekoratorPotwierdzenia):
    def __init__(self):
        self.tekst = "NAGŁÓWEK 2"
    
    def drukuj(self):
        print(self.tekst)

class Stopka1(DekoratorPotwierdzenia):
    def __init__(self):
        self.tekst = "STOPKA 1"
    
    def drukuj(self):
        print(self.tekst)

class Stopka2(DekoratorPotwierdzenia):
    def __init__(self):
        self.tekst = "STOPKA 2"
    
    def drukuj(self):
        print(self.tekst)

if __name__ == '__main__':
    komponent = Komponent()
    komponent.drukuj(1)
    print()
    komponent.drukuj(2)