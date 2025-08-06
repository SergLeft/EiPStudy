"""'Zwei Kreisscheiben Ki und Kj schneiden sich genau dann, wenn der Abstand ihrer Mittelpunkte kleiner oder gleich der Summe ihrer Radien ist'
Eine Kreisscheibe mit Radius ri reicht vom Mittelpunkt Mi aus maximal ri Einheiten weit, analog reicht Kreisscheibe Kj
maximal rj Einheiten von Mj aus. Die beiden Kreisscheiben können sich nur dann berühren oder überlappen, wenn ihre
"Reichweiten" zusammen (ri + rj) mindestens so groß sind wie der Abstand ihrer Mittelpunkte d(Mi, Mj). Ist der
Mittelpunktsabstand größer als ri + rj, bleibt eine Lücke zwischen den Kreisscheiben, sodass sie sich nicht schneiden
können.
"""

"""Eine Kreisscheibe Ki liegt genau dann vollständig in der Kreisscheibe Kj, wenn die Summe von ri und der Distanz der 
Mittelpunkte kleiner ist als rj."""

class Kreis:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"Kreis mit Mittelpunkt ({self.x} ,{self.y}) und Radius {self.r}"

    def __repr__(self):
        return str(self)

    def __contains__(self, other: "Kreis"):
        dist = ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return (dist + other.r) < self.r

    def schneidet(self, item: "Kreis"):
        dist = (self.x - item.x) ** 2 + (self.y - item.y) ** 2
        return dist <= (self.r + item.r)**2

    def __lt__(self, other):
        return self.r < other.r

K1 = Kreis (14 , 3 , 2)
K2 = Kreis (10 , 13 , 3)
K3 = Kreis (8 , 12 , 6)
K4 = Kreis (5 , 5 , 4)

print(K1)
print(K2 in K1)
print(K2 in K3)
print(K2.schneidet(K3))
print(K4.schneidet(K3))
print(K1.schneidet(K4))

def sortieren(K: list[Kreis]):
    # def get_r(k: Kreis):
    #     return k.r
    # K2 = sorted(K, key=get_r)
    K2 = sorted(K)
    return K2

K = [K1, K2, K3, K4]
print(sortieren(K))

def enthaelt(K: list[Kreis]):
    E = []
    for i in range(len(K)):
        E.append([])
        for j in range(len(K)):
            E[-1].append(K[i] in K[j])
    return E

E = enthaelt(K)
for line in E:
    print(line)
