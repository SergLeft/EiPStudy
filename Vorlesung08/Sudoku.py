# Lösen von Sudokus mittels Backtracking

# Wir repräsentieren ein Sudoku als zweidimensionales Feld mit 9x9 Einträgen.
# Der Wert 0 steht für noch unbelegte Einträge im Sudoku-Feld.
S1 = [[0, 0, 9, 8, 0, 0, 0, 0, 0],
      [0, 0, 5, 0, 6, 3, 0, 0, 0],
      [0, 2, 0, 0, 9, 0, 8, 3, 0],
      [0, 0, 0, 0, 0, 7, 0, 0, 3],
      [0, 0, 0, 6, 0, 0, 5, 1, 0],
      [0, 1, 0, 4, 0, 0, 2, 0, 0],
      [0, 0, 7, 0, 1, 0, 0, 6, 8],
      [8, 0, 3, 0, 0, 0, 0, 2, 0],
      [1, 0, 0, 9, 8, 0, 0, 4, 0]]

S2 = [[0, 0, 0, 1, 0, 0, 6, 0, 9],
      [0, 2, 0, 8, 0, 0, 5, 0, 0],
      [4, 7, 1, 0, 5, 0, 0, 0, 0],
      [0, 0, 4, 0, 0, 5, 0, 0, 2],
      [0, 5, 0, 0, 0, 0, 0, 0, 0],
      [1, 0, 7, 4, 0, 0, 0, 0, 8],
      [0, 0, 0, 0, 0, 0, 0, 4, 0],
      [3, 0, 0, 0, 0, 6, 0, 0, 0],
      [2, 0, 0, 9, 0, 0, 0, 0, 1]]
S3 = [[0, 0, 5, 0, 0, 9, 2, 1, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 6],
      [8, 2, 0, 0, 0, 0, 7, 0, 0],
      [0, 0, 2, 0, 0, 5, 0, 3, 4],
      [0, 9, 0, 0, 7, 0, 0, 0, 0],
      [4, 0, 0, 8, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 4, 7, 0, 0, 2],
      [0, 0, 6, 5, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 9, 0]]

S4 = [[8, 0, 0, 0, 4, 5, 0, 0, 7],
      [0, 7, 0, 0, 0, 0, 0, 4, 0],
      [0, 5, 0, 3, 0, 0, 8, 0, 2],
      [0, 0, 0, 1, 0, 0, 0, 0, 8],
      [9, 8, 0, 0, 5, 0, 0, 7, 3],
      [1, 0, 0, 0, 0, 9, 0, 0, 0],
      [2, 0, 7, 0, 0, 6, 0, 8, 0],
      [0, 4, 0, 0, 0, 0, 0, 2, 0],
      [5, 0, 0, 2, 7, 0, 0, 0, 9]]

# Die Zulässigkeitsüberprüfung einer Teilbelegung des Sudoku-Feldes wird
# durchgeführt, wenn ein neuer Eintrag in Zeile z und Spalte s erfolgt ist.
def zulaessig(S, z, s):
    # Wir überprüfen, ob die neu gesetzte Ziffer S[z][s] schon in der Zeile z vorkommt.
    for j in range(9):
        if j == s:
            # Wir überspringen den Feldeintrag S[z][s]
            continue
        if S[z][s] == S[z][j]:
            return(False)

    # Wir überprüfen, ob die neu gesetzte Ziffer S[z][s] schon in der Spalte s vorkommt.
    for i in range(9):
        if i == z:
            # Wir überspringen den Feldeintrag S[z][s]
            continue
        if S[z][s] == S[i][s]:
            return(False)

    # Wir überprüfen, ob die neu gesetzte Ziffer S[z][s] schon in dem 3x3 Block vorkommt,
    # zu dem der Eintrag mit den Indizes (z,s) gehört.
    zb = 3*(z//3)
    sb = 3*(s//3)
    for i in range(zb,zb+3):
        for j in range(sb,sb+3):
            if i == z and j == s:
                # Wir überspringen den Feldeintrag feld[z][s]
                continue
            if S[z][s] == S[i][j]:
                return(False)
    return(True)

# Eine Hilfsfunktion zum Auffinden eines noch freien Eintrages.
def freiesFeld(S):
    for i in range(9):
        for j in range(9):
            if S[i][j] == 0:
                return(i,j)
    return(-1,-1)

# Wir lösen das Sudoku mit Hilfe der Backtracking-Methode.
# Das Sudoku-Feld S stellt eine Teillösung dar, die es zu vervollständigen gilt.
# Das übergebene Feld S wird in der Funktion verändert.
def vervollstaendige(S):
    # Wir suchen zunächst einen noch freien Feldeintrag.
    z,s = freiesFeld(S)
    if z == -1 and s == -1:
        # Es gibt keinen freien Feldeintrag mehr, d.h. wir haben das Sudoku gelöst.
        return(True)

    # Wir belegen das freie Feld in Zeile z und Spalte s nacheinander mit den
    # möglichen Ziffern 1 bis 9. Falls durch diese Belegung kein Konflikt mit
    # schon vorhandenen Ziffern auftritt, versuchen wir die entstandene Belegung
    # durch eine rekursive Anwendung der vervollstaendige-Funktion weiter zu einer
    # Gesamtlösung auszubauen.
    for ziffer in range(1,10):
        # Wir belegen das noch freie feld[z[s] mit der Ziffer ziffer
        S[z][s] = ziffer
        # und überprüfen die Zulässigkeit.
        if zulaessig(S, z, s):
            # Wenn dadurch kein Konflikt zu vorhandenen Einträgen auftritt, versuchen
            # wir die diese Teillösung zu vervollständigen.
            if vervollstaendige(S):
                # Es ist gelungen, eine Gesamtlösung zu finden. Wir brechen die Suche ab.
                return(True)
        # Wir entfernen die gesetzte Ziffer wieder. Dies entspricht dem Backtracking-Schritt.
        S[z][s] = 0
    # Keine Ziffer hat zum Erfolg geführt, d.h. die Startbelegung kann in keinem Fall
    # zu einer Gesamtlösung vervollständigt werden. Dies führt in der aufrufenden Funktion
    # zu einem Backtracking-Schritt.
    return(False)# Eine Hilfsfunktion zum Auffinden eines noch freien Eintrages.
def freiesFeld(S):
    for i in range(9):
        for j in range(9):
            if S[i][j] == 0:
                return(i,j)
    return(-1,-1)

# Wir lösen das Sudoku mit Hilfe der Backtracking-Methode.
# Das Sudoku-Feld S stellt eine Teillösung dar, die es zu vervollständigen gilt.
# Das übergebene Feld S wird in der Funktion verändert.
def vervollstaendige(S):
    # Wir suchen zunächst einen noch freien Feldeintrag.
    z,s = freiesFeld(S)
    if z == -1 and s == -1:
        # Es gibt keinen freien Feldeintrag mehr, d.h. wir haben das Sudoku gelöst.
        return(True)

    # Wir belegen das freie Feld in Zeile z und Spalte s nacheinander mit den
    # möglichen Ziffern 1 bis 9. Falls durch diese Belegung kein Konflikt mit
    # schon vorhandenen Ziffern auftritt, versuchen wir die entstandene Belegung
    # durch eine rekursive Anwendung der vervollstaendige-Funktion weiter zu einer
    # Gesamtlösung auszubauen.
    for ziffer in range(1,10):
        # Wir belegen das noch freie feld[z[s] mit der Ziffer ziffer
        S[z][s] = ziffer
        # und überprüfen die Zulässigkeit.
        if zulaessig(S, z, s):
            # Wenn dadurch kein Konflikt zu vorhandenen Einträgen auftritt, versuchen
            # wir die diese Teillösung zu vervollständigen.
            if vervollstaendige(S):
                # Es ist gelungen, eine Gesamtlösung zu finden. Wir brechen die Suche ab.
                return(True)
        # Wir entfernen die gesetzte Ziffer wieder. Dies entspricht dem Backtracking-Schritt.
        S[z][s] = 0
    # Keine Ziffer hat zum Erfolg geführt, d.h. die Startbelegung kann in keinem Fall
    # zu einer Gesamtlösung vervollständigt werden. Dies führt in der aufrufenden Funktion
    # zu einem Backtracking-Schritt.
    return(False)

# Wir lösen ein schwieriges Sudoku
feld = S1
print(vervollstaendige(feld))

# und geben die Lösung aus.
for i in range(9):
    for j in range(9):
        print(feld[i][j],end='')
    print()

