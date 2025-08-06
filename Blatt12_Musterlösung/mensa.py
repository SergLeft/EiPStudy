def read_tsv(filename: str):
    dishes = []
    with open(filename, 'r', encoding="utf-8") as file:
        dishes = [(lambda t: (t[0], int(t[1]), float(t[2])))(line.strip().split('\t')) for line in file]
    return dishes


dish_list = read_tsv('mensa.tsv')


# Hier kommt dein Code hin.
class Dish:
    def __init__(self, name, price, rating):
        self.name = name
        self.price = price
        self.rating = rating

    def __str__(self):
        return self.name + ' (' + str(self.price / 100) + '€)' + ' [' + str(self.rating) + ']'

    def __eq__(self, other: 'Dish') -> bool:
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


# a)
dish_list = [Dish(dish[0], dish[1], dish[2]) for dish in dish_list]
# l = []
# for dish in dish_list:
#     l.append(Dish(dish[0], dish[1], dish[2]))
# c)
vergleichs_dish = Dish('Veggi Kraut Dog- XXL Hot Dog mit knackigem Kraut und Röstzwiebeln (1,2,Gl,Ei,So,Sl,Sf,We)', 0,
                       0)
counter = 0
for dish in dish_list:
    if dish == vergleichs_dish:
        counter += 1
print(counter)

d = {}
for dish in dish_list:
    if dish not in d:
        d[dish] = []

    d[dish].append(dish.rating)

for dish in d:
    average = sum(d[dish]) / len(d[dish])
    print(dish.name + f': {average} bei {len(d[dish])} Bewertungen')
