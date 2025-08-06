# Fakultaet iterativ
n = 3
f = 1
while n > 0:
    f = f * n
    n = n - 1
print(f)

# Fakultaet rekursiv

def f(n):
    if n == 0:
        return(1)
    return(n*f(n-1))

print(f(3))

# Fibonacci rekursiv

def f(n):
    if n == 0: 
        return(0)
    if n == 1:
        return(1)
    return(f(n-1)+f(n-2))

print(f(5))

# Fibonacci rekursiv mit Memoisation
G = [0,1]

def f(n):
    if n < len(G):
        return(G[n]) 
    G.append(f(n-1)+f(n-2))
    return(G[n])

print(f(5))
