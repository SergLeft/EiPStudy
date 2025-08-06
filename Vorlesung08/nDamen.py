# Lösung des n-Damen Problems mittels Backtracking
# Siehe https://de.wikipedia.org/wiki/Damenproblem
# Wir kodieren eine Stellung der Damen auf einem nxn Schachbrett,
# indem wir ein eindimensionales Feld S benutzen.
# Pro Spalte i kann sich nur eine Dame aufhalten. Die Dame
# in Spalte i befinde sich in der Zeile S[i].

# Überprüfung der Zulässigkeit einer Stellung S.
# Die Stellung muss noch nicht vollständig sein.
def zulaessig(S):
    # Es wurden bisher k Damen in den Spalten 0 bis k-1 platziert.
    k = len(S)
    # Wir überprüfen, ob die zuletzt platzierte Dame in Spalte (k-1)
    # eine zuvor platzierte Dame schlagen kann.
    for i in range(k-1):
        if S[i] == S[k - 1]:
            # Die Dame in Spalte i steht in der selben Zeile wie die
            # Dame in der (k-1)-ten Spalte.
            return(False)
        if (S[k-1]-S[i]) == k-1-i:
            # Die Dame in Spalte i und die Dame in Spalte (k-1) können
            # sich diagonal schlagen.
            return(False)
        if (S[k-1]-S[i]) == -(k-1-i):
            # Analog zum vorherigen Fall, mit negativer Diagonalensteigung.
            return(False)
    return(True)

# Im Backtracking-Algorithmus versuchen wir, eine Teillösung, die durch das
# Feld S kodiert ist, zu vervollständigen.
# Man beachte, dass das Feld S in der Funktion vervollstaendige verändert wird.
def vervollstaendige(S):
    # Der Rekursionsanker.
    if len(S) == n:
        # Wir haben eine vollständige Lösung mit n Damen gefunden.
        return(True)
    # Wir suchen eine Platzierung für die Dame in der nächsten Spalte.
    # Dafür kommen alle Positionen innerhalb dieser Spalte in Frage.
    for i in range(n):
        # Wir hängen die gewählte Position/Zeilennummer an unser Stellungsfeld an
        S.append(i)
        # und überprüfen, ob die dadurch neu geschaffene Stellung zulässig ist.
        if zulaessig(S):
            # Wenn die Platzierung der neuen Dame zulässig ist, versuchen wir
            # rekursiv die so erweiterte Teillösung zu vervollständigen.
            if vervollstaendige(S):
                # Es ist uns gelungen, eine Gesamtlösung zu finden. Deshalb brechen
                # wir die Suche ab. Das Stellungsfeld S beinhaltet die gefundene Lösung.
                return(True)
        # Die zuvor erzeugte Teillösung war nicht zulässig oder hat sich nicht
        # vervollständigen lassen. Deshalb nehmen wir diese Platzierung der Dame zurück,
        # indem wir die zuletzt platzierte Dame am Feldende wieder löschen.
        S.pop()
    # Es ist uns nicht gelungen, die Teillösung, von der wir gestartet sind, um eine
    # weitere Dame zu ergänzen. Deshalb melden wir der aufrufenden Funktion zurück, dass
    # diese Teillösung nicht Teil einer Gesamtlösung sein kann.
    # Auf diese Weise ersparen wir es uns, all die denkbaren Stellungen von n Damen
    # anzuschauen, die sich als Vervollständigung der betrachteten Startstellung ergeben
    # könnten.
    return(False)

# Die Problemgröße als globale Variable
n = 6
# Wir starten mit der leeren Stellung, bei der noch keine Dame gesetzt wurde.
S = []
# Wir suchen nach einer Lösung.
print(vervollstaendige(S))
# Wir geben die erste gefundene Lösung aus.
print(S)

