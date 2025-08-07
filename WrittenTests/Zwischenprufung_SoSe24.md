Aufgabe 1: (6 + 6 + 6 Punkte)
1. Schreiben Sie eine iterative Funktion f(n), die eine positive reelle Zahl n solange halbiert, bis ihr
Wert kleiner oder gleich 1 wird. Die Funktion soll die Anzahl von Teilungsschritten zurückgeben.
2. Schreiben Sie eine rekursive Funktion r(n), so dass r(n) = f(n) für n in R_+, d.h. die Funktion r
hat die gleiche Rückgabe wie f.
3. Schreiben Sie eine Funktion c(n) mit konstanter Laufzeit, so dass c(n) = f(n) für n in R_+, d.h. c
hat ebenfalls die gleiche Rückgabe wie f.

Aufgabe 2: (6 + 6 Punkte)
Gegeben sei ein Feld a der Länge n mit ganzzahligen Feldeinträgen. Wenn für alle Indizes 0 <= i < n − k
gilt, dass a_i = a_(i+k), dann nennen wir die Folge der Feldeinträge periodisch mit einer Periode der Länge
k in N_0, d.h. die ersten k Zeichen wiederholen sich.
1. Schreiben Sie eine Funktion hatPeriode(a,k), die entscheiden kann, ob die Feldeinträge eine Periode
der Länge k aufweisen.
2. Schreiben Sie eine Funktion kleinstePeriode(a) die den kleinsten Wert k berechnet, sodass das
Feld periodisch ist, d.h. für jedes 0 <= i < n − k : a_i = a_(i+k).
Beispiel:
a = [2,3,1,2,2,3,1,2,2,3,1,2,2,3]
hatPeriode(a,3)-> False hatPeriode(a,8) -> True kleinstePeriode(a) -> 4

Aufgabe 3: (5 + 5 + 5 + 6 + 4 Punkte)
Gegeben sei eine zweidimensionale Matrix M 2 Nn⇥n, deren Einträge natürliche Zahlen sind.
1. Schreiben Sie eine Funktion zeilensumme(M,i), die die Summe der Zahlen der i-ten Zeile berechnet.
2. Schreiben Sie eine Funktion spaltensumme(M,j), die die Summe der Zahlen der j-ten Spalte berechnet.
3. Schreiben Sie eine Funktion istMagisch(M), die überprüft, ob M ein magisches Quadrat ist. Dazu müssen alle Spaltensummen, alle Zeilensummen und die Summen der beiden Diagonalen übereinstimmen.
4. Schreiben Sie ein Programm, das ein magisches Quadrat der Größe n x n mit Hilfe von Backtracking finden kann. Als Feldeinträge sollen die Zahlen von 1 bis n^2 jeweils einmal verwendet werden.
5. Zeigen Sie, dass die Zeilen- und Spaltensummen in Teilaufgabe 4 dann den Wert n(n^2 + 1)/2 annehmen.

Aufgabe 4: (6 + 6 + 4 Punkte)
1. Schreiben Sie eine Funktion erzeuge3DFeld(n), die ein dreidimensionales Feld F der Dimension n x n x n erzeugt und alle Feldelemente F_(i,j,k) für 0 <= i, j, k < n mit dem Wert i+j +k initialisiert. Der Rückgabewert der Funktion soll das erzeugte Feld F sein.
2. Schreiben Sie ein Programm, das mittels der Funktion erzeuge3DFeld ein dreidimensionales Feld
der obigen Form für n = 4 erzeugt und anschließend die Summe s aller Feldelemente berechnet und mit Hilfe des print-Kommandos ausgibt.
3. Beweisen Sie, dass Folgendes gilt: s = (3/2)*(n − 1)*n^3

Aufgabe 5: (8 + 6 Punkte)
Gegeben sei die Adjazenzmatrix A 2 B^(n x n) eines ungerichteten Graphen G = (V,E). Die Knotenmenge V sei die Menge {0, 1, . . . ,n − 1}. Wir repräsentieren A in Form eines zweidimensionalen Feldes A von booleschen Werten. Eine Kante (u, v) zwischen den Knoten u und v existiere genau dann, wenn der Feldeintrag A[u][v] den Wert True hat.
1. Schreiben Sie eine Funktion konvertiere(A,G), die aus einer Adjazenzmatrix A eine Adjazenzliste G für den Graphen erstellt. Dabei repräsentieren wir die Adjazenzliste G als ein Feld G von Feldern mit der Eigenschaft, dass das Feld G[u] alle Knoten v enthält, für die A[u][v] == True gilt, d.h. (u, v) in E.
2. Ein ungerichteter Graph G = (V,E) heißt zweifärbbar, wenn man jedem Knoten v 2 V eine von zwei Farben geben kann, so dass alle Kanten (u, v) in E stets Knoten mit unterschiedlichen Farben miteinander verbinden. Schreiben Sie eine Funktion istZweiFaerbbar(G), die einen ungerichteten, zusammenhängenden Graphen G = (V,E) daraufhin untersucht, ob er zweifärbar ist. Verwenden Sie zur Lösung eine modifizierte Breitensuche.

Aufgabe 6: (8 Punkte)
Gegeben sei eine Folge von kleinen Buchstaben des deutschen Alphabets. Zum Beispiel folgender Satz: "franz jagt im komplett verwahrlosten taxi quer durch bayern".
Schreiben Sie eine Funktion pangramm(satz), die überprüft, ob die gegebene Buchstabenfolge satz ein Pangramm ist. Das heißt, dass jeder Buchstabe des Alphabets (mit Ausnahme der Umlaute) in der Buchstabenfolge vorkommen muss.

Aufgabe 7: (7 Punkte)
Wir betrachten eine Treppe mit n Stufen. Beim Ersteigen der Treppe kann man eine Treppenstufe oder auch zwei Treppenstufen in einem Schritt nehmen. Schreiben Sie eine Funktion zahlDerSchrittfolgen(n), die die Zahl der unterschiedlichen Schrittfolgen berechnet, um eine Treppe mit n Stufen zu ersteigen.
Hinweis: Fibonacci-Folge