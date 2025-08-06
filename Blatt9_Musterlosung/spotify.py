class Song:
    def __init__(self, title, artist, length: int):
        self.title = title
        self.artist = artist
        self.length = length

    def __str__(self):  # Für die str() Funktion, für print() und für den Debugger (nachrangig zu __repr__)
        return f"{self.title} - {self.artist} - {self.length}"

    def __repr__(self):  # Für den Debugger und das Printen von Listen aus Molekülen
        return f"{self.title} - {self.artist}"

class Entry:
    def __init__(self, song: Song):
        self.song = song
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_entry: "Entry"):
        self.next = next_entry

class Playlist:
    def __init__(self, first_song: Song):
        self.first = Entry(first_song)

    def add_front(self, song: Song):
        e = Entry(song)
        e.set_next(self.first)
        self.first = e

    def add_back(self, song: Song):
        # Finde das Element bei dem .next None ist
        entry = self.first
        while entry.next is not None:
            entry = entry.next

        e = Entry(song)
        entry.set_next(e)

    def add_at(self, song: Song, position):
        if position == 0:
            self.add_front(song)
            return
        # Angenommen wir wollen Song x an Position 2 einfügen. Unsere aktuelle Playlist: a, b, c, d. Das heißt nach
        # der Operation soll die Playlist: a, b, x, c, d aussehen. Daher müssen wir b finden, b.next = x und x.next = c
        # setzen.

        # Finde das Element an der Position "position - 1", damit wird dessen .next auf den neuen Song setzen können
        entry = self.first
        for i in range(position - 1):
            entry = entry.next

        e = Entry(song)
        e.set_next(entry.next)
        entry.set_next(e)

    def __str__(self):
        s = "Playlist: "
        entry = self.first
        while entry is not None:
            s += str(entry.song) + " | "
            entry = entry.next
        return s

    def __getitem__(self, key):
        if isinstance(key, slice):
            start, stop = key.start, key.stop
            # Gehe bis zum Start
            entry = self.first
            for i in range(0, start):
                entry = entry.next
            # Gehe vor Start zum End und füge alle Elemente der Liste hinzu
            l = []
            for i in range(start, stop):
                l.append(entry.song)
                entry = entry.next
            # return l
            # Erstelle aus der Liste aus Songs eine neue Playlist
            new = Playlist(l.pop(0))
            for song in l:
                new.add_back(song)
            return new
        else:
            entry = self.first
            for i in range(key):
                entry = entry.next
            return entry.song

f = open("playlist.txt", "r", encoding="utf-8")
songs = []
for line in f:
    line = line.split(" - ")
    title = line[0]
    artist = line[1]
    # Length m:ss zu int in sec
    length = line[2]
    m, s = length.split(":")
    length = int(s) + 60 * int(m)
    song = Song(title, artist, length)
    songs.append(song)

playlist = Playlist(songs.pop(0))
for song in songs:
    playlist.add_front(song)

print(playlist)

playlist.add_back(Song("Rock me Amadeus", "Falco", 265))
print(playlist)

print(playlist[9])

playlist.add_at(Song("Rock me Amadeus 2", "Falco", 265), 3)
print(playlist)

print(playlist[1:3])
