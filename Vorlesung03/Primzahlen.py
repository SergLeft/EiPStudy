# Berechnung aller Primzahlen < 1000
n = 2

while n < 1000:
    x = 2
    # [n = a*b wobei a,b,n natürliche Zahlen > 1] => [a <= sqrt(n) oder b <= sqrt(n)]
    # Deshalb genügt es, nur Teiler <= sqrt(n) zu suchen.
    while x*x <= n:
        # Wir verwenden Division mit Rest, um zu überprüfen, ob x die Zahl n teilt
        if n % x == 0:
            #print(n,'ist keine Primzahl.',x,'ist ein Teiler.')
            # Wenn wir einen Teiler gefunden haben, können wir die Suche nach einem Teiler
            # sofort abbrechen
            break
        # Wir gehen zum nächsten möglichen Teiler über.
        x += 1
    else:
        # Der else-Teil der while-Schleife wird nur ausgeführt, wenn wir die Schleife nicht
        # durch break abgebrochen haben.
        print(n,'ist eine Primzahl.')

    n += 1