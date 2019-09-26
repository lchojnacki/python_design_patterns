class Graphic:
    def __init__(self):
        self.elements = []
    def draw(self):
        pass
    def add(self, element):
        self.elements.append(element)
    def remove(self, element):
        i = self.elements.index(element)
        del self.elements[i]
    def get_child(self, i):
        return self.elements[i]

class Line(Graphic):
    def draw(self):
        print("Rysuję linię...")

class Rectangle(Graphic):
    def draw(self):
        print("Rysuję prostokąt...")

class Text(Graphic):
    def draw(self):
        print("Rysuję tekst...")

class Picture(Graphic):
    def __init__(self):
        self.graphics = []
    def draw(self):
        print("Rysuję obrazek...")
        for g in self.graphics:
            g.draw()
        print("Obrazek narysowany!")
    def add(self, graphic):
        self.graphics.append(graphic)
    def remove(self, graphic):
        i = self.graphics.index(graphic)
        del self.graphics[i]
    def get_child(self, i):
        return self.graphics[i]

if __name__ == "__main__":
    
    p = Picture()
    p.add(Line())
    p.add(Rectangle())
    
    p2 = Picture()
    p2.add(Text())
    p2.add(Line())
    p2.add(Rectangle())
    
    p.add(p2)
    p.add(Line())

    p.draw()