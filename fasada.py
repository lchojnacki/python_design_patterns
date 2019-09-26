class Wektor3d:
    def __init__(self, x = 0, y = 0, z = 0):
        self._x = x
        self._y = y
        self._z = z
    
    def __add__(self, other):
        if (type(self) == type(other)):
            return Wektor3d(self._x + other._x,
                            self._y + other._y,
                            self._x + other._z)
    
    def __mul__(self, k):
        return Wektor3d(k * self._x, k * self._y, k * self._z)

    def __str__(self):
        return "[" + str(self._x) + ", " + str(self._y) + ", " + str(self._z) + "]"


class Wektor2d:
    def __init__(self, x = 0, y = 0):
        self.w3d = Wektor3d(x, y, 0)
    
    def __add__(self, other):
        if (type(self) == type(other)):
            return Wektor2d(self.w3d._x + other.w3d._x,
                            self.w3d._y + other.w3d._y)
    
    def __mul__(self, k):
        return Wektor2d(k * self.w3d._x, k * self.w3d._y)

    def __str__(self):
        return "[" + str(self.w3d._x) + ", " + str(self.w3d._y) + "]"


if __name__ == "__main__":
    w31 = Wektor3d()
    w32 = Wektor3d(3, 4, 5)

    print("Pierwszy wektor 3D: " + str(w31))
    print("Drugi wektor 3D: " + str(w32))

    w21 = Wektor2d()
    w22 = Wektor2d(3, 4)
    w23 = Wektor2d(1, 2)

    print("Pierwszy wektor 2D: " + str(w21))
    print("Drugi wektor 2D: " + str(w22))
    print("Trzeci wektor 2D: " + str(w23))
    print("Suma wektora drugiego i trzecego: " + str(w22+w23))
    print("Wektor trzeci pomnożony przez 4: " + str(w23 * 4))
