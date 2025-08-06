# Die Tuerme von Hanoi

def hanoi(n,start,ziel,hilf):
    if n == 0:
        return
    hanoi(n-1,start,hilf,ziel)
    print(start,' -> ',ziel)
    hanoi(n-1,hilf,ziel,start)

hanoi(2,1,2,3)
