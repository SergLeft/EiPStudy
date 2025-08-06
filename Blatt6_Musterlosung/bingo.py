def read_bingo(f):
    field = []
    for j in range(0, 5):  # Unser Bingo hat 5 Zeilen
        line = f.readline()
        zahlen = line.split()
        # Mache die Strings zu Integer. Bei dem Joker 'x' fügen wir die -1 ein.
        # Wir fügen in die Liste -1 ein wenn zahl == "x" sonst int(zahl)
        zahlen = [-1 if zahl == "x" else int(zahl) for zahl in zahlen]
        field.append(zahlen)
    return field

def read(file):
    f = open(file, 'r')
    fields = []
    for i in range(0, 4):  # Wir haben 4 Spieler:innen
        field = read_bingo(f)
        fields.append(field)
        f.readline()

    # Lese die gezogenen Zahlen ein
    gerda = f.readline()
    gerda = gerda.split()
    gerda = [int(i) for i in gerda]
    # list(map(int, gerda))  # Alternative

    f.close()
    return (fields, gerda)

def mark_cell(field, num):
    # Wir gehen jede Zahl durch und schauen ob die gezogene Zahl vorhanden ist. Wenn ja setzen wir diese Zahl auf -1
    # und wissen daher dass sie bereits gezogen wurde. Beachte am Anfang haben wir den Joker auch auf -1 gesetzt.
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == num:
                field[i][j] = -1

def check_bingo_zeile(field):
    # Wir gehen jede Zeile durch und überprüfen ob irgendwo noch keine -1 steht. Falls überall -1 steht bleibt die
    # Variable gewonnen auf True, sonst wird sie auf False gestzt.
    for i in range(len(field)):
        gewonnen = True
        for j in range(len(field[i])):
            if field[i][j] != -1:
                gewonnen = False
        if gewonnen:
            return True
    return False

def check_bingo_spalte(field):
    # Wir gehen jede Spalte durch und überprüfen ob irgendwo noch keine -1 steht. Falls überall -1 steht bleibt die
    # Variable gewonnen auf True, sonst wird sie auf False gestzt.
    for i in range(len(field)):
        gewonnen = True
        for j in range(len(field[i])):
            if field[j][i] != -1:  # <----- Vertauschte Indizes
                gewonnen = False
        if gewonnen:
            return True
    return False

def check_bingo_diagonale(field):
    gewonnen = True
    for i in range(len(field)):
        if field[i][i] != -1:
            gewonnen = False
    if gewonnen:
        return True
    return False

def check_bingo(field):
    if check_bingo_zeile(field):
        return True
    if check_bingo_spalte(field):
        return True
    if check_bingo_diagonale(field):
        return True
    return False


fields, gerda = read("Bingo.txt")

gewonnen = False
for g in gerda:
    for i in range(len(fields)):
        field = fields[i]
        mark_cell(field, g)
        if check_bingo(field):
            print(f'Bingo! Player {i} won!')
            gewonnen = True
            break
    if gewonnen:
        break
