Altklausur Einführung in die Programmierung 23/24

Aufgabe 1)
A sei eine Matrix der Größe n x n.
Der Wert von aij in a mit 0 <= i, j < n sei 1, wenn i*j durch 3 teilbar ist. Schreibe eine Funktion , die eine zweidimensionale Liste A mit den Werten aij aus der Matrix A zurückgibt.

Aufgabe 2)
a)
Gegeben sei eine ganze Zahl n. Schreibe eine Funktion quersumme(n) n), die die Quersumme der
übergebenen Zahl n iterativ berechnet.
b) Schreibe eine Funktion quersumme(n), die die Quersumme von n rekursiv berechnet

Aufgabe 3)
Es gebe eine Menge von Zahlen L = {10, 5, 8, 3, 2 }. Dann sei (a, c) ein Tripel, wenn gilt:
a < b und a + b = c. Zum Beispiel sind (2,8,10) und (2,3,5) Tripel. Schreibe eine Funktion, die eine Liste mit Zahlen bekommt (paarweise verschieden) und die Anzahl der Tripel z urückgibt.

Aufgabe 4)
Ein Wort u ist streichbar zum Wort v es gilt len(u) > len (v), wenn man durch das Streichen bestimmter Buchstaben in u das Wort v bilden kann, z. B. Fritteuse --> Riese.
Schreibe ein Funktion istStreichbarWort(u, v) v), die True zurückgibt, falls v aus u durch Streichen gebildet werden kann.

Aufgabe 5)
G sei eine Adjazenzliste eines ungerichteten Graphen G = (V,E).
a) Schreibe die Funktion istUngerichtet(G), die prüft, ob der Graph ungerichtet ist.
b) Ein Graph sei zusammenhängend für die Knoten u, v, wenn es einen Weg von u nach v gibt. Ein zusammenhängender Teilgraph eines Graphen heiße Zusammenhangskomponente.

Betrachte folgendes Programm:
def breitensuche(besucht, u):
	Q = [u]
	besucht[u] = True
	while len(Q) != 0:
		u = Q.pop(0)
		for i in G[u]:
			if besucht[i] == False:
				Q.append(i)
				besucht[i] = True

G = (Adjazenzliste eines Graphen)
besucht = [False for i in range(len(G))]
for i in range(len(G)):
	if besucht[i] == False:
		breitensuche(besucht, i)

Ergänze das Programm so, dass es die Anzahl der Zusammenhangskomponenten berechnet.
c) Ergänze das in b) gegebene Programm so, dass es die maximale Anzahl an Knoten einer Zusammenhangskomponente berechnet.

Aufgabe 6)
a) Sei T eine Menge an M enschen in e iner n * n Matrix. Ist E intrag T [i][j] == T [j][i] == True, dann kennen sich Person i und j. Schreibe eine Funktion istClique(T,C) welche prüft, ob C eine Cliqe ist. eine Clique ist definiert, als Menge an Menschen, in der jeder jeden kennt.
b)Teste ob eine beliebige Person p aus T neues Mitglied einer Clique C werden kann. Gibt es eine solche Person nicht, gib None zurück

Aufgabe 7)
X sei eine Liste mit natürlichen Zahlen der Länge 2n+1 für die gelte: alle xi != xj, 0 <= i < j < n, d. h. alle Elemente sind zweipaarverschieden.
a) Schreibe eine Funktion zweipaarVerschieden(X), die überprüft , ob alle Elemente der Liste zweipaarverschieden sind.
b) Der Median sei das Element der Liste X, für das n Elemente größer sind und n Elemente kleiner sind. Schreibe die Funktion median(X) X), die den Median Falls die Elemente der Liste nicht zweipaarverschieden sind, soll die Funktion None zurückgeben.
c) Wie viele Elementvergleiche in der Liste X in Abhängigkeit von der Länge n dieser Liste sind für die Funktionen zweipaarVerschieden und median nötig?

Aufgabe 8)
class Baumknoten:
def __init__(self,
self.wert = wer t
self.links = None
self.rechts = None

Ein binärer Suchbaum sei mit der Klasse Baumknoten implementiert, sodass jeder Knoten ein Element dieser Klasse ist.
Schreibe eine Funktion groesse(knoten), die die Werte aller Knoten im Teilbaum, dessen Wurzelknoten ist, addiert, inkl. dem Wert von  knoten.

Aufgabe 9)
Betrachten wir eine Quadratpflanze wie oben abgebildet. Dabei ist die Seitenlänge des größten Quadrats m und des nächstkleinere n Quadrats m/3. Jedes Jahr wächst die Pflanze um 1 Stufe (im Jahr 0 besteht die Pflanze aus einem Quadrat der Seitenlänge n).
a) Schreibe eine Funktionumfang(n, m) m), die rekur siv den Umfang im Jahr n in Abhängigkeit von m berechnet.
b) Schreibe eine Funktion flaecheninhalt(n, m), die rekursiv den Flächeninhalt im Jahr n in Abhängigkeit von m berechnet.

Aufgabe 10)
Es gebe eine Datei Atommassen.txt, in der die Atommassen in u stehen:
H 1,008
He 4,0026
Li 6,94
Be 9,0122
B 10,81
C 12,011
N 14,007
O 15,999
F 18,998

Außerdem gebe es eine Datei Molekuele.txt in der Moleküle und deren Atome aufgelistet sind:
Wasser H 2 O 1
Glucose C 6 H 12 O 6
Kohlenstoffdioxid C 1 O 2
Salzsäure H 1 Cl 1
Ameisensäure C 2 O 2 H 4

Moleküle sollen in der Klasse Molekuel darstellbar sein.

a) Schreibe ein Programm, mit dem man die Datei Atommassen.txt einliest und in einer Datenstruktur speichert. Begründe, warum die benutzte Datenstruktur vorteilhaft für diese Anwendung ist.

b) Schreibe ein Klasse Molekuel, sodass man den Konstruktor mit mol = Molekuel('Wasser H 2 O 1') aufrufen kann. Außerdem soll es möglich sein, die Molekülmassen verschiedener Moleküle zu vergleichen Schreibe auch eine Mem berfunktion der Klasse Molekuel, mit der man die
Molekülmasse eines Moleküls ausre chnen kann.
c) Schreibe ein Programm, welches die Datei Molekuele.txt einliest und in Instanzen der Klasse Molekuel speichert. Diese sollen alle in einer Liste molFeld gespeichert werden d) Sortiere die Liste molFeld nach der Molekülmasse. Implementiere die dafür nötigen Funktionen und begründe, welche Funktion dafür ausreic ht, sort() zu benutzen.
e) Schreibe ein Programm, welches die Moleküle der Größe nach in die Ausgabedatei sortierteMolekuele.txt schreibt.