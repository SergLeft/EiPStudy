# Eingabe des Kapitals
K = float(input('Startkapital = '))

# Festlegung des Zinssatzes
p = 0.01
# Initialisierung des Jahreszählers
jahr = 0

# Der eingerückte Anweisungsblock der while-Schleife wird solange ausgeführt,
# wie die Bedinung (jahr < 30) erfüllt ist.
while jahr < 30:
    # Ermittlung der Zinsen nach Ablauf eines Jahres
    Z = K * p
    # Am Ende des Jahres addieren wir die Zinsen zum Kapital
    K = K + Z
    # Wir inkrementieren den Jahreszähler
    jahr = jahr + 1
    # Ausgabe des neuen Kapitalstandes in jedem Schleifendurchlauf
    print('Kapital nach dem',jahr,'. Jahr  = ', K)