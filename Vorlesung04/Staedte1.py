# Das eindimensionale Feld der Städtenamen.
stadt = ['MZ', 'KO', 'TR', 'SP', 'WO', 'KL', 'LU']

# Das zweidimensionale Feld der Abstandstabelle.
dist = [[0, 61, 119, 77, 41, 71, 61],
        [61, 0, 95, 129, 97, 101, 116],
        [119, 95, 0, 137, 124, 87, 133],
        [77,129, 137, 0, 35, 50, 17],
        [41, 97, 124, 35, 0, 48, 19],
        [71, 101, 87, 50, 48, 0, 49],
        [61, 116, 133, 17, 19, 49, 0]]

A = input('Von ? ')
B = input('Nach ? ')

# Die beiden Indizes der Start- und der Zielstadt. 
Aidx = stadt.index(A)
Bidx = stadt.index(B)

print('Entfernung = ',dist[Aidx][Bidx])

