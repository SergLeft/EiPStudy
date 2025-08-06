datei = open('Training.hrm','r')
# Wir lesen zunaechst nur die erste Zeile der Datei, damit wir später nur die Zahlen einlesen
zeile = datei.readline()

summe = 0
counter = 0
for zeile in datei:
    infos = zeile.split("\t")
    puls = int(infos[0])
    speed = int(infos[1])
    if puls > 150:
        summe += speed
        counter += 1
datei.close()

mean = summe / counter
print("Die Durchschnittliche Geschwindikeit bei einem Puls > 150 ist %.3f" % mean)

# b)
import os
tage = os.listdir("sessions/")

for tag in tage:
    summe = 0
    counter = 0
    trainings = os.listdir(os.path.join("sessions", tag))
    for training in trainings:
        datei = open(os.path.join("sessions", tag, training),'r')
        zeile = datei.readline()
        for zeile in datei:
            infos = zeile.split("\t")
            puls = int(infos[0])
            speed = int(infos[1])
            summe += speed
            counter += 1
        datei.close()
    mean = summe / counter
    print(f"Tag {tag}: %.2f" % mean)
