from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_mammal(self, mammal):
        pass

    @abstractmethod
    def visit_bird(self, bird):
        pass

    @abstractmethod
    def visit_reptile(self, reptile):
        pass

    @abstractmethod
    def visit_fish(self, fish):
        pass


class SumVisitor(Visitor):
    def __init__(self):
        self.sum = 0

    def visit_mammal(self, mammal):
        self.sum += mammal.price

    def visit_bird(self, bird):
        self.sum += bird.price

    def visit_reptile(self, reptile):
        self.sum += reptile.price

    def visit_fish(self, fish):
        self.sum += fish.price


class SumBlackVisitor(Visitor):
    def __init__(self):
        self.black_sum = 0

    def visit_mammal(self, mammal):
        self.black_sum += mammal.price

    def visit_bird(self, bird):
        self.black_sum += bird.black_price

    def visit_reptile(self, reptile):
        self.black_sum += reptile.price

    def visit_fish(self, fish):
        self.black_sum += fish.price


class VetVisitor(Visitor):
    def __init__(self):
        pass

    def visit_mammal(self, mammal):
        print("Odwiedzone zwierzę: ssak.")
        if mammal.healthy:
            print("Diagnoza: zdrowy.")
        else:
            print("Diagnoza: choroba. Leczenie: antybiotyki.")
        print()

    def visit_bird(self, bird):
        print("Odwiedzone zwierzę: ptak")
        if bird.healthy:
            print("Diagnoza: zdrowy.")
        else:
            if bird.black_price > (2 * bird.price):
                print("Diagnoza: choroba. Leczenie: transport do lecznicy.")
            else:
                print("Diagnoza: choroba. Leczenie: antybiotyki, dieta.")
        print()

    def visit_reptile(self, reptile):
        print("Odwiedzone zwierzę: gad.")
        if reptile.healthy:
            print("Diagnoza: zdrowy.")
        else:
            print("Diagnoza: choroba. Leczenie: antybiotyki.")
        print()

    def visit_fish(self, fish):
        print("Odwiedzone zwierzę: ryba.")
        if fish.healthy:
            print("Diagnoza: zdrowy.")
        else:
            print("Diagnoza: choroba. Leczenie: antybiotyki.")
        print()


class Animal(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Mammal(Animal):
    def __init__(self, healthy=True, price=500):
        self.healthy = healthy
        self.price = price

    def accept(self, visitor):
        visitor.visit_mammal(self)


class Bird(Animal):
    def __init__(self, healthy=True, price=350, black_price=500):
        self.healthy = healthy
        self.price = price
        self.black_price = black_price

    def accept(self, visitor):
        visitor.visit_bird(self)


class Reptile(Animal):
    def __init__(self, healthy=True, price=250):
        self.healthy = healthy
        self.price = price

    def accept(self, visitor):
        visitor.visit_reptile(self)


class Fish(Animal):
    def __init__(self, healthy=True, price=50):
        self.healthy = healthy
        self.price = price

    def accept(self, visitor):
        visitor.visit_fish(self)


if __name__ == '__main__':
    animals = [Fish(price=20), Bird(healthy=False, price=50, black_price=80), Mammal(), Reptile(),
               Fish(healthy=False, price=10), Bird(), Mammal(healthy=False, price=200),
               Reptile(healthy=False, price=50), Bird(healthy=False, price=80, black_price=200), Mammal(price=1000)]

    visitor_price = SumVisitor()
    visitor_black_price = SumBlackVisitor()
    visitor_vet = VetVisitor()

    print("Zwierzęta w kolekcji:")
    for animal in animals:
        print(animal.__class__.__name__)

    for animal in animals:
        animal.accept(visitor_price)

    print("Suma cen zwierząt w kolekcji: " + str(visitor_price.sum))

    for animal in animals:
        animal.accept(visitor_black_price)

    print("Suma cen czarnorynkowych: " + str(visitor_black_price.black_sum))

    for animal in animals:
        animal.accept(visitor_vet)
