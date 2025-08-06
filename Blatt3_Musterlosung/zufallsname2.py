import random

name1 = input("Bitte geben Sie einen Namen ein: ")
name2 = input("Bitte geben Sie einen weiteren Namen ein: ")

# random.random() gibt einen gleichverteilten zufälligen Wert zwischen 0 und 1 zurück. Also ist in der Hälfte der Fälle
# der Wert kleiner als 0.5
if random.random() < 0.5:
    print("Hello ", name1)
else:
    print("Hello ", name2)


# Hier ziehen wir uns einen zufälligen Index
names_liste = [name1, name2]
index = random.randint(0, len(names_liste) - 1)
print("Hello ", names_liste[index])
