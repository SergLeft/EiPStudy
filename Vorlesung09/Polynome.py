# Die Klasse Bruch ist eine Schablone für das Erstellen von einzelnen Objekten
# dieses Typs. Man sagt auch: Objekte vom Typ Bruch sind Instanzen der Klasse Bruch.
# Ein Bruch besitzt als Attribute (Membervariablen) seinen Zähler z und seinen Nenner n.
# Darüber hinaus definieren wir eine Vielzahl von Operationen (Memberfunktionen) zum Rechnen
# mit Brüchen. Wir überladen insbesondere die arithmetischen Operatoren.

class Bruch:

    def __init__(self,zaehler,nenner = 1):
        # Der Konstruktor für Brüche. Falls kein Nenner beim Aufruf des Konstruktors
        # angegeben wird, wird als Default-Wert der Wert 1 verwendet.

        # Die Membervariablen werden initialisiert. Jedes erzeugte Bruch-Objekt
        # besitzt seine eigenen Zähler- und Nenner-Variablen.
        self.z = zaehler
        self.n = nenner

    def ggT(a,b):
        # Eine Klassenfunktion (nicht zu verwechseln mit einer Memberfunktion) besitzt
        # kein self-Argument und kann nur in der Form Klassenname.Klassenfunktion
        # aufgerufen werden.
        # ggT-Berechnung nach dem Euklidschen Algorithmus
        while b != 0:
            r = a % b
            a = b
            b = r
        return(a)

    def reduce(self):
        # Eine Memberfunktion, die dazu dient, dass ein gekürzter Bruch entsteht.
        # Aufruf der Klassenfunktion ggT.
        g = Bruch.ggT(self.z,self.n)
        # Rückgabe des gekürzten neuen Bruches.
        return(Bruch(self.z//g,self.n//g))

    def __str__(self):
        # Eine Memberfunktion zur Darstellung eines Bruches als Zeichenkette.
        # Überladung der str-Funktion.
        if self.n == 1:
            return str(self.z)
        return(str(self.z)+'/'+str(self.n))

    def __neg__(self):
        # Eine Memberfunktion für das unäre Minus. Z.B. a = -Bruch(1,2)
        return(Bruch(-self.z,self.n))

    def __add__(self,other):
        # Eine Memberfunktion zur Addition zweier Brüche.
        # Überladen des + Operators.
        # c = a + b  entspricht c = a.__add__(b),
        # d.h a ist das self-Objekt und b das other-Objekt.

        c = Bruch(self.z*other.n+self.n*other.z,self.n*other.n)
        # Als Ergebnis wird stets ein gekürzter Bruch zurückgeliefert.
        return(c.reduce())

    def __sub__(self,other):
        # Eine Memberfunktion zur Subtraktion zweier Brüche.
        # Überladen des - Operators.
        c = Bruch(self.z*other.n-self.n*other.z,self.n*other.n)
        return(c.reduce())

    def __mul__(self,other):
        # Eine Memberfunktion zur Multiplikation zweier Brüche.
        # Überladen des * Operators.
        c = Bruch(self.z*other.z,self.n*other.n)
        return(c.reduce())

    def __lt__(self,other):
        # Eine Memberfunktion zum Vergleich zweier Brüche.
        # Überladen des < Operators.
        return(self.z * other.n < self.n * other.z)

    def __truediv__(self,other):
        # Eine Memberfunktion zur Division zweier Brüche.
        # Überladen des / Operators.
        c = Bruch(self.z*other.n,self.n*other.z)
        # Wir wollen das Vorzeichen des Bruches im Zähler speichern.
        # Der Nenner soll stets positiv sein.
        if c.n < 0:
            c.z = -c.z
            c.n = -c.n
        return(c.reduce())

    def isZero(self):
        # Eine Memberfunktion zur Überprüfung, ob der gegebene Bruch 0 ist.
        return(self.z == 0)


# Eine Klasse zur Darstellung von univariaten Polynomen mit rationalen Koeffizienten.
class Polynom:
    def __init__(self,coeff):
        # Der Konstruktor für die Polynomklasse.

        # Die Koeffizienten des Polynoms sollen Brüche sein. 
        # Sie werden in einem Feld namens c gespeichert.
        # Wir fertigen eine Kopie des Koeffizientenfeldes coeff an.
        self.c = coeff[:]

    def __getitem__(self,i):
        # Wir überladen den [] Operator, um einfacher auf Koeffizienten zugreifen zu können.
        return(self.c[i])

    def grad(self):
        # Wir ermitteln den Grad des gegebenen Polynoms anhand der Länge des Koeffizientenfeldes.
        return(len(self.c)-1)

    def __str__(self):
        # Wir stellen unser Polynom in der Variable x als Zeichenkette dar.
        if self.isZero():
            return '0'
        s = ''
        for i in range(self.grad(),-1,-1):
            if self[i].z == 0:
                continue
            if self[i].z > 0 and i < self.grad():
                s += '+'
            s += str(self[i])
            if i > 1:
                s += 'x^'+str(i)
            elif i == 1:
                s += 'x'

        return(s)

    # Zur einfacheren Dokumentation der Polynomarithmetik stehe
    # self für ein Polynom a(x) = a_n*x^n+...+a_1*x+a_0 = sum_{i=0}^n a_i*x^i
    # und other für b(x) = b_m*x^m+...+b_1*x+b_0 = sum_{j=0}^m b_j*x^j

    def __add__(self,other):
        # Wir überladen den + Operator, um die beiden Polynome zu addieren.
        # a(x)+b(x) = sum_{i=0}^max(n,m) (a_i+b_i)*x^i, wobei a_i = 0 für i > n und b_j = 0 für j > m
        # grad(a(x)+b(x)) <= max(grad(a(x),grad(b(x)) = max(n,m)

        # Wir ermitteln die Koeffizienten des Ergebnispolynoms.
        h = [Bruch(0) for i in range(0,max(self.grad(),other.grad())+1)]
        for i in range(0,self.grad()+1):
            h[i] = self[i]
        for j in range(0,other.grad()+1):
            h[j] = h[j] + other[j]
        # Wir eliminieren führende Nullkoeffizienten, dadurch kann der Grad des Ergebnispolynoms sinken.
        for i in range(len(h)-1,0,-1):
            if h[i].isZero():
                h.pop()
            else:
                break
        # Aus dem berechneten Koeffizientenfeld bauen wir ein neues Polynom
        # und geben dieses zurück.
        return(Polynom(h))

    def __mul__(self,other):
        # Wir überladen den * Operator.
        # a(x)*b(x) = sum_{i=0}^n sum_{j=0}^m a_i*b_j*x^(i+j)
        # grad(a(x)*b(x)) = grad(a(x))+grad(b(x)) = n + m
        h = [Bruch(0) for i in range(0,self.grad()+other.grad()+1)]
        for i in range(0,self.grad()+1):
            for j in range(0,other.grad()+1):
                h[i+j] = h[i+j] + self[i] * other[j]
        return(Polynom(h))

    def __pow__(self,other):
        # Wir überladen den ** Operator, zur Potenzierung eines Polynoms.
        # a(x)^n = prod_{i=0}^{n-1} a(x)
        poly = Polynom([Bruch(1)])
        # Naive Implementierung der Potenzierung durch wiederholte Multiplikation
        for i in range(0,other):
            poly = poly * self
        return(poly)

    def __truediv__(self,other):
        # Wir überladen den / Operator zur Polynomdivision.
        # Algorithmus zur Polynomdivision siehe https://de.wikipedia.org/wiki/Polynomdivision
        if self.grad() < other.grad():
            return Polynom([Bruch(0)])
        h = [Bruch(0) for i in range(0,self.grad()-other.grad()+1)]
        r = self[:]
        c = other[other.grad()]
        for i in range(self.grad()-other.grad(),-1,-1):
            h[i] = r[i+other.grad()] / c
            for j in range(other.grad(),-1,-1):
                r[i+j] = r[i+j] - other[j]*h[i]

        return(Polynom(h))

    def __mod__(self,other):
        # Wir überladen den % Operator zur Bestimmung des Restes bei der Polynomdivision.
        # Algorithmus siehe oben.
        if self.grad() < other.grad():
            return Polynom([Bruch(0)])
        h = [Bruch(0) for i in range(0,self.grad()-other.grad()+1)]
        r = self[:]
        c = other[other.grad()]
        for i in range(self.grad()-other.grad(),-1,-1):
            h[i] = r[i+other.grad()] / c
            for j in range(other.grad(),-1,-1):
                r[i+j] = r[i+j] - other[j]*h[i]
        for i in range(len(r)-1,0,-1):
            if r[i].isZero():
                r.pop()
            else:
                break

        return(Polynom(r))

    def isZero(self):
        # Eine Memberfunktion zur Überprüfung, ob das gegebene Polynom das Nullpolynom ist.
        if self.grad() > 0:
            return False
        return(self[0].isZero())

    def diff(self):
        # Eine Memberfunktion zur Differentiation des gegebenen Polynoms.
        h = []
        for i in range(1,self.grad()+1):
            h.append(Bruch(i)*self[i])
        return(Polynom(h))

    def ggT(self,other):
        # Eine Memberfunktion zur Bestimmung des größten gemeinsamen Teilers
        # für zwei Polynome nach dem Euklidschen Algorithmus.
        # Man beachte die Analogie zum Euklidschen Algorithmus für ganze Zahlen.
        a = Polynom(self)
        b = Polynom(other)
        while not b.isZero():
            r = a % b
            a = b
            b = r
        return(a)

# Wir konstruieren drei Brüche.
a = Bruch(1)
# Ausgabe des ersten Bruches und seines Typs.
print(a,type(a))
b = -Bruch(2)
c = Bruch(5)

# Wir konstruieren ein Polynom aus einem Feld von drei rationalen Koeffizienten.
f = Polynom([a,b,c])
# Ausgabe des Polynoms und seines Typs.
print(f,type(f))
# Ein weiteres Polynom.
g = Polynom([c,a,b,a])
# Noch ein Polynom.
h = f**2*g
print(h)
# Wir wollen überprüfen, ob das Polynom h Mehrfachnullstellen besitzt.
# Dazu berechnen wir den ggT(h,h').
d = h.diff()
e = h.ggT(d)
print(e)
print(e / Polynom([e[0]]))




