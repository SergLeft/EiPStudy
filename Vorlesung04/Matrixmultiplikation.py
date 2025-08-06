A = [[1,2],[3,4],[5,6]]
B = [[-1,1],[1,1]]

n = len(A)
m = len(B[0])
d = len(A[0])

print(n,d,m)

C = [ [0 for j in range(m)] for i in range(n) ]

for i in range(n):
    for j in range(m):
        C[i][j] = 0.0
        for k in range(d):
            C[i][j] += A[i][k] * B[k][j]

print(C)
