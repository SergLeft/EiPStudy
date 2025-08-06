n = 12
A = []

for i in range(n):
    A.append([])
    for j in range(n):
        if (i * j) % 3 == 0:
            A[i].append(True)
        else:
            A[i].append(False)
        # Alternativ:
        # A[i].append( (i * j) % 3 == 0 )

# Möglichkeit 2

A = [[False for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        if i * j % 3 == 0:
            A[i][j] = True

# Möglichkeit 3

A = [[i * j % 3 == 0 for j in range(n)] for i in range(n)]

