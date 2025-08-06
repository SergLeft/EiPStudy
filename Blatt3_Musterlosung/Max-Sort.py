# Um ein Liste der Länge n absteigend zu sortieren müssen wir n Mal das Maximum finden (äußere Schleife).
# Pro Durchlauf finden wir das Maximum in  in der restlichen, unsortierten Liste. Dazu benötigen wir im ersten
# Durchlauf n Vergleiche, im zweiten n-1, im dritten n-2, ..., da die restliche, unsortierte Liste pro Durchlauf um eins
# kleiner wird.
# => T(n) = n + (n-1) + (n-2) + ... + 3 + 2 + 1 = n * (n-1) / 2 ~= c * n^2

# Die Laufzeit ist also c * n^2