import random,time

# Wir messen die Laufzeit von Bubblesort für verschiedene Problemgrößen
n = 1000
while n <= 16000:
    a = []
    for i in range(0,n):
        x = random.randint(0,1000000)
        a.append(x)

    # print(a)

    # Wir starten die Stoppuhr zur Laufzeitmessung
    t1 = time.time()

    # Bubblesort arbeitet in n-1 Phasen. Die i-te Phase besteht aus n-i aufeinanderfolgenden
    # Elementvergleichen der Form a[j] <-> a[j+1], die eine Vertauschung durchführen, wenn
    # a[j] > a[j+1] ist.
    # Die Korrektheit der Sortierung ergibt sich induktiv aus folgender Invariante:
    # Nach der i-ten Phase sind die i größten Feldelemente ans Ende des Feldes gewandert
    # und befinden sich an ihrer korrekten Position.

    for i in range(1,n): # i steht für den Phasenzähler
        # Wir führen eine Kaskade von Vergleichen benachbarter Elemente durch.
        # Man beachte, dass in der i-ten Phase nur n-i Vergleiche nötig sind.
        for j in range(0,n-i): # j steht für den Vergleichszähler
            if a[j] > a[j+1]:
                # Tausch der Werte zwischen den Variablen a[j] und a[j+1]
                hilf = a[j]
                a[j] = a[j+1]
                a[j+1] = hilf

    # Die theoretische Gesamtlaufzeit können wir ermitteln, indem wir die Zahl
    # der Vergleichsoperationen zählen: n-1 in Phase 1, n-2 in Phase 2, ...,
    # n-i in Phase i, ... 1 in Phase n-1
    # Insgesamt: 1+2+3+...+n-1 = n*(n-1)/2 nach Gauss

    # Wieviel Zeit ist seit Beginn der Laufzeitmessung vergangen?
    t2 = time.time()

    # Ein Selbsttest, um zu bestätigen, dass wir korrekt sortiert haben.
    fehler = False
    for j in range(0,n-1):
        # Vergleich aufeinanderfolgender Element, um gegebenenfalls eine
        # Fehlstellung zu entdecken
        if a[j] > a[j+1]:
            fehler = True
            break

    if fehler:
        print("Sortierung falsch")
    else:
        print("Sortierung korrekt")
    # print(a)

    # Ausgabe der Laufzeit für die jeweilige Problemgröße
    print("T(", n, ") = ", t2 - t1)

    # Verdopplung der Problemgröße sollte zu einer Vervierfachung der Laufzeit führen,
    # denn T(n) = c*n^2 => T(2*n)=4*T(n)
    n *= 2
