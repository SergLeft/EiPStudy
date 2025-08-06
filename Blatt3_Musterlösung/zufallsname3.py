import random

name1 = input("Bitte geben Sie einen Namen ein: ")
name2 = input("Bitte geben Sie einen weiteren Namen ein: ")
name3 = input("Bitte geben Sie einen weiteren Namen ein: ")

# random.random() gibt einen gleichverteilten zufälligen Wert zwischen 0 und 1 zurück.
r = random.random()
if r < 0.25:
    print("Hello ", name1)
elif r < 0.75:  # Wir wissen das r > 0.25
    print("Hello ", name2)
else:
    print("Hello ", name3)


# Hier ziehen wir uns einen zufälligen Index
namens_liste = [name1, name2, name3]
# random.choices gibt eine einelementige Liste zurück, daher müssen nach dem Aufruf auf das eizige und damit 0te Element
# zugreifen
zufalls_name = random.choices(namens_liste, weights=[1, 2, 1])[0]

print("Hello ", zufalls_name)
