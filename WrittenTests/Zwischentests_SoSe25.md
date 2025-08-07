Aufgabe 1: Bücher (10 Punkte)
Sie haben eine Liste von Büchern angelegt, die Sie in der Bibliothek ausleihen möchten. Jedes
Buch ist durch ein Tupel mit dem Titel, dem Autor und dem Erscheinungsjahr repräsentiert.
Beispiel:
data = \[( ’Der Prozess ’, ’Franz Kafka ’, 1925) ,
(’Der Steppenwolf ’, ’Hermann Hesse ’, 1927) ,
(’Der Meister und Margarita ’, ’Michail Bulgakow ’, 1967) ,
(’Der alte Mann und das Meer ’, ’Ernest Hemingway ’, 1952) ,
(’Die Verwandlung ’, ’Franz Kafka ’, 1915) ,
...]
Um nicht unnötig in der Bibliothek hin und her zu laufen, möchten Sie die Bücher nach den Autoren
gruppieren.


a) Schreiben Sie eine Klasse Book, die die Attribute title, author und year enthält. Implementieren Sie die Methode **init**(self, title, author, year), die diese Werte speichert.
b) Später wollen Sie die Bücher auch nach dem Erscheinungsjahr sortieren können. Implementieren Sie die Methode **lt**(self, other) in Book, die die Erscheinungsjahre der Bücher vergleicht und True zurückgibt, wenn das aktuelle Buch älter ist als das andere Buch.
c) Konvertieren Sie die Liste data in eine Liste books von Book-Objekten.
d) Implementieren Sie eine Funktion group\_by\_author(books), die die Bücher nach Autoren gruppiert. Sie soll ein Dictionary zurückgeben, in dem die Schlüssel die Autorennamen und die Werte Listen von Büchern sind.


Beispiel:
grouped\_books = {
’Franz Kafka ’:
\[ Book (’Der Prozess ’, ’Franz Kafka ’, 1925) ,
Book (’Die Verwandlung ’, ’Franz Kafka ’, 1915)] ,
’Hermann Hesse ’:
\[ Book (’Der Steppenwolf ’, ’Hermann Hesse ’, 1927)] ,
’Michail Bulgakow ’:
\[ Book (’Der Meister und Margarita ’, ’Michail Bulgakow ’, 1967)] ,
’Ernest Hemingway ’:
\[ Book (’Der alte Mann und das Meer ’, ’Ernest Hemingway ’, 1952)]
}


e) Sortieren Sie die Bücher in jedem Autor-Array nach dem Erscheinungsjahr.



Aufgabe 2: Pythagoreische Tripel (2 + 5 + 3 = 10 Punkte)
Ein pythagoreisches Tripel ist ein Tripel (a, b, c) von (positiven) natürlichen Zahlen, so dass a2 + b2 = c2 gilt.
a) Schreiben Sie eine Funktion is\_pythagorean\_triple(a, b, c), die überprüft, ob a, b, c ein pythagoreisches Tripel bilden. Die Funktion soll True zurückgeben, wenn a, b, c ein pythagoreisches Tripel bilden, und False sonst.

b) Schreiben Sie ein Programm, das alle pythagoreischen Tripel mit a, b, c < 100 ausgibt. Achten Sie darauf, alle Tripel nur einfach auszugeben. Hinweis: Probieren Sie systematisch alle Kombinationen von a, b, c aus. Sie dürfen natürlich die Funktion aus a) verwenden.
c) Einige pythagoreische Tripel lassen sich auch durch die Formeln a = 2mn, b = m2−n2, c = m2 + n2 mit m, n ∈ N erzeugen. Schreiben Sie ein Programm, das pythagoreischen Tripel mit a, b, c < 100 mithilfe der Formeln erzeugt. 

Hinweis: Achten Sie darauf, dass sie nur gültige Tripel erzeugen, d.h. insbesondere a, b, c > 0.



Aufgabe 3:
Gegeben sei eine Liste data, die n ganze Zahlen (Typ int) enthält.
Entwickeln Sie ein Programm, das alle negativen Zahlen, d.h. Zahlen kleiner 0, der Liste data ausgibt.
Entwickeln Sie ein Programm, das alle ungeraden Zahlen ausgibt. Erinnerung: Sie können mit dem  Modulo-Operator % den Rest
einer Division berechnen. Eine Zahl x ist durch p teilbar, wenn x mod p = 0.
Entwickeln Sie ein Programm, das alle positiven Zahlen, d.h. Zahlen größer 0, der Liste data ausgibt.

a) Erstellen Sie ein Programmflussdiagramm, das das Problem löst.
b) Implementieren Sie das Programm in Python.

