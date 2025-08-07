Aufgabe 1: Listen (4 + 3 + 2 = 9 Punkte)
Gegeben seien zwei Listen lst1 und lst2 der Länge n mit natürlichen Zahlen. Wir wollen
überprüfen, ob die Elemente von lst1 und lst2 gleich sind. Dazu schauen wir für jedes Element
aus lst1 nach, ob es in lst2 vorkommt.
a) Erstellen Sie ein Programmablaufdiagramm, das den beschriebenen Algorithmus darstellt.
Am Ende soll das Ergebnis True oder False ausgegeben werden.
b) Schreiben Sie eine Python-Funktion check_lists(lst1, lst2), die den beschriebenen
Algorithmus implementiert. Die Funktion soll True zurückgeben, wenn alle Elemente von
lst1 in lst2 vorkommen, sonst False.
c) Schätzen Sie die Laufzeit des Algorithmus aus b) in Bezug auf die Länge n der Listen ab.
Begründen Sie Ihre Antwort.

Aufgabe 2: Magische Quadrate (2 + 2 + 3 = 7 Punkte)
Gegeben sei eine Matrix M ∈ Nn×n (als zweidimensionale Liste), deren Einträge natürliche
Zahlen sind.
a) Schreiben Sie eine Funktion zeilensumme(M,i), die die Summe der Zahlen der i-ten Zeile
berechnet.
b) Schreiben Sie eine Funktion spaltensumme(M,j), die die Summe der Zahlen der j-ten
Spalte berechnet.
c) Schreiben Sie eine Funktion istMagisch(M), die überprüft, ob M ein magisches Quadrat
ist. Dazu müssen alle Spaltensummen, alle Zeilensummen und die Summen der beiden
Diagonalen übereinstimmen

Aufgabe 3: Rekursion (2 + 3 + 3 = 8 Punkte)
Implementieren Sie folgende Funktionen rekursiv:
a) Eine rekursive Funktion reverse(lst), die eine gegebene Liste lst umdreht.
b) Schreiben Sie eine rekursive Funktion sum_of_digits(int_str), die die Quersumme der
Ziffern eines gegebenen Strings int_str berechnet. Beispiel: Für int_str = ’12345’ wird
1 + 2 + 3 + 4 + 5 = 15 zurückgegeben.
c) Gegeben eine Liste lst, die sowohl Zahlen, als auch Listen enthalten kann. Schreiben Sie
eine rekursive Funktion deep_sum(lst), die die Summe der Zahlen aller enthaltenen Listen
berechnet. Die Summe der leeren Liste ist 0. Beispiel: Für lst = [1,2,[3,4],[5,[6]]]
wird 1 + 2 + 3 + 4 + 5 + 6 = 21 zurückgegeben.
Hinweis: Sie können mit isinstance(obj, list) überprüfen, ob obj eine Liste ist.

Aufgabe 4: Dateien (2 + 2 + 2 = 6 Punkte)
Gegeben Sei eine Datei map.txt, in der eine Karte mit verschiedenen Ortsnamen und deren
Breiten- und Längengrade wie folgt gespeichert ist:
Beispiel:
Mainz , 49.992 , 8.247
Wiesbaden , 50.082 , 8.240
Berlin , 52.523 , 13.413
...
Hinweis: Sie dürfen in jeder Teilaufgabe die vorherigen Teilaufgaben als gegeben voraussetzen.
a) Lesen Sie die Datei map.txt ein und speichern Sie die Ortsnamen, Breiten- und Längen-
grade in einer geeigneten Datenstruktur.
b) Finden Sie die Orte aus der Datei, die in der Nähe von Mainz liegen. Ein Ort ist in der Nähe
von Mainz, wenn die Differenz des Breiten- sowie Längengrades kleiner als 1 ist. Beispiel:
Wiesbaden ist in der Nähe von Mainz, Berlin nicht.
c) Schreiben Sie die Namen der gefilterten Orte in eine neue Datei output.txt. In jeder Zeile
soll genau ein Name vorkommen.

