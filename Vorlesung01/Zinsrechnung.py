K = float(input('Startkapital = '))
if K > 1000:
    p = 0.01
else:
    p = 0.02
Z = K * p
K = K + Z
print('Kapital nach einem Jahr = ',K)