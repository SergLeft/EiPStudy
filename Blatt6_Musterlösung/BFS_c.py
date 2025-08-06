datei = open('huepfburg0.txt','r')
# Wir lesen zunaechst nur die erste Zeile der Datei
zeile = datei.readline()
# Dort finden wir die Zahl der Knoten |V| und die Zahl |E| der Kanten des Graphen G
nve = zeile.split()

print(int(nve[0]),int(nve[1]))

# n = |V|
n = int(nve[0])

# Initialisierung einer leeren Adjazenzliste
G = [[] for i in range(n+1)]

# In jeder neuen Zeile der Datei finden wir eine gerichtete Kante (u->v) des Graphen G
# Wir fuegen Kante fuer Kante zu der Adjazenzliste von G
for zeile in datei:
    kante = zeile.split()
    u = int(kante[0])
    v = int(kante[1])
    G[u].append(v)
    G[v].append(u)  # New <----------------
datei.close()

# Wir geben zur Kontrolle die Adjazenliste von G aus
for i in range(len(G)):
    print(i," : ",G[i])

# Es folgt die Breitensuche.

# Für alle n Knoten enthält die Matrix später n Einträge mit der Distanz zueinander.
# Für den 0ten Knoten fügen wir als Dummy eine leere Liste hinzu
dist_matrix = [[]]
# Wir nehmen pro Durchlauf einen neuen Knoten als Start
for start in range(1, n+1):
    besucht = [ False for i in range(n+1)]
    pred = [ 0 for i in range(n+1)]

    Q = [start]
    besucht[start] = True

    # Das Feld Q fungiert als Warteschlange
    while len(Q) > 0:
        # Wir bearbeiten stets den Knoten u am Kopf der Warteschlange.
        u = Q.pop(0)
        # Dazu schauen wir uns alle von u ausgehenden Kante in der Adjazenzliste G[u] an.
        for v in G[u]:
            # Wir untersuchen, ob die Kante u-> zu einem noch nicht besuchten Knoten v fuehrt.
            if not besucht[v]:
                # Wir fuegen den neu entdeckten Knoten zur Warteschlange Q hinzu
                Q.append(v)
                # und markieren v als besucht, um v zu einem spaeteren Zeitpunkt nicht erneut in Q aufzunehmen.
                besucht[v] = True
                # Wir merken uns im Vorgaengerfeld, dass wir v von u aus entdeckt haben.
                pred[v] = u

    # Durch Rueckwaertsverfolgung der Vorgaengerverweise folgen wir einem kuerzesten Weg
    # vom Zielknoten 2 zum Startknoten 1.
    dist = [0]
    for u in range(1, len(pred)):
        # Falls Start- und Zielknoten die gleichen sind...
        if u == start:
            dist.append(0)
            continue

        # Zähle die Anzahl der Knoten die wir rückwärts vom Zielknoten u bis zum Startknoten laufen müssen
        counter = 0
        while u != start:
            u = pred[u]
            counter += 1
        dist.append(counter)
    dist_matrix.append(dist)

print("Kürzeste Wege:")
# Gebe Matrix-Indizes aus
for u in range(1, len(dist_matrix)):
    print(f"\t{u}", end="")
print()
# Gebe Matrix aus
for u in range(1, len(dist_matrix)):
    print(u, end="\t")
    for v in range(1, len(dist_matrix)):
        print(dist_matrix[u][v], end="\t")
    print()

m = -1
for u in range(1, len(dist_matrix)):
    for v in range(1, len(dist_matrix[u])):
        if dist_matrix[u][v] > m:
            m = dist_matrix[u][v]

print(f"Der Durchmesser ist {m}")
