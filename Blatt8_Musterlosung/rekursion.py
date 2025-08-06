def product(lst):
    if len(lst) == 0:
        return 1
    return lst[0] * product(lst[1:])

print(product([1, 2, 3]))

def down_and_up(n):
    if n == 0:
        print(0, end=" ")
        return
    print(n, end=" ")
    down_and_up(n-1)
    print(n, end=" ")

down_and_up(5)
print()

def merge(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1

    if lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])

l1 = sorted([2,7,32,7,34,1,8,35,78])
l2 = sorted([4,8,3,7,3,73,8,32,6,86,14])

print(merge(l1, l2))