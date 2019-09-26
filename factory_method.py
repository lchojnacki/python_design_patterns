from abc import ABC, abstractmethod

class Creator(ABC):
    @abstractmethod
    def utworz_bd(self):
        pass

class CreatorSQLServer(Creator):
    def utworz_bd(self):
        print("Tworzenie bazy SQL Server...")
        return ZapytanieSQLServer()

class CreatorOracle(Creator):
    def utworz_bd(self):
        print("Tworzenie bazy Oracle...")
        return ZapytanieOracle()

class SzablonZapytania(ABC):
    @staticmethod
    def wykonaj_zapytanie(creator, nazwadb, table, columns):
        creator = creator.utworz_bd()
        print(creator.formatuj_connect(nazwadb))
        print(creator.formatuj_select(table, columns))

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

    def utworz_bd(self):
        return ZapytanieSQLServer()

class ZapytanieOracle(SzablonZapytania):
    def formatuj_connect(self, nazwadb):
        return "Łączenie z bazą Oracle " + nazwadb + "..."

    def formatuj_select(self, table, columns="*"):
        return "SELECT " + columns + " FROM " + table + ";"

    def utworz_bd(self):
        return ZapytanieOracle()

if __name__ == '__main__':
    c1 = CreatorOracle()
    c2 = CreatorSQLServer()
    lista_creator = [c1, c2]
    for creator in lista_creator:
        SzablonZapytania.wykonaj_zapytanie(creator, "nazwa_bazy", "pracownicy", "imie, nazwisko")
        print()
