"""
Na (1 pkt.):
- Zaimplementuj klasy: Rectangle, Square, Circle dziedziczące z klasy Figure
oraz definiujące jej metody:
    - Rectangle powinien mieć dwa atrybuty odpowiadające bokom (a i b)
    - Klasa Square powinna dziedziczyć z Rectangle.
    - Circle ma posiadać tylko atrybut r (radius).
- Przekształć metody we własności (properties).
---------
Na (2 pkt.):
- Zwiąż ze sobą boki a i b klasy Square (tzn. modyfikacja boku a lub boku b
powinna ustawiać tę samą wartość dla drugiego atrybutu).
- Zaimplementuj metody statyczne pozwalające na obliczenie pola
figury na podstawie podanych parametrów.
- Zaimplementuj classmethod "name" zwracającą nazwę klasy.
---------
Na (3 pkt.):
- Zaimplementuj klasę Diamond (romb) dziedziczącą z Figure,
po której będzie dziedziczyć Square,
tzn. Square dziediczy i z Diamond i Rectangle.
- Klasa wprowadza atrybuty przekątnych (e i f) oraz metody:
-- are_diagonals_equal: sprawdź równość przekątnych,
-- to_square: po sprawdzeniu równości przekątnych zwróci instancję
klasy Square o takich przekątnych.
- Zwiąż ze sobą atrybuty e i f (w klasie Diamond) oraz a, b, e i f
(w klasie Square)
"""
import math


class Figure:

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError

    @classmethod
    def name(cls):
        return cls.__name__

    def __str__(self):
        return (
            f'{self.name()}: area={self.area():.3f}, '
            f'perimeter={self.perimeter():.3f}'
        )


class Circle(Figure):
    _r = 0

    def __init__(self, r=None):
        if r is not None:
            self.r = r

    @property
    def r(self):
        return self._r

    @r.setter
    def r(self, arg):
        self._r = arg

    @staticmethod
    def calculate_area(r):
        return math.pi * r * r

    @staticmethod
    def calculate_perimeter(r):
        return math.pi * 2 * r

    def area(self):
        return self.calculate_area(self.r)

    def perimeter(self):
        return self.calculate_perimeter(self.r)


class Rectangle(Figure):
    _a = 0
    _b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, arg):
        self._a = arg

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, arg):
        self._b = arg

    @staticmethod
    def calculate_area(a, b):
        return a * b

    @staticmethod
    def calculate_perimeter(a, b):
        return a + a + b + b

    def area(self):
        return self.calculate_area(self.a, self.b)

    def perimeter(self):
        return self.calculate_perimeter(self.a, self.b)



class Diamond(Figure):
    _e = 1
    _f = 1

    def __init__(self, e, f):
        self.e = e
        self.f = f

    @property
    def e(self):
        return self._e

    @e.setter
    def e(self, arg):
        self._e = arg
        self._f *= (arg / self._e)

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, arg):
        self._f = arg
        self._e *= (arg / self._f)

    @staticmethod
    def calculate_area(e, f):
        return e * f / 2

    @staticmethod
    def calculate_perimeter(e, f):
        return 2 * math.sqrt((e*e+f*f))

    def area(self):
        return self.calculate_area(self.e, self.f)

    def perimeter(self):
        return self.calculate_perimeter(self.e, self.f)

    def are_diagonals_equal(self):
        if self.e == self.f:
            return True
        else:
            return False

    def to_square(self):
        if self.are_diagonals_equal():
            a = self.e / math.sqrt(2)
            return Square(a)
        else:
            return None


class Square(Rectangle, Diamond):

    def __init__(self, a, b=None):
        super().__init__(a, b=None)
        self.a = a
        self.b = a
        self.e = a * math.sqrt(2)

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        self._a = a
        self._b = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        self._a = b
        self._b = b



if __name__ == '__main__':
    kolo1 = Circle(1)
    assert str(kolo1) == 'Circle: area=3.142, perimeter=6.283'

    rec_1 = Rectangle(2, 4)
    assert str(rec_1) == 'Rectangle: area=8.000, perimeter=12.000'

    # print("Square")
    sqr_1 = Square(4)
    assert str(sqr_1) == 'Square: area=16.000, perimeter=16.000'

    diam_1 = Diamond(6, 8)
    assert str(diam_1) == 'Diamond: area=24.000, perimeter=20.000'

    diam_2 = Diamond(1, 1)
    assert str(diam_2) == 'Diamond: area=0.500, perimeter=2.828'

    sqr_3 = diam_2.to_square()
    assert str(sqr_3) == 'Square: area=0.500, perimeter=2.828'
