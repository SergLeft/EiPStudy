def binary_search(lst, x):
    l = 0
    r = len(lst) - 1
    while l < r:
        m = (l + r) // 2  # Berechne Mitte
        if lst[m] == x:
            return m  # Element gefunden
        if x < lst[m]:
            r = m - 1  # Verschiebe rechte Grenze
        else:
            l = m + 1  # Verschiebe linke Grenze
    return -1
    #                          m
    # [1, 1, 2, 2, 3, 5, 6, 7, 8, 10]
    #  l                          r


def binary_search_rec(lst, x, l, r):
    m = (l + r) // 2  # Berechne Mitte
    if x == lst[m]:
        return m  # Element gefunden
    if l >= r:
        return -1  # Liste komplett durchsucht, Element nicht gefunden
    if x < lst[m]:
        # Verschiebe rechte Grenze
        return binary_search_rec(lst, x, l, m-1)
    # Verschiebe linke Grenze
    return binary_search_rec(lst, x, m+1, r)

l = sorted([1,5,2,1,8,7,2,3,6,10])

print(binary_search(l, 9))

res = binary_search_rec(l, 5, 0, len(l)-1)
print(res)
res = binary_search_rec(l, 4, 0, len(l)-1)
print(res)