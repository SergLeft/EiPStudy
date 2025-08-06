import time

# Wir öffnen die utf-8-Datei der deutschen Wörter zum Lesen.
# datei = open('data/Deutsche-Woerter.txt','r',encoding='utf-8')
datei = open('data/Substantive.txt','r',encoding='iso-8859-1')
# Wir initialisieren eine leere Wortliste namens lexikon.
lexikon = []
# Wir lesen die Textdatei zeilenweise.
for zeile in datei:
    # Wir splitten die Zeichenkette zeile in einzelne Wörter anhand von Whitespace-Zeichen.
    wortListe = zeile.split()
    # In unserem Fall erhalten wir nur ein Wort pro Zeile - ohne Zeilenvorschub.
    # Wir hängen dieses Wort ans Ende unseres Lexikons.
    lexikon.append(wortListe[0])
# Wir schließen die Datei.
datei.close()
# Wir sortieren die Wörter im Lexikon lexikographisch.
lexikon.sort()
# Wir öffnen eine neue Textdatei zum Schreiben.
datei = open('data/Lexikon.txt','w',encoding='utf-8')
# Wir schreiben der Reihe nach alle Wörter unserer sortierten Wortliste zeilenweise in die Datei.
for wort in lexikon:
    # Nach jedem Wort findet ein Zeilenvorschub statt.
    datei.write(wort+'\n')
# Wir schließen die Datei wieder.
datei.close()

# Wir definieren ein Suchwort.
suchwort = 'Programm'
# Wir stoppen die Zeit für die binäre Suche.
t1 = time.time()

# Wir wollen folgende Invariante während der binären Suche aufrechterhalten:
# lexikon[links] <= suchwort <= lexikon[rechts]

n = len(lexikon)
# Zu Beginn setzen wir die linke Grenze des Suchintervalls auf die Listenposition 0
# und die rechte Grenze auf die Position des Listenendes.
links = 0
rechts = n-1
# i zählt die Zahl der Unterteilungsschritte.
i = 0
# Solange das Suchintervall nicht leer geworden ist, setzen wir die Suche fort.
while links <= rechts:
     # Wir berechnen die Mitte des Suchintervalls.
    mitte = (links+rechts)//2
    # Wir geben zur Kontrolle das Wort in der Mitte des aktuellen Suchintervalls aus.
    print(lexikon[mitte])
    i += 1
    # Wir entscheiden, ob wir die Suche links von der Mitte fortsetzen sollen.
    if suchwort < lexikon[mitte]:
        # und passen dementsprechend die neue rechte Grenze an.
        rechts = mitte-1
    # Wir überprüfen, ob wir die Suche rechts der Mitte fortsetzen sollen.
    elif suchwort > lexikon[mitte]:
        # und passen die neue linke Grenze an.
        links = mitte+1
    else:
        # Wir haben das Suchwort gefunden
        gefunden = True
        # und können die Suche abbrechen.
        break
else:
    # Das Suchwort konnte nicht gefunden werden.
    gefunden = False

# Wir stoppen erneut die Zeit.
t2 = time.time()

# Wir geben aus, ob wir das Wort in unserem Lexikon gefunden haben.
print(gefunden)
# Wir geben die benötigte Laufzeit aus
print('Laufzeit = ',t2-t1)
# und auch die Zahl der Unterteilungsschritte.
print('Zahl der Suchschritte = ',i)
