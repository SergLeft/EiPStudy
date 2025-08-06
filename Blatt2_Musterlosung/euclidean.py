import math

ux = 2
uy = 0

ax = 16
ay = 6

# a)
print("a)")
d = math.sqrt((ux - ax)**2 + (uy - ay)**2)
print("Der Fusweg beträgt %.2f LE" % d)

# b)
# H = (18, 2), G = (12, 12)
print("b)")

hx = 18
hy = 2

gx = 12
gy = 12

# Berechne Fußweg zum Höfchen von Wohnort A
fusweg_hofchen = math.sqrt((hx - ax)**2 + (hy - ay)**2)
# Berechne Fußweg zur Goethestraße von Wohnort A
fusweg_goethe = math.sqrt((gx - ax)**2 + (gy - ay)**2)

if fusweg_hofchen > fusweg_goethe:
    print("Der Fußweg zur Goethestraße ist kürzer!")
else:
    print("Der Fußweg zum Höfchen ist kürzer!")

# c)
print("c)")

busweg_hofchen = math.sqrt((hx - ux)**2 + (hy - uy)**2)  # in LE
bahnweg_goethe = math.sqrt((gx - ux)**2 + (gy - uy)**2)  # in LE

buszeit_hofchen = busweg_hofchen / 2  # in min
bahnzeit_goethe = bahnweg_goethe / 3  # in min

# Für Fußwege: bereits in min, da min gleich LE

verfugbare_zeit = 15  # in min

if d < verfugbare_zeit:
    print("Zu Fuß schaffen Sie es rechtzeitig")
else:
    print("Zu Fuß schaffen Sie es nicht rechtzeitig")

if fusweg_hofchen + buszeit_hofchen < verfugbare_zeit:
    print("Übers Höfchen schaffen Sie es rechtzeitig")
else:
    print("Übers Höfchen schaffen Sie es nicht rechtzeitig")

if fusweg_goethe + bahnzeit_goethe < verfugbare_zeit:
    print("Über die Goethestraße schaffen Sie es rechtzeitig")
else:
    print("Über die Goethestraße schaffen Sie es nicht rechtzeitig")

if d < fusweg_hofchen + buszeit_hofchen and d < fusweg_goethe + bahnzeit_goethe:
    print("Der Fußweg ist am schnellsten")
elif fusweg_hofchen + buszeit_hofchen < fusweg_goethe + bahnzeit_goethe:
    print("Übers Höfchen ist es am schnellsten")
else:
    print("Über die Goethestraße ist es am schnellsten")

