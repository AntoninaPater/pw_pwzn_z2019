"""
Częśćć 1 (1 pkt): Uzupełnij klasę Vector tak by reprezentowała wielowymiarowy wektor.
Klasa posiada przeładowane operatory równości, dodawania, odejmowania,
mnożenia (przez liczbę i skalarnego), długości
oraz nieedytowalny (własność) wymiar.
Wszystkie operacje sprawdzają wymiar.
Część 2 (1 pkt): Klasa ma statyczną metodę wylicznia wektora z dwóch punktów
oraz metodę fabryki korzystającą z metody statycznej tworzącej nowy wektor
z dwóch punktów.
Wszystkie metody sprawdzają wymiar.
"""


class Vector:
    dim = None  # Wymiar vectora

    @property
    def len(self):
        tmp = tuple(i ** 2 for i in self.values)
        length = sum(tmp) ** 0.5
        return length

    def __init__(self, *args):
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args
            self.dim = len(args)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            if self.dim != other.dim:
                raise ValueError
            else:
                result = tuple(a + b for a, b in zip(self.values, other.values))
                return Vector(*result)
        else:
            raise NotImplemented

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            if self.dim != other.dim:
                raise ValueError
            else:
                result = tuple(a - b for a, b in zip(self.values, other.values))
                return Vector(*result)
        else:
            raise NotImplemented

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            if self.dim != other.dim:
                raise ValueError
            else:
                result = sum(a * b for a, b in zip(self.values, other.values))
                return result
        else:
            result = tuple(a * other for a in self.values)
            return Vector(*result)

    def __eq__(self, other):
        if isinstance(other, Vector):
            if self.dim != other.dim:
                raise ValueError
            else:
                return self.values == other.values

        else:
            return self.values == other


    def __len__(self):
        tmp = sum(1 for i in self.values)
        # length = sum(tmp) ** 0.5
        return int(tmp)



    @staticmethod
    def calculate_vector(beg, end):
        """
        Calculate vector from given points

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: Calculated vector
        :rtype: tuple
        """
        beg = Vector(*beg)
        end = Vector(*end)

        if beg.dim != end.dim:
            raise ValueError
        else:
            vec = end - beg
            return tuple(vec.values)


    @classmethod
    def from_points(cls, beg, end):
        """"""
        """
        Generate vector from given points.

        :param beg: Begging point
        :type beg: list, tuple
        :param end: End point
        :type end: list, tuple
        :return: New vector
        :rtype: tuple
        """
        raise NotImplemented


if __name__ == '__main__':
    v1 = Vector(1,2,3)
    v2 = Vector(1,2,3)
    assert v1 + v2 == Vector(2,4,6)
    assert v1 - v2 == Vector(0,0,0)
    assert v1 * 2 == Vector(2,4,6)
    assert v1 * v2 == 14
    assert len(Vector(3,4)) == 5.
    assert Vector.calculate_vector([0, 0, 0], [1,2,3]) == (1,2,3)
    assert Vector.from_points([0, 0, 0], [1,2,3]) == Vector(1,2,3)
