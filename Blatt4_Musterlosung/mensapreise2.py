menu = [('Frühlingswoche: Gebratene Hähnchenbrust  mit Frankfurter Grüne Sauce  und neuen Kartoffeln', 3.67), ('Gnocchi  a la romana mit Pilzen und Parmesan  und Tomatensauce', 2.9), ('Penne Rigate - Pastasorte  mit Carbonara-Sauce', 2.5), ('Penne Rigate - Pastasorte  mit Gemüsesauce', 2.5), ('Currywurst vom Schwein  oder Vegane Currywurst  mit Currysauce  und Pommes frites', 3.36), ('verfeinert mit Paprika, Oliven und Hüttenkäse  oder Spiralli  und Tomatensauce', 2.58), ('Schwäbischer Rahmbraten  mit Rahmsauce  und Kartoffeln', 3.18), ('Frühlingswoche: Spargel mit Sauce Hollandaise  und Kartoffeln', 4.78), ('Penne Rigate - Pastasorte  mit Carbonara-Sauce', 2.5), ('Penne Rigate - Pastasorte  mit Gemüsesauce', 2.5), ('Mohnnudeln  mit Dessertsauce "Vanillegeschmack"', 2.59), ('Fully loaded fries "BBQ Pulled Pork", Pommes frites getoppt mit Pulled Pork, Zwiebeln und BBQ Sauce', 3.67), ('Schwäbische Maultaschen  mit Zwiebelbrühe', 2.58), ('Bärlauchknödel  mit Pilzragout von frischen Champignons u. Austernpilzen', 4.08), ('Penne Rigate - Pastasorte  mit Carbonara-Sauce', 2.5), ('Penne Rigate - Pastasorte  mit Gemüsesauce', 2.5), ('Paniertes Schnitzel XXL', 3.52), ('"Gai Pad Prik" mit gegrilltem Gemüse und Hähnchen  oder Reis', 3.19), ('Frühlingswoche: Spargelragout mit Hähnchenstreifen  und Reis', 3.51), ('Spinatknödel  mit Käsesauce', 3.21), ('Penne Rigate - Pastasorte  mit Carbonara-Sauce', 2.5), ('Penne Rigate - Pastasorte  mit Gemüsesauce', 2.5), ('oder Rindswurst  oder Vegane Currywurst  mit Currysauce  und Pommes frites', 3.37), ('Schwäbische Spätzle  verfeinert mit Spinat und Feta  und Sahnesauce', 2.56), ('Frühlingswoche Ofenkartoffeln mit Schnittlauch-Sauerrahm Dip  zur Wahl mit Speckstreifen  oder eingelegten Radieschen', 2.49), ('Cremiger Gemüse-Nudelauflauf  getoppt mit Schnittlauchsauce', 2.71), ('Penne Rigate - Pastasorte  mit Carbonara-Sauce', 2.5), ('Penne Rigate - Pastasorte  mit Gemüsesauce', 2.5), ('Mexican Wrap mit Salat und Sauerrahm', 3.46), ('Penne Rigate - Pastasorte  mit sautiertem Broccoli und Karotte mit Käsesauce', 2.54)]

# a)
_min = (menu[0][0], menu[0][1])
for s in menu:
    if s[1] < _min[1]:
        _min = s
# oder
_min = min(menu, key=lambda x: x[1])
print(_min)

# b)
filtered_names = []
filtered_prices = []
for s in menu:
    # das ist zwar nicht effizient aber macht hier nichts
    if s[0] not in filtered_names:
        filtered_prices.append(s[1])
        filtered_names.append(s[0])

mean = sum(filtered_prices) / len(filtered_prices)
print("Das Essen kostet Durchschnittlich %.2f€." % mean)
