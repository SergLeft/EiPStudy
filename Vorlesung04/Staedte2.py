import math

# Wir führen drei Listen für die Städtenamen, die Breitengrade und die Längengrade
stadt = []
breitengrad = []
laengengrad = []

# Wir öffnen die Städte-Datei zum Lesen.
datei = open('data/Staedte.txt','r',encoding='utf-8')
# Wir lesen die Datei zeilenweise.
for zeile in datei:
    # Wir splitten die Zeile in ihre drei Bestandteile anhand des Tabulator-Trennzeichens.
    daten = zeile.split('\t')
    # Wir hängen den gelesenen Stadtnamen in die Städte-Liste an.
    stadt.append(daten[0])
    # Wir verfahren in gleicher Weise mit den Breiten- und Längengraden und
    # rechnen diese von Grad-Angaben ins Bogenmaß um.
    breitengrad.append(float(daten[1])*math.pi/180)
    laengengrad.append(float(daten[2])*math.pi/180)

datei.close()

#print(stadt)
#print(breitengrad)
#print(laengengrad)

# Radius der Erdkugel.
R = 6371

# Zahl der Städte in Deutschland.
n = len(stadt)

# Wir initialisieren ein zweidimensionales Feld bestehend aus n Zeilen und n Spalten mit 0 Werten.
dist = [ [ 0 for i in range(n)] for j in range(n)]

# Wir bauen die Distanztabelle auf.
for Aidx in range(n):
    theta = breitengrad[Aidx]
    phi = laengengrad[Aidx]

    # Kartesische Koordinaten des Punktes A
    Ax = math.cos(theta) * math.cos(phi)
    Ay = math.cos(theta) * math.sin(phi)
    Az = math.sin(theta)

    for Bidx in range(Aidx+1,n):
        theta = breitengrad[Bidx]
        phi = laengengrad[Bidx]

        # Kartesische Koordinaten des Punktes B
        Bx = math.cos(theta)*math.cos(phi)
        By = math.cos(theta)*math.sin(phi)
        Bz = math.sin(theta)

        # Skalarprodukt des A-Vektors und B-Vektors
        AB = Ax * Bx + Ay * By + Az * Bz
        # Fehlerbehandlung für den Fall, dass aufgrund numerischer Fehler AB nicht im Definitionsbereich des acos liegt.
        if AB > 1.0:
            AB = 1.0
        if AB < -1.0:
            AB = -1.0
        # Winkel zwischen A-Vektor und B-Vektor
        alpha = math.acos(AB)
        # Eintrag des berechneten Distanzwertes in die symmetrische Distanztabelle.
        dist[Aidx][Bidx] = dist[Bidx][Aidx] = alpha * R

# Beispielhafte Distanzberechnung für MZ und KO.
Aidx = stadt.index('MAINZ')
Bidx = stadt.index('KOBLENZ')

print('Entfernung = ',dist[Aidx][Bidx])


