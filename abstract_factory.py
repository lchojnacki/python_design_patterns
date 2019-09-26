from abc import ABC, abstractmethod # moduł Abstract Base Class

class Konfiguracja:
    def __init__(self):
        self.niska_rozdzielczosc = FabrykaNisRozdz()
        self.wysoka_rozdzielczosc = FabrykaWysRozdz()

    def poierz_sterownik_niskiej_rozdzielczosci(self):
        return self.niska_rozdzielczosc
    
    def poierz_sterownik_wysokiej_rozdzielczosci(self):
        return self.wysoka_rozdzielczosc

class FabrykaSter(ABC):
    @abstractmethod
    def pobierz_sterownik_ekranu(self):
        pass
    @abstractmethod
    def pobierz_sterownik_drukarki(self):
        pass

class FabrykaNisRozdz(FabrykaSter):
    def __init__(self):
        pass
    def pobierz_sterownik_ekranu(self):
        return SENR()
    def pobierz_sterownik_drukarki(self):
        return SDNR()

class FabrykaWysRozdz(FabrykaSter):
    def __init__(self):
        pass
    def pobierz_sterownik_ekranu(self):
        return SEWR()
    def pobierz_sterownik_drukarki(self):
        return SDWR()

class ApNadzorujaca:
    def __init__(self, fabryka):
        self.sterownik_drukarki = fabryka.pobierz_sterownik_drukarki()
        self.sterownik_ekranu = fabryka.pobierz_sterownik_ekranu()
    def rysuj(self):
        self.sterownik_ekranu.rysuj()
    def drukuj(self):
        self.sterownik_drukarki.drukuj()

class SterownikEkranu(ABC):
    @abstractmethod
    def rysuj(self):
        pass

class SterEkrnNisRozdz(SterownikEkranu):
    def __init__(self):
        self.sterownik = SENR()
    def rysuj(self):
        self.sterownik.rysuj()

class SENR:
    def __init__(self):
        self.tekst = "Rysuję figurę za pomocą sterownika ekranu niskiej rozdzielczości."
    def rysuj(self):
        print(self.tekst)

class SterEkrnWysRozdz(SterownikEkranu):
    def __init__(self):
        self.sterownik = SEWR()
    def rysuj(self):
        self.sterownik.rysuj()
    
class SEWR:
    def __init__(self):
        self.tekst = "Rysuję figurę za pomocą sterownika ekranu wysokiej rozdzielczości."
    def rysuj(self):
        print(self.tekst)

class SterownikDrukarki(ABC):
    @abstractmethod
    def drukuj(self):
        pass
    
class SterDrukNisRozdz(SterownikDrukarki):
    def __init__(self):
        self.sterownik = SDNR()
    def drukuj(self):
        self.sterownik.drukuj()

class SDNR:
    def __init__(self):
        self.tekst = "Drukuję figurę za pomocą sterownika drukarki niskiej rozdzielczości."
    def drukuj(self):
        print(self.tekst)

class SterDrukWysRozdz(SterownikDrukarki):
    def __init__(self):
        self.sterownik = SDWR()
    def drukuj(self):
        self.sterownik.drukuj()

class SDWR:
    def __init__(self):
        self.tekst = "Drukuję figurę za pomocą sterownika drukarki wysokiej rozdzielczości."
    def drukuj(self):
        print(self.tekst)

if __name__ == '__main__':
    konf = Konfiguracja()

    ap = ApNadzorujaca(konf.poierz_sterownik_niskiej_rozdzielczosci())
    ap.drukuj()
    ap.rysuj()

    print()

    ap = ApNadzorujaca(konf.poierz_sterownik_wysokiej_rozdzielczosci())
    ap.rysuj()
    ap.drukuj()