n = int(input('n = '))
x = 2
while x*x <= n:
    if n % x == 0:
        print('ist nicht prim.')
        break
    x = x + 1
else:
    print('ist prim.')