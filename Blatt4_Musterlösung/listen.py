import random
N = 100
K = 1000
l = [random.randint(0, K) for i in range(N)]

# a) Maximum
m = l[0]
for i in l:
    if i > m:
        m = i
print(m)

# b) Minimum
m = l[0]
for i in l:
    if i < m:
        m = i
print(m)

# c) Summe
s = 0
for i in l:
    s += i
print(s)

# d) Umdrehen
for i in range(len(l)//2):
    l[i], l[-1-i] = l[-1-i], l[i]

# e) Merge
# Idee:
# Die ersten Elemente beider Listen sind jeweils das kleinste Element. Für unsere neue Liste ist also das kleinste
# Element, das kleinste der beiden Elemente.
l1 = sorted([random.randint(0, K) for i in range(N)])
l2 = sorted([random.randint(0, K) for i in range(N)])
i,j = 0,0
l3 = [0 for _ in range(len(l1)+len(l2))]

for k in range(len(l1)+len(l2)):
    if j == len(l2) or (i < len(l1) and l1[i] < l2[j]):
        l3[k] = l1[i]
        i += 1
    else:
        l3[k] = l2[j]
        j += 1
print(f'Ergebnis ist sortiert: {l3 == list(sorted(l1 + l2))}')

# f) Countingsort
c = [0 for _ in range(K + 1)]
l = [random.randint(0, K) for i in range(N)]
# Zähle die Elemente
for num in l:
    c[num] += 1

# Berechne die Prefix-Summe, d.h. den Index des ersten Elementes das größer ist
for i in range(1, len(c)):
    c[i] += c[i-1]

l4 = [-1 for _ in l]

for v in l:
    # Setze v auf den hintersten freien Platz
    l4[c[v]-1] = v
    # Verschiebe den zeiger auf den letzten freien Platz von v
    c[v] -= 1

print(f'Ergebnis ist sortiert: {list(sorted(l)) == l4}')

# ----- Beispiel -----
# l = [3,2,3,3,1,1,2]
# Zähle die Elemente und berechne die Prefix-Summe
# 1: 2 Elemente ->     2
# 2: 2 Elemente -> 2+2=4
# 3: 3 Elemente -> 4+3=7
# [2,4,7]
# Wir stellen uns die sortierte Liste vor und schauen worauf der jeweilige Index der Prefix-Summe zeigt:
# Sortierete Liste: 1,1,2,2,3,3,3
#                       ^   ^    ^
#  Wir sehen dass der jeweilige Index der Prefix-Summe auf den ersten Platz nach der Zahl zeigt. D.h. der Index von 1
#  zeigt auf die erste zwei, der Index von 2 zeigt auf die erste 3, usw...
# Beim Erstellen der neuen Liste, setzen wir die 1 also auf Position des Indexes - 1, d.h. auf den ersten Platz. Danach
# verringern wir den Index damit die nächste 1 auch auf ein freies Feld gesetzt wird.

# Wir fangen also mit einer leeren Liste l4 an und fügen nacheinander die Elemente aus unserer unsortierten Liste l ein.
# Leere Elemente sind hier mit x gekennzeichnet (im Code ist es -1)
# [x,x,x,x,x,x,x]
#      ^   ^    ^  | Füge die 3 ein an der Index-Position - 1 (7-1=6) und verringere den Index von 7 auf 6
# [x,x,x,x,x,x,3]
#      ^   ^   ^   | Füge die 2 ein an der Index-Position - 1 (4-1=3) und verringere den Index von 4 auf 3
# [x,x,x,2,x,x,3]
#      ^ ^     ^   | Füge die 3 ein an der Index-Position - 1 (6-1=5) und verringere den Index von 6 auf 5
# [x,x,x,2,x,3,3]
#      ^ ^   ^     | Füge die 3 ein an der Index-Position - 1 (5-1=4) und verringere den Index von 5 auf 4
# [x,x,x,2,3,3,3]
#      ^ ^ ^       | Füge die 1 ein an der Index-Position - 1 (2-1=1) und verringere den Index von 2 auf 1
# [x,1,x,2,3,3,3]
#    ^   ^ ^       | Füge die 1 ein an der Index-Position - 1 (1-1=0) und verringere den Index von 1 auf 0
# [1,1,x,2,3,3,3]
#  ^     ^ ^       | Füge die 2 ein an der Index-Position - 1 (3-1=2) und verringere den Index von 3 auf 2
# [1,1,2,2,3,3,3]
#  ^   ^   ^       | Fertig, wir haben alle Elemente eingefügt

# Was ist die Laufzeit und was die Nachteile?? (Lösung in Spiegelschrift)

# tros xam dnu tros elbbub sla resseb )ßorg repus thcin k nnew( tfo timos dnu K + N2 = N + K + N tsi tiezfuaL eiD
# tgitöneb rehciepS rehcilztäsuz >- ecalp-ni thciN
# gignähba K lhaZ netßörg red nov hcua rehciepS rehcilztäsuZ
# )taolf( nelhazammoK rüf thcin treinoitknuF
