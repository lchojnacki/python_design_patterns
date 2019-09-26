from abc import ABC, abstractmethod


class File:
    def __init__(self):
        self.__state = FileClosed()

    def __str__(self):
        return str(type(self))

    def open(self):
        self.__state.open(self)

    def close(self):
        self.__state.close(self)

    def read(self):
        self.__state.read(self)

    def write(self):
        self.__state.write(self)

    def change_state(self, new_state):
        self.__state = new_state


class FileState(ABC):
    @abstractmethod
    def open(self, obj):
        pass

    @abstractmethod
    def close(self, obj):
        pass

    @abstractmethod
    def read(self, obj):
        pass

    @abstractmethod
    def write(self, obj):
        pass

    @staticmethod
    def change_file_state(file, state):
        if isinstance(file, File):
            file.change_state(state)


class FileOpened(FileState):
    def open(self, obj):
        print("Plik " + str(obj) + " jest już otwarty.")

    def close(self, obj):
        print("Zamykam plik " + str(obj) + "...")
        super().change_file_state(obj, FileClosed())
        print("Plik " + str(obj) + " został zamknięty.")

    def read(self, obj):
        print("Wyświetlam zawartość pliku " + str(obj) + ".")

    def write(self, obj):
        print("Piszę do pliku ")


class FileClosed(FileState):
    def open(self, obj):
        print("Otwieram plik " + str(obj) + "...")
        super().change_file_state(obj, FileOpened())
        print("Plik został otwarty.")

    def close(self, obj):
        print("Plik " + str(obj) + " jest już zamknięty.")

    def read(self, obj):
        print("Nie możesz czytać, plik " + str(obj) + " jest zamknięty.")

    def write(self, obj):
        print("Nie możesz pisać, plik " + str(obj) + " jest zamknięty.")


if __name__ == '__main__':
    f = File()
    f.write()
    f.read()
    f.close()
    f.open()
    f.write()
    f.read()
    f.open()
    f.close()
