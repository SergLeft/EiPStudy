n = 2
while n < 100:
    x = 2
    while x < n:
        if n % x == 0:
            break
        x = x + 1
    else:
        print(n)
    n += 1  