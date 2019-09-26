from collections import namedtuple

class Konfigurator:
    def __init__(self, kraj):
        self.kraje = {"pl": PodatekPolska(), "de": PodatekNiemcy()}
        self.kraj = self.kraje[kraj]

class Zamowienie:
    def __init__(self, towary, podatek):
        self.towary = towary
        if (isinstance(podatek, ObliczPodatek)):
            self.metoda_obliczania_podatku = podatek
        else:
            raise TypeError('To nie jest sposób obliczania podatku')
    def oblicz_podatek(self, przedmiot_sprzedazy, ilosc, cena):
        return self.metoda_obliczania_podatku.kwota_podatku(przedmiot_sprzedazy, ilosc, cena)

class ObliczPodatek:
    def kwota_podatku(self, przedmiot_sprzedazy, ilosc, cena):
        pass

class PodatekPolska(ObliczPodatek):
    def kwota_podatku(self, przedmiot_sprzedazy, ilosc, cena):
        return cena * ilosc * 0.23

class PodatekNiemcy(ObliczPodatek):
    def kwota_podatku(self, przedmiot_sprzedazy, ilosc, cena):
        return 15
    
def drukuj_paragon(tytul, zamowienie):
    print(tytul)
    linia = "---------------------------------------------------------"
    print(linia)
    print('{:<15s}{:>12s}{:>10s}{:>10s}{:>10s}'.format("Nazwa", "Netto (szt.)", "Podatek", "Ilość", "Brutto"))
    print(linia)
    suma_brutto = 0
    for towar in zamowienie.towary:
        kwota_podatku = zamowienie.oblicz_podatek(towar.nazwa, towar.ilosc, towar.cena)
        brutto = (towar.cena + kwota_podatku) * towar.ilosc
        print('{:<15s}{:>12.2f}{:>10.2f}{:>10d}{:>10.2f}'.format(towar.nazwa, towar.cena, kwota_podatku, towar.ilosc, brutto))
        suma_brutto += brutto
    print(linia)
    print('{:<15s}{:>42.2f}'.format("Suma:", suma_brutto))
    
if __name__ == '__main__':
    
    artykul = namedtuple("Artykuł", ["nazwa", "cena", "ilosc"])
    towary1 = [artykul("mysz", 25, 1), artykul("klawiatura", 30, 2), artykul("monitor", 450, 1)]
    towary2 = [artykul("szafka", 330, 1), artykul("biurko", 450, 1), artykul("krzeslo", 150, 3)]

    z1 = Zamowienie(towary1, Konfigurator("pl").kraj)
    z2 = Zamowienie(towary2, Konfigurator("de").kraj)

    print()
    drukuj_paragon("Zamówienie nr. 1, Polska:", z1)
    print("\n\n")
    drukuj_paragon("Zamówienie nr. 2, Niemcy:", z2)
    
