datei = open('data/LondonTubeLines.csv','r')
datei.readline()
# Initialisierung einer leeren Adjazenzliste
G = []

# In jeder neuen Zeile der Datei finden wir eine gerichtete Kante (u->v) des Graphen G
# Wir fuegen Kante fuer Kante zu der Adjazenzliste von G
stations = []
for zeile in datei:
    kante = zeile.split(',')
    uName = kante[1]
    if uName not in stations:
        stations.append(uName)
        G.append([])
    vName = kante[2].rstrip('\n')
    if vName not in stations:
        stations.append(vName)
        G.append([])
    u = stations.index(uName)
    v = stations.index(vName)
    if v not in G[u]:
        G[u].append(v)
    if u not in G[v]:
        G[v].append(u)
datei.close()

n = len(stations)
print(n)

# Es folgt die Breitensuche.

# Wir initialisieren zwei Hilfsfelder.
# Ein boolesches Feld 'besucht' zur Markierung der bereits besuchten Knoten von G
besucht = [ False for i in range(n)]
# Ein Vorgaengerfeld 'pred' zum Speichern des Knotens, von wo aus wir einen neuen Knoten entdeckt haben.
pred = [ 0 for i in range(n)]

# Wir suchen vom Startknoten die kuerzesten Wege zu allen anderen Knoten in G.
# Unter einem kuerzesten Weg verstehen wir einen Weg, der die kleinst mögliche Zahl von Kanten benutzt.
start = stations.index('Silver Street')
Q = [start]
print(stations[start])
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
# vom Zielknoten zum Startknoten.
u = stations.index('Wimbledon')
print(stations[u],end='')
while u != start:
    v = pred[u]
    print(' -> ',stations[v])
    u = v

