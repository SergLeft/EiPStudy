n = input("Ihre Eingabe für die Collatzfolge: ")
n = int(n)  # Datentyp beachten!! input() liefert einen String zurück
n_copy = n  # Kopie zur späteren Ausgabe

k = 1  # Counter: Wir fangen bei 1 an, weil n selbst Teil der Folge ist
while n != 1:
    if n % 2 == 0:  # Gerade
        n = n // 2
    else:           # Ungerade
        n = 3 * n + 1
    k += 1

print("Ihre Zahl ", n_copy, " ergab eine Folgenlänge von ", k)
