dishes = []

# Einlesen
file = open('mensa.tsv', 'r', encoding='utf-8')
for dish in file:
    infos = dish.split('\t')
    dishes.append((infos[0], int(infos[1]), float(infos[2])))
file.close()

# Dictionary erstellen
average_ratings = {}
for dish in dishes:
    if dish[0] not in average_ratings:
        average_ratings[dish[0]] = [ [dish[1]], [dish[2]]]
    else:
        average_ratings[dish[0]][0].append(dish[1])
        average_ratings[dish[0]][1].append(dish[2])

# Durchschnittliches Rating berechnen
for dish in average_ratings.keys():
    average_ratings[dish][1] = sum(average_ratings[dish][1]) / len(average_ratings[dish][1])

# Gerichte mit einem schlechterem Rating als 2.5 aussortieren
best_dishes = {}
for dish in average_ratings.keys():
    if average_ratings[dish][1] >= 2.5:
        best_dishes[dish] = average_ratings[dish]

# Nur als Hinweis dass es auch Dict-Comprehensions gibt. Funktionieren wie List-Comprehensions
best_dishes2 = {k:v for k, v in best_dishes.items() if v[1] >= 2.5}

# Durchschnittlichen alten Preis berechen
alter_preis = []
for dish in dishes:
    alter_preis.append(dish[1])
alter_preis = sum(alter_preis) / len(alter_preis)

# Durchschnittlichen neuen Preis berechen
neuer_preis = []
for dish in best_dishes.keys():
    preise = best_dishes[dish][0]
    for preis in preise:
        neuer_preis.append(preis)
neuer_preis = sum(neuer_preis) / len(neuer_preis)

print("Alter Preis: ", alter_preis)
print("Neuer Preis: ", neuer_preis)