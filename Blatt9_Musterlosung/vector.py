class Vector:
    def __init__(self, lst: list):
        self._coords = lst[:]

    def __str__(self):
        return str(tuple(self._coords))

    def __len__(self):
        return len(self._coords)

    def __add__(self, other):
        if len(self) != len(other):
            print("Vektoren haben nicht die gleiche Länge!!")
            return Vector([])
        v = []
        for i in range(len(self)):
            v.append(self._coords[i] + other._coords[i])
        return Vector(v)
        # Alternativ
        # Vector([a + b for a, b in zip(self._coords, other._coords)])

    def __sub__(self, other):
        if len(self) != len(other):
            print("Vektoren haben nicht die gleiche Länge!!")
            return Vector([])
        v = []
        for i in range(len(self)):
            v.append(self._coords[i] - other._coords[i])
        return Vector(v)

    def __mul__(self, other):
        return Vector([number * other for number in self._coords])

    def __rmul__(self, other):
        return self.__mul__(other)

l = [1, 2, 3]
v1 = Vector(l)
v2 = Vector([4, 5, 6])
print(v1)
print(v2)
erg = 3 * v1 + v2 * 2
print(erg)
