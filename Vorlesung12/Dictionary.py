# Verwendung von Wörterbüchern (engl. dictionaries)
# Anlegen eines dict mit deutsch-englischen Wortpaaren der Form Schlüssel:Inhalt (engl. key : value)
DE = {'Haus':'house','Baum':'tree','Garten':'garden','Dach':'roof'}
# Hinzufügen eines weiteren Wortpaares: key = 'Auto', value = 'car'
DE.update({'Auto':'car'})
# Suche nach dem Schlüssel 'Baum'
print(DE.get('Baum'))
# Löschen des Schlüssel:Inhalt-Paares zum Schlüssel 'Baum'
DE.pop('Baum')
# Ausgabe des gesamten dict.
print(DE)
# Intuitive Schreibweise zum Einfügen des Schlüssel-Inhalt-Paares 'Baum':'tree'
DE['Baum'] = 'tree'
# Erneute Ausgabe des gesamten dict.
print(DE)

# Erstellen eines inversen englisch-deutschen Wörterbuches
# Initialisierung eines leeren dict.
ED = {} # dict()
# Wir iterieren über alle Schlüssel des deutsch-englischen Wörterbuches
for x in DE.keys():
    # und verwenden die englische Übersetzung DE[x] des deutschen Wortes x
    # als Schlüssel zu x im englisch-deutschen Wörterbuch.
    ED[DE[x]] = x
# Ausgabe des englisch-deutschen Wörterbuches.
print(ED)
print(ED['tree'])

D = dict()

datei = open('data/Woerterbuch.txt',encoding='utf-8')

for zeile in datei:
    wort = zeile.split('\t')
    # print(wort[0],wort[1])
    D.update({wort[0]:wort[1]})

datei.close()

while True:
    wort = input('de = ')
    print(D.get(wort))


