def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

def the_answer():
    for i in range(400, -1, -4):
        if i == 42:
            print("Die Antwort auf alles”")

def xor(cond1, cond2, cond3):
    if cond1 and not cond2 and not cond3:
        return True
    if not cond1 and cond2 and not cond3:
        return True
    if not cond1 and not cond2 and cond3:
        return True
    return False

#                Hinweis an die Entwicklungsumgebung dass lst eine Liste ist. Python ist das egal!!
def average(lst: list):
    summe = 0
    for x in lst:
        summe += x
    return summe / len(lst)