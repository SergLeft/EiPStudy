# Elementare Datentypen
# Wir betrachten die elementaren Datentypen:
# - float(ing point number) = Fließkommazahlen
# - int(eger) = ganze Zahlen
# - str(ing) = Zeichenketten
# - bool(ean) = Wahrheitswerte
# Der Typ einer Variable kann mit Hilfe der type-Funktion ermittelt werden.#

x = 1.0
print(x,type(x))
x = 1
print(x,type(x))
x = 'EIP'
print(x,type(x))
x = (1 < 2)
print(x,type(x))

# Eine Million in wissenschaftlicher Notation als Fließkommazahl und als ganze Zahl:

x = 1e6
print(x,type(x))
x = 1000000
print(x,type(x))

# Fließkommazahlen (float) werden nur mit endlicher Genauigkeit (1 Bit Vorzeichen, 
# 52 Bit Mantisse und 11 Bit Exponent im Binärsystem) dargestellt. 
# Deshalb sind arithmetische Operationen Rundungsfehler behaftet.

print(3*0.1-0.3)

# Formatierte Ausgabe einer Fließkommazahl
# Die Formatierung wird über eine Zeichenkette der Form '%n.mf' gesteuert.
# - n steht für die Zahl der insgesamt ausgegebenen Zeichen inklusive des Dezimalpunktes.
# - m steht für die Zahl der Nachkommastellen.

x = 1234.5678
print('%.2f' % x)
print('%.20f' % x)

y = 98.7654321
print('x = %10.2f' % x)
print('y = %10.2f' % y)

# Ganze Zahlen (int) können potentiell beliebig viele Stellen besitzen. Die zugehörigen
# arithmetischen Operationen sind exakt.

x = 10000000000000000000000000000000000000000000000000000000000000000000000000000000000001
print(x,type(x))
y = float(x)
print(y,type(y))
print(x - y)

# Zeichenketten (str) bestehen aus einer Folge von Zeichen (Buchstaben, Ziffern, Sonderzeichen)

x = 'Hallo EIP!'
print(x,type(x))

# Wahrheitswerte (bool) können nur die Werte True und False annehmen.

x = (1 < 2)
print(x,type(x))

# Wir betrachten die gebräuchlichen arithmetischen Operationen +,-,*,/,** für floats
# a**b steht für die Potenz a^b.
# Dabei gelten die üblichen Vorrangregeln (Punktrechnung vor Strichrechnung)

x = (1.0+3.0*2.0**3)/10.0
print(x)

# Man kann int-Zahlen und float-Zahlen in arithmetischen Ausdrücken kombinieren. 
# Sobald eine float-Zahl involviert ist, ist das Ergebnis vom Typ float.

x = 1+2.0
print(x,type(x))

# Bei dem Divisionsoperator ist zu beachten, dass das Ergebnis von a / b stets vom 
# Typ float ist, selbst wenn a und b vom Typ int sind.

x = 21 / 7
print(x,type(x))

# Deshalb sollte man bei ganzzahliger Arithmetik den Divisionsoperator // verwenden.
# Bei der ganzzahligen Division mit Rest von zwei natürlichen Zahlen a und b ergibt sich:
# a = q * b + r mit 0 <= r < b.
# Qutient q = a // b und Rest r = a % b

x = 21 // 7
print(x,type(x))

a = 21
b = 5
q = a // b
r = a % b

print(a,' = ',q,'*',b,'+',r)

# Operationen auf Zeichenketten
x = 'Hallo'
y = 'EIP'

print(x+' '+y)
print(3*x)
print(x < y, x>= y, x != y, x == y)


# Boolesche Operationen
print('x    ','|','y    ','|','not x','|', 'x and y','|', 'x or y','|', 'x xor y')

x = False; y = False
print(x,'|',y,'|',not x,' |', x and y,'  |', x or y,' |', x ^ y)

x = False; y = True
print(x,'|',y,' |',not x,' |', x and y,'  |', x or y,'  |', x ^ y)

x = True; y = False
print(x,' |',y,'|',not x,'|', x and y,'  |', x or y,'  |', x ^ y)

x = True; y = True
print(x,' |',y,' |',not x,'|', x and y, '   |',x or y,'  |', x ^ y)