class Listenknoten:
    # Konstruktor für einen Listenknoten bestehend aus Inhalt
    # und Verweis auf den nachfolgenden Listenknoten.
    def __init__(self,inhalt):
        self.inhalt = inhalt
        self.next = None

# Die Klasse Liste als abstrakte Datenstruktur.
class Liste:
    def __init__(self):
        self.kopf = None

    # Hinzufügen eines neuen Listenelementes am Anfang der Liste.
    def einfuege(self,inhalt):
        knoten = Listenknoten(inhalt)
        knoten.next = self.kopf
        self.kopf = knoten

    # Suche nach dem Listenknoten mit dem Inhalt element.
    # Der Einfachheit halber bestimmen wir nur, ob das gesuchte Element in der Liste vorhanden ist.
    def suche(self,element):
        # Wir beginnen die Suche am Kopf der Liste
        knoten = self.kopf
        # und laufen bis zum Ende der Liste.
        while knoten != None:
            if knoten.inhalt == element:
                # Wir haben das gesuchte Element gefunden.
                return(True)
            # Wir gehen zum Nachfolger des aktuellen Listenknotens über.
            knoten = knoten.next
        # Wir haben das Listenende erreicht, ohne das gesuchte Element gefunden zu haben.
        return(False)

    
    # Löschen des ersten Listenknotens mit dem Inhalt element.
    def loesche(self,element):
        # Wir starten wieder am Kopf der Liste.
        knoten = self.kopf
        # Wir merken uns beim Durchlaufen der Liste den Vorgängerknoten des aktuellen Listenknotens.
        vorgaenger = None
        while knoten != None:
            if knoten.inhalt == element:
                # Wir haben den zu löschenden Listenknoten gefunden.
                if vorgaenger == None:
                    # Wir müssen den Fall gesondert behandeln, wenn das erste Element der Liste gelöscht werden soll.
                    self.kopf = knoten.next
                else:
                    # Wir setzen den Nachfolgerverweis des Vorgängers auf den Nachfolger des zu löschenden Knotens.
                    vorgaenger.next = knoten.next
                return
            # Wir gehen zum nächsten Listenknoten über und aktualisieren auch den Vorgänger.
            vorgaenger = knoten
            knoten = knoten.next

    # Überladen der str-Funktion zur Ausgabe der kompletten Liste.
    def __str__(self):
        s = ''
        knoten = self.kopf
        while knoten != None:
            s += str(knoten.inhalt)+' '
            knoten = knoten.next
        return(s)

# Anlegen einer leeren Liste durch Aufruf des Konstruktors für Liste.
L = Liste()
# Sukzessives Einfügen der Elemente [0..9]
for i in range(10):
    L.einfuege(i)
# Ausgabe der Liste durch Aufruf der überladenen str-Funktion.
print(L)
# Löschen des Elementes 9.
L.loesche(9)
# Erneute Ausgabe.
print(L)

