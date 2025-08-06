a = int(input('a = '))
b = int(input('b = '))

# Berechnung des größten gemeinsamen Teilers der beiden natürlichen Zahlen a und b
# unter Verwendung des Euklidischen Algorithmus
# Sei a = q * b + r mit 0 <= r < b, r = Rest bei ganzzahliger Division von a durch b,
# dann gilt ggT(a,b) = ggT(b,r).
# Dadurch können wir die Berechnung des ggT zweier großer Zahlen a und b auf die
# Berechnung des ggT zweier kleinerer Zahlen b und r zurückführen.

# Solange bei der Berechnung des ggT(a,b) b noch nicht den Wert 0 erreicht hat, führen wir
# den Schleifenrumpf durch, indem wir wiederholt die ganzzahlige Division einsetzen
# und einen Rollentausch (a,b) <-> (b,r) vornehmen.
while b > 0:
    # r = Rest bei ganzzahliger Division von a durch b
    r = a % b
    # Das Paar (a,b) wird ersetzt durch das neue Paar (b,r)
    a = b
    b = r
    print('ggT(',a,',',b,') = ')

# Ausgabe des ggT
print(a)
