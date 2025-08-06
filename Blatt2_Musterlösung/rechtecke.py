# a) intervals
# Der Schnitt von Interval ( ) mit Interval [ ] hat die folgenden Möglichen Kombinationen:
# 1. ( ) [ ]  # Kein Schnitt
# 2. [ ] ( )  # Kein Schnitt
# 3. ( [ ) ]  # Schnitt
# 4. [ ( ] )  # Schnitt
# 5. ( [ ] )  # Schnitt
# 6. [ ( ) ]  # Schnitt
I1a = -2
I1b = 5

I2a = 3
I2b = 7
# check for intersection I1, I2
# Aus den obrigen Beispielen ist ersichtlich dass zwei Intervalle sich NICHT schneiden wenn beide Grezen eines Intervals
# (sagen wir I1) niedriger als die untere Grenze des anderen ist, oder beide Grezen größer als die obere Grenze des
# anderen ist
#=>         1. Fall         ODER         2. Fall
if (I1a < I2a and I1b < I2a) or (I1a > I2b and I1b > I2b):
    print("Die beiden Intervalle schneiden sich nicht")
else:
    print("Die beiden Intervalle schneiden sich")

# -------------------
# b) rectangles
# Zwei Rechtecke schneiden sich genau dann, wenn sich deren Intervall auf der x-Achse (hier [a,b]) und auf der y-Achse
# schneiden.
R1a = 1
R1b = 3
R1c = 2
R1d = 4

R2a = 2
R2b = 5
R2c = 3
R2d = 6
# check for intersection R1, R2
# Wir benutzen zwei Mal den Schnitttest aus a). Beachte dass der Test prüft oder sich die Intervalle NICHT schneiden.

if (R1a < R2a and R1b < R2a) or (R1a > R2b and R1b > R2b):  # Test x-Achse
    # Wenn sich die Intervall auf der x-Achse sich nicht schneiden sind wir fertig
    print("Die beiden Rechtecke schneiden sich nicht")
else:
    if (R1c < R2c and R1d < R2c) or (R1c > R2d and R1d > R2d):  # Test y-Achse
        print("Die beiden Rechtecke schneiden sich nicht")
    else:
        print("Die beiden Rechtecke schneiden sich")
