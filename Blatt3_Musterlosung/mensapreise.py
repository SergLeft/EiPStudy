a = float(input())
b = float(input())
c = float(input())

# a)
if a < b and a < c:
    print("a ist das günstigste Essen und kostet %.2f€" % a)
elif b < c:
    print("b ist das günstigste Essen und kostet %.2f€" % b)
else:
    print("c ist das günstigste Essen und kostet %.2f€" % c)

# b)
if b < a < c or c < a < b:
    print("a ist das zweitgünstigste Essen und kostet %.2f€" % a)
elif a < b < c or c < b < a:
    print("b ist das zweitgünstigste Essen und kostet %.2f€" % b)
else:
    print("c ist das zweitgünstigste Essen und kostet %.2f€" % c)

#c)
durchschnittspreis = (a + b + c) / 3
print("Das Mensaessen kostet heute durchschnittlich %.2f€" % durchschnittspreis)
