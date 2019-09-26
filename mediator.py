class Mediator:
    def __init__(self):
        self.checks = []

    def update(self, sender):
        if sender.checked:
            # Jeśli wyzwalający checkbox został zaznaczony
            index = self.checks.index(sender)
            for i in range(index, 0, -1):
                self.checks[i-1].checked = True
        else:
            # Jeśli wyzwalający checkbox został odznaczony
            index = self.checks.index(sender)
            for i in range(index, len(self.checks)):
                self.checks[i].checked = False


class Checkbox:
    def __init__(self, text, my_mediator):
        super().__init__()
        self.text = text
        self.checked = False
        self.mediator = my_mediator
        self.mediator.checks.append(self)

    def click(self):
        print("Clicked: " + self.text)
        self.checked = not self.checked
        self.mediator.update(self)


class Menu:
    def __init__(self):
        self.checks = []

    def __str__(self):
        text = ""
        if len(self.checks) > 0:
            for i in range(len(self.checks)):
                    text += str(i+1) + ". " + self.checks[i].text + "\t\t\t" + ("X" if self.checks[i].checked else "") \
                            + "\n"
            text += str(i+2) + ". Wyjście z programu"
        else:
            text += "Menu jest puste!"
        return text

    def add_checkbox(self, checkbox):
        self.checks.append(checkbox)


if __name__ == '__main__':
    mediator = Mediator()
    menu = Menu()
    menu.add_checkbox(Checkbox("Ćwiczenia zaliczone", mediator))
    menu.add_checkbox(Checkbox("Egzamin zaliczony", mediator))
    menu.add_checkbox(Checkbox("Przedmiot zaliczony", mediator))

    while True:
        print(menu)
        key = input()
        if key == '1':
            menu.checks[0].click()
        elif key == '2':
            menu.checks[1].click()
        elif key == '3':
            menu.checks[2].click()
        else:
            break
