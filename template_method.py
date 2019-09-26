from abc import ABC, abstractmethod

class SzablonZapytania(ABC):
    def wykonaj_zapytanie(self, nazwadb, table, columns):
        print(self.formatuj_connect(nazwadb))
        print(self.formatuj_select(table, columns))

    @abstractmethod
    def formatuj_connect(self, nazwadb):
        pass

    @abstractmethod
    def formatuj_select(self, table, columns):
        pass
        
class ZapytanieSQLServer(SzablonZapytania):
    def formatuj_connect(self, nazwadb):
        return "Łączenie z SQL Server " + nazwadb + "..."

    def formatuj_select(self, table, columns="*"):
        return "SELECT " + columns + " FROM " + table

class ZapytanieOracle(SzablonZapytania):
    def formatuj_connect(self, nazwadb):
        return "Łączenie z bazą Oracle " + nazwadb + "..."

    def formatuj_select(self, table, columns="*"):
        return "SELECT " + columns + " FROM " + table + ";"

if __name__ == '__main__':
    z1 = ZapytanieSQLServer()
    z2 = ZapytanieOracle()
    lista_zapytan = [z1, z2]
    for zapytanie in lista_zapytan:
        zapytanie.wykonaj_zapytanie("nazwa_bazy", "pracownicy", "imie, nazwisko")
        print()
