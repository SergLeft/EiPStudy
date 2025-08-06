# a) Die in der letzten Vorlesung vorgestellten Dictionaries wären die beste Wahl, hier aber mit Listen

def get_mass(l: list, atom: str):
    """Findet ein Atom in der Liste und gibt die Masse zurück"""
    for entry in l:
        name, mass = entry[0], entry[1]
        if name == atom:
            return mass
    return -1

f = open("Atommassen.txt", "r")
atoms = []
for line in f:
    name, mass = line.split()
    # Speichere die Atome in einer Liste aus Tupeln
    atoms.append((name, float(mass)))
f.close()

class Molekuel:
    def __init__(self, description: str):
        description = description.split()
        self.name = description.pop(0)
        self.atoms_list = []
        for i in range(0, len(description), 2):
            self.atoms_list.append((description[i], int(description[i + 1])))

    def berechneMasse(self):
        summe = 0
        for atom in self.atoms_list:
            name, count = atom[0], atom[1]
            mass = get_mass(atoms, name)
            summe += mass * count
        return summe

    def __lt__(self, other):
        if self.berechneMasse() < other.berechneMasse():
            return True
        else:
            return False

    def __str__(self):  # Für die str() Funktion, für print() und für den Debugger (nachrangig zu __repr__)
        s = self.name
        for atom in self.atoms_list:
            s += " " + atom[0] + " " + str(atom[1])
        return s

    def __repr__(self):  # Für den Debugger und das Printen von Listen aus Molekülen
        return f"{self.name}: Masse - %.2f" % self.berechneMasse()

f = open("Molekuele.txt", "r")
molFeld = []
for line in f:
    molFeld.append(Molekuel(line))
    molFeld[-1].berechneMasse()
f.close()

molFeld.sort()

f = open("SortierteMolekuele.txt", "w")
for mol in molFeld:
    f.write(str(mol) + "\n")
f.close()