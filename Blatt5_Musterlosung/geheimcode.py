import random

code = [[40, 'h'], [14, 'w'], [29, '.'], [24, 's'], [26, 'w'], [8, 'h'], [14, 'u'], [27, 'X'], [9, 'd'], [15, 'a'],
        [31, 'y'], [1, 'b'], [-10, 'e'], [16, '?'], [-3, 'u'], [-11, '4'], [-7, 'w'], [-16, 'Q'], [15, 'w'], [-11, '='],
        [-6, 't'], [2, 'o'], [16, 'W'], [16, 'm'], [8, 't'], [3, 't'], [-16, '.'], [15, ':'], [-25, 'p'], [-10, 'v'],
        [-8, '9'], [-10, 'c'], [-27, 'c'], [4, 'w'], [1, 'c'], ['#', 'Q'], [-18, '/'], [-11, 'w'], [-31, 'g'],
        [-23, '/'], [-15, 't'], [-35, 'o'], [-6, '/']]

# a)
l3 = []
i = 0
while code[i][0] != '#':
    l3.append(code[i][1])
    i += code[i][0]

# Manuelles hinzufügen des letzten Buchstaben, da wir die Schleife beenden ohne den letzten Buchstaben hinzugefügt zu
# haben
l3.append(code[i][1])

for letter in l3:
    print(letter, end='')
print()
# Alternative: print(''.join(l3))

# b)
l = list('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

# Liste die anzeigt an welcher Stelle der i-te Buchstabe im Geheimcode steht
idx = list(range(1,len(l)))
random.shuffle(idx)  # Vertausche die Elemnte in eine zufällige Ordnung
# Füge manuell die 0 hinzu, da sie auf jeden Fall an der 0-ten Stelle stehen muss, da beim Geheimcode der erste
# Buchstabe an der 0-ten Stelle steht
idx.insert(0, 0)

# Erstelle leere Liste
l2 = [0 for i in range(len(l))]

for i in range(0, len(l)-1):
    # jump_n ist die Position des nächsten Buchstabens (idx[i+1]) minus die Position des aktuellen Buchstabens (idx[i])
    l2[idx[i]] = [idx[i+1] - idx[i], l[i]]
# Manuelles hinzufügen des letzten Buchstabens da jump_n = #
l2[idx[-1]] = ['#', l[-1]]

print(l2)
