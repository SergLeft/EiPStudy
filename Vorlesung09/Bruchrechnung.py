class Bruch:
    def __init__(self,zaehler,nenner = 1):
        self.z = zaehler
        self.n = nenner

    def __add__(self, other):
        ergebnis_zaehler = self.z * other.n + self.n * other.z
        ergebnis_nenner = self.n * other.n
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __sub__(self, other):
        ergebnis_zaehler = self.z * other.n - self.n * other.z
        ergebnis_nenner = self.n * other.n
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __mul__(self, other):
        ergebnis_zaehler = self.z * other.z
        ergebnis_nenner = self.n * other.n
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __truediv__(self, other):
        ergebnis_zaehler = self.z * other.n
        ergebnis_nenner = self.n * other.z
        return(Bruch(ergebnis_zaehler,ergebnis_nenner).reduce())

    def __neg__(self):
        return(Bruch(-self.z,self.n))

    def __str__(self):
        if self.n == 1:
            return(str(self.z))
        return(str(self.z)+'/'+str(self.n))

    def __lt__(self, other):
        if self.n * other.n > 0:
            return(self.z * other.n < self.n * other.z)
        else:
            return (self.z * other.n > self.n * other.z)

    def __eq__(self, other):
            return(self.z * other.n == self.n * other.z)

    def reduce(self):
        g = Bruch.ggT(self.z,self.n)
        return(Bruch(self.z // g,self.n // g))

    def ggT(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return(a)

a = Bruch(1,2)
b = -Bruch(2,3) # Bruch(2,3).__neg__()
c = a + b # a.__add__(b)
d = a / b # a.__truediv__(b)
L = [a,b,c,d]
L.sort() # sort verwendet intern __lt__

for x in L:
    print(x)

a = Bruch(1,2)
b = Bruch(1,2)
print(a == b) # a.__eq__(b)
# Wenn __eq__ nicht überladen wäre, würde == nur die Verweise der Objekte auf ihren Speicherort
# vergleichen und da a und b auf unterschiedliche Speicherorte verweisen, wäre das Ergebnis dieses
# Vergleichs False
