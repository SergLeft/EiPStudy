datei = open('data/huepfburg0.txt','r')
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
datei.close()

# Wir geben zur Kontrolle die Adjazenliste von G aus
for i in range(len(G)):
    print(i," : ",G[i])

# Es folgt die Breitensuche.

# Wir initialisieren zwei Hilfsfelder.
# Ein boolesches Feld 'besucht' zur Markierung der bereits besuchten Knoten von G 
besucht = [ False for i in range(n+1)] 
# Ein Vorgaengerfeld 'pred' zum Speichern des Knotens, von wo aus wir einen neuen Knoten entdeckt haben.
pred = [ 0 for i in range(n+1)]

# Wir suchen vom Startknoten '1' die kuerzesten Wege zu allen anderen Knoten in G.
# Unter einem kuerzesten Weg verstehen wir einen Weg, der die kleinst mögliche Zahl von Kanten benutzt.
Q = [1]
besucht[1] = True

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
u = 2
print(u,end='')
while u != 1:
    v = pred[u]
    print(' -> ',v,end='')
    u = v

