import string

s1 = "franz jagt im komplett verwahrlosten taxi quer durch bayern"

s = list(string.ascii_lowercase)

# Idee: Erstelle eine Liste mit allen Buchstaben des Alphabets. Entferene jeden Buchstaben aus s1 aus der Liste und
# überprüfe ob danach die Liste leer ist, d.h. alle Buchstaben entfernt wurden.

for letter in s1:
    if letter in s:
        s.remove(letter)
        # Alternative:
        # idx = s.index(letter)
        # s.pop(idx)

if len(s) == 0:
    print("Alle Buchstaben kamen vor")
else:
    print("Nicht alle Buchstaben kamen vor")

# b)

s1 = "Hering".lower()
s2 = "Gehirn".lower()

s = list(s1)
for letter in s2:
    if letter in s:
        s.remove(letter)
    else:
        print("Kein Anagramm")
        break

if len(s) == 0:
    print("Anagramm")
else:
    print("Kein Anagramm")

# Alternative

if sorted(list(s1)) == sorted(list(s2)):
    print("Anagramm")
else:
    print("Kein Anagramm")