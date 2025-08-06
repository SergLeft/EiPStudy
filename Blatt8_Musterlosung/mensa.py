dishes = [('Wedges', 4.5, 105), ('Kartoffeln', 2, 72), ('Buntes Gemüse', 1.5, 72), ('Gemüsesuppe', 2, 72), ('Hausgemachte Käsespätzle', 5, 306), ('Tagesmenü', 4, 378), ('Hausgemachter Weißer Bohneneintopf', 2.5, 222), ('Gebratenes Seelachsfilet', 0, 374), ('Auswahl an angemachten Salaten', 1.7, 89)]

#a)

'''Die Funktion G(i,P) besteht aus den "Basisfällen" i=0 und P=0, offensichtlich muss in beiden Fällen G=0 sein.
Der erste rekursive Fall betrachtet den Fall, dass das Gericht zu teuer ist. In diesem Fall gilt dass G(i,P)=G(i-1,P), da das 
zuletzt "betrachtete" Produkt keinen Einfluss auf den "Geschmack R" haben kann. Der zweite rekursive Fall betrachtet den Fall, dass
wir die Entscheidung treffen müssen, das i-te Gericht zu kaufen, oder es zu lassen. Es wird mit der max Funktion geschaut, ob G mit 
dem Gericht oder ohne das Gericht "größer" ist. Das heißt wir berechnen:
1. G(i-1, P), also das Ergebnis wenn wir das i-te Gericht ignorieren und daher auch den verfügbaren Betrag P nicht ändern.
2. G(i-1, P - p_{i-1}) + g_{i-1}, also das Ergebniss wenn wir das i-te Gericht nehmen, also den Geschmack zu den anderen genommenen
   Gerichten addieren und den restlichen Betrag entsprechen verringern'''

#b)

#     i und P ist int | Rückgabetyp int (mit -> kann man den Rückgabetyp für die Entwicklungsumgebung angeben (Python ist das egal!!))
def G(i: int, P: int) -> int:
    """Berechnet den maximalen Geschmack für die ersten i Gerichte mit einem Guthaben von P"""
    if i == 0 or P == 0:
        return 0
    elif dishes[i-1][2] > P:
        return G(i-1, P)
    else:
        # Langform:
        mit = G(i-1, P - dishes[i-1][2]) + dishes[i-1][1]
        ohne = G(i-1, P)
        if mit > ohne:
            return mit
        else:
            return ohne
        # Kurzform
        # return max(G(i-1, P), G(i-1, P-dishes[i-1][2]) + dishes[i-1][1])

n = len(dishes)
Pmax = 500
print(G(n, Pmax))

#c)

def optimal_dishes(i: int, P: int) -> list:
    """Berechnet den maximalen Geschmack und die Gerichte dafür für die ersten i Gerichte mit einem Guthaben von P"""
    if i == 0 or P == 0:
        return [0, []]  # Kein Geschmack, keine Gerichte
    elif dishes[i-1][2] > P:
        return optimal_dishes(i-1, P)
    else:
        mit = optimal_dishes(i-1, P-dishes[i-1][2])
        mit = [mit[0] + dishes[i-1][1], mit[1] + [dishes[i-1]]]
        ohne = optimal_dishes(i-1, P)
        if mit[0] > ohne[0]:
            return mit
        else:
            return ohne

# Alternative
# def optimal_dishes(i, P):
#     if i == 0 or P == 0:
#         return []
#     elif dishes[i-1][2] > P:
#         return optimal_dishes(i-1, P)
#     else:
#         # Wir formulieren den max-Operator als if/else
#         # Berechne den Geschmack mit oder ohne Gericht i mit Hilfe von G
#         if dishes[i-1][1] + G(i-1, P-dishes[i-1][2]) > G(i-1, P):
#             return optimal_dishes(i-1, P-dishes[i-1][2]) + [dishes[i-1]]  # Füge das Gericht hinzu
#         else:
#             return optimal_dishes(i-1, P)  # Lasse das Gericht weg

n = len(dishes)
Pmax = 500
optimal = optimal_dishes(n, Pmax)
print("Die optimalen Gerichte sind:")
for dish in optimal[1]:
    print(dish[0])
