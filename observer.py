class Observer:
    def __init__(self):
        pass

    def update(self):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        if isinstance(observer, Observer):
            self.observers.append(observer)

    def detach(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify(self, subject):
        for observer in self.observers:
            observer.update(subject)


class ConcreteSubject(Subject):
    def __init__(self):
        super().__init__()
        self.state = 0

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        super().notify(self)


class ConcreteObserver(Observer):
    def __init__(self, subject):
        super().__init__()
        self.subject = subject
        subject.attach(self)
        self.observer_state = self.subject.get_state()

    def __del__(self):
        self.subject.detach(self)

    def update(self, subject):
        if self.subject == subject:
            self.observer_state = self.subject.get_state()
            print("Obserwowany obiekt zmienił stan.")
            print("Nowy stan: " + str(self.observer_state))


if __name__ == '__main__':
    subjects = [ConcreteSubject() for _ in range(5)] # tworzenie listy 5 przedmiotów obserwacji
    observers = [(ConcreteObserver(subject), ConcreteObserver(subject)) for subject in subjects] # tworzenie listy obserwatorów, po dwóch dla każdego obiektu

    print("-> Następuje zmiana stanu obiektu obserwowanego przez dwóch obserwatorów.")
    subjects[0].set_state(2)

    print("\n-> Dodanie trzeciego obserwatora do jednego z obiektów.")
    new_observer = ConcreteObserver(subjects[3])
    print("-> Następuje zmiana stanu obiektu obserwowanego przez trzech obserwatorów.")
    subjects[3].set_state(4)
