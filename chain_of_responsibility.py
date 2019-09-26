from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self, next_object=None):
        self.next_object = next_object

    @abstractmethod
    def handle_help(self):
        pass

    def has_help(self, name):
        print(name + ": Odebrałem żądanie wyświetlenia pomocy.")
        if callable(getattr(self, "show_help", None)):
            self.show_help()
        else:
            print(name + ": Nie mogę obsłużyć tego żądania, przekazuję dalej.")
            try:
                self.next_object.handle_help()
            except AttributeError:
                print("Nie ma kolejnego obiektu, żądanie nieobsłużone.")


class aPrintButton(Handler):
    def handle_help(self):
        super().has_help("aPrintButton")


class anOkButton(Handler):
    def handle_help(self):
        super().has_help("anOkButton")


class aSaveDialog(Handler):
    def handle_help(self):
        super().has_help("aSaveDialog")


class aPrintDialog(Handler):
    def handle_help(self):
        super().has_help("aPrintDialog")


class anApplication(Handler):
    def handle_help(self):
        super().has_help("anApplication")

    def show_help(self):
        print("anApplication: Wyświetlam pomoc.")


class Configuration:
    def __init__(self):
        self.app = anApplication()
        self.print_dialog = aPrintDialog(self.app)
        self.save_dialog = aSaveDialog(self.app)
        self.print_button = aPrintButton(self.print_dialog)
        self.ok_button = anOkButton(self.print_dialog)


if __name__ == '__main__':
    config = Configuration()
    config.print_button.handle_help()
