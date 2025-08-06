import math
# a)
# Die naive Lösung, den Gesamtzins von 100% einfach durch fünf zu teilen, lässt den Zinseszins außer Acht, d.h. man
# muss berücksichtigen, dass die verdienten Zinsen im zweiten Jahr auch verzinst werden.
# Daher benutzen wir die formel für den Zinseszins: K = K_0 * (1 + p)^n
# Gegeben ist das Startkapital K_0 = 1000€, das Endkapital K = 2000€, die Laufzeit von n=5 Jahren und gesucht ist p
# Durch Einsetzen in die Formel ergibt sich: 2000 = 1000 * (1 + p)^5
#                                        <=> 2^(1/5) - 1 = p

p = 2**(1/5) - 1
print("a) Der Zinsatz p beträgt %.2f%%." % (p * 100))

# b)
# Gegeben Startkapital K_0 = 2000€, Laufzeit 10 Jahre und Zinssatz p aus Aufgabenteil a). Gesucht Endkapital K.

K = 2000 * (p + 1)**10
print("b) Das Endkapital beträgt nach zehn weiteren Jahren %.2f€." % K)

# c)
# Gegeben Startkapital K_0 = 10.000€, Endkapital K = 1.000.000€ und den Zinsatz p aus Aufgabenteil a).
# Gesucht Laufzeit n. 1.000.000 = 10.000 * (1 + p)^n
#                 <=>       100 = (1 + p)^n
#                 <=>  log(100) = log(1 + p) * n
#    <=>  log(100) / log(1 + p) = n

n = math.log(100) / math.log(1 + p)
print("c) Sie sind in %.2f Jahren Millionär:in!" % n)
