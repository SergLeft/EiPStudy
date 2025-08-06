class Auto :
    def __init__(self, baujahr:int, gewicht:float):
        self.baujahr = baujahr
        self.gewicht = gewicht

    def __repr__(self):
        return f'Auto({self.baujahr}, {self.gewicht})'

def berechne_histogram(liste:list[Auto]):
    d = {}
    for car in liste:
        jahrzent = car.baujahr // 10
        if jahrzent not in d:
            d[jahrzent] = [car.gewicht]
        else:
            d[jahrzent].append(car.gewicht)
    erg = []
    for k in d.keys():
        car = Auto(k * 10, sum(d[k]) / len(d[k]))
        erg.append(car)
    return erg


verkaufe = [Auto(2017,2300.0), Auto(1955,910.0),
            Auto(1985,1230.0), Auto(2015,1700.0)]

ergebnis = berechne_histogram(verkaufe)
print(ergebnis)
