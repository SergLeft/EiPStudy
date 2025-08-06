# a)
# Vom i-ten zum (i+1)-ten Spieltag werden alle Mannschaften (bis auf die letzte (hier die 9.)) um einen Platz rotiert.
# Die Mannschaft die auf dem oberen Platz (anfangs das 0. Team) spielt gegen die letzte (hier 9.) Mannschaft abwechseln
# daheim und auswärts.
# Mathematisch: Wir nummerieren ein Platz entsprechend der Mannschafts-Nummer am 0. Spieltag, d.h. die Mannschaft auf
# dem 8. Platz spiel zuhause gegen die Mannschaft auf dem 1. Platz, wobei der letzte (hier 9.) Platz besonders ist.
# Gegeben sind n (gerade) Mannschaften. Dann spielt immer der i-te Platz gegen den (n-i-1)-ten Platz, wobei die Mannschaft
# auf einem geraden Platz (außer dem 0. und n-ten Platz) die Heimmanschaft ist. Nach dem Spieltag rotieren die
# Mannschaften einen Platz weiter, mit Außnahme der Mannschaft auf dem letzten Platz, die die ganze Saison auf dem
# letzten Platz bleibt. Die Mannschaft auf dem letzten Platz spiel bei jedem geraden Spieltag zuhause.

# b)
datei = open("Bundesliga-Klubs.txt", "r", encoding='utf-8')
vereine = [verein.replace("\n", "") for verein in datei]
datei.close()

# Letzte Mannschaft is fix
letzer_verein = vereine.pop(-1)

for n in range(len(vereine)):
    print(n, ". Spieltag")
    if n % 2 == 0:
        print(letzer_verein, " vs. ", vereine[0])
    else:
        print(vereine[0], " vs. ", letzer_verein)

    # Auf dem Beispiel auf dem Arbeitsblatt haben wir zehn Vereine, wobei wir einen bereits entfernt haben. Unsere Liste
    # hat also die Länge 9. Um alle Spiele auszugeben müssen wir von 1 bis inklusive 4 iterieren. D.h. wir brauchen eine
    # range(1, 5)
    for m in range(1, len(vereine) // 2 + 1):
        if m % 2 == 0:
            # Alternative: print(vereine[m], " vs. ", vereine[len(vereine) - m])
            print(vereine[m], " vs. ", vereine[-m])
        else:
            print(vereine[-m], " vs. ", vereine[m])

    # Rotation
    temp = vereine.pop(0)
    vereine.append(temp)

# c)
# 1. Jeder spielt gegen jeden anderen:
# Die fixierte Mannschaft (Mannschaft 6) spielt der Reihe nach gegen alle anderen:
# Da sie immer am gleichen Platz bleibt und die anderen vorbeirotieren, trifft sie jede genau einmal.
# Die rotierenden Mannschaften treffen sich ebenfalls alle:
# Durch die ständige Rotation bei einer ungeraden Anzahl an Mannschaften im Kreis spielt jede Mannschaft beim nächsten
# Spieltag gegen die Mannschaft hinter dem aktuellen Gegner. Dadurch kommen alle möglichen Kombinationen vor.
# 2. Keine Wiederholungen
# Das System verhindert Wiederholungen durch seine feste Struktur:
# Jeder Spieler (außer dem fixierten) durchläuft systematisch alle Positionen
# Da es genau n-1 Runden für n Spieler gibt, und jeder Spieler in jeder Runde gegen genau einen anderen spielt, können
# keine Paarungen doppelt vorkommen.
