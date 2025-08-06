# Sortieren durch Mischen ist ein effizientes vergleichsbasiertes Sortierverfahren,
# das dem Divide & Conquer-Prinzip folgt - einem wichtigen Paradigma beim Algorithmenentwurf.
# Idee für die rekursive Vorgehensweise:
# 1. Wir teilen die unsortierte Folge in eine linke und eine rechte Hälfte.
# 2. Wir sortieren die beiden Hälften getrennt voneinander in rekursiver Weise.
# 3. Wir mischen die beiden sortierten Folgen zu einer sortierten Ergebnisfolge.
# Sei T(n) die Zahl der Vergleichsoperationen von Mergesort zum Sortieren von n Elemente,
# dann erhält man folgende Rekursionsgleichung für T(n) = 2*T(n/2)+n und T(1) = 0
# Die Lösung dieser Gleichung lautet: T(n) = n*log_2(n).
# Diese Laufzeit ist somit deutlich besser als die quadratische Laufzeit von naiven
# Sortierverfahren wie z.B. Bubblesort.

import random

# Der Selbsttest zur Überprüfung, ob eine Liste L sortiert ist.
def istSortiert(L):
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            return(False)
    return(True)

# Die Funktion zum Mischen zweier sortierer Folgen A und B zu einer Ergebnisfolge C.
def merge(A,B):
    # Initialisierung der Ergebnisliste C
    C = []
    # Die Indizes i und j zeigen auf die Positionen der noch zu bearbeitenden Elemente von A und B
    i = j = 0
    # Solange wir noch Elemente aus A und B vor uns haben ...
    while i < len(A) and j < len(B):
        # ... übertragen wir das jeweils kleinere in die Ergebnisfolge C und
        # bewegen den Index i bzw. j um eine Position weiter.
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
     # Wir übertragen den eventuell verbliebenen Rest von A nach C.
    while i < len(A):
        C.append(A[i])
        i += 1
     # Wir übertragen den Rest von B nach C.
    while j < len(B):
        C.append(B[j])
        j += 1
    return(C)

# Rekursive Implementierung von Mergesort.
def sort(L):
    n = len(L)
    # Rekursionsanker falls die zu sortierende Folge L nur aus einem Element besteht.
    if n == 1:
        return(L)
    # Wir bestimmen die Mitte zum Aufteilen der Folge L.
    mitte = n // 2
    # Wir sortieren die linke Hälfte. Dazu übergeben wir eine Kopie der Elemente von L
    # von Position 0 bis zur Position mitte-1.
    A = sort(L[0:mitte])
    # Mit der rechten Hälfte verfahren wir analog.
    B = sort(L[mitte:n])
    # Abschließend mischen wir die beiden nun sortierten Teilfolgen und geben das Ergebnis zurück.
    C = merge(A,B)
    return(C)

F = [random.randint(1000,9999) for i in range(100000)]
print(istSortiert(sort(F)))
