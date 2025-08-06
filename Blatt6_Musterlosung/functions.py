def my_abs(x):
    if x < 0:
        return -x
    return x


def manhattan_norm(x):
    return my_abs(x[0]) + my_abs(x[1])


def my_zip(l1, l2):
    l = []
    for i in range(len(l1)):
        l.append((l1[i], l2[i]))
    return l


l1 = [i for i in range(20, 30)]
l2 = [i for i in range(0, 10)]


zipped = my_zip(l1, l2)
print(zipped)

# d)
b = map(manhattan_norm, zipped)
# Mache das Map-Object zu einer Liste
b = list(b)

# e)

def my_map(f, l):
    l2 = []
    for i in l:
        l2.append(f(i))
    return l2


erg = my_map(manhattan_norm, my_zip(l1, l2))
print(erg)
