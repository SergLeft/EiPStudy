class Tier:
    def __init__(self, name, ruf):
        self.name = name
        self.ruf = ruf

    def rufen(self):
        print(f'{self.name} ruft {self.ruf}')

    def bewegen(self):
        pass


class LandTier(Tier):
    # def __init__(self, *args):
    #     super().__init__(*args)
    def __init__(self, name, ruf):
        super().__init__(name, ruf)

    def laufen(self):
        print(f'{self.name} läuft')

    def bewegen(self):
        self.laufen()
        super().bewegen()


class FlugTier(Tier):
    def __init__(self, *args):
        super().__init__(*args)

    def fliegen(self):
        print(f'{self.name} fliegt')

    def bewegen(self):
        self.fliegen()
        super().bewegen()


class WasserTier(Tier):
    def __init__(self, *args):
        super().__init__(*args)

    def schwimmen(self):
        print(f'{self.name} schwimmt')

    def bewegen(self):
        self.schwimmen()
        super().bewegen()


class FlugLandTier(FlugTier, LandTier):
    def __init__(self, *args):
        super().__init__(*args)


class FlugWasserTier(FlugTier, WasserTier):
    def __init__(self, *args):
        super().__init__(*args)


class LandWasserTier(LandTier, WasserTier):
    def __init__(self, *args):
        super().__init__(*args)


class FlugLandWasserTier(FlugTier, LandTier, WasserTier):
    def __init__(self, *args):
        super().__init__(*args)


taube = FlugLandTier('Taube', 'gurr')
taube.rufen()
taube.bewegen()

ente = FlugLandWasserTier('Ente', 'quak')
ente.bewegen()

# f)
print(FlugLandTier.mro())
# MRO = Method resolution order
# Die Reihenfolge der Vererbung ist:
# 1. FlugLandWasserTier
# 2. FlugTier
# 3. LandTier
# 4. WasserTier
# 5. Tier
# Daher ruft dann FlugLandWasserTier.bewegen() FlugTier.bewegen() auf, der super().bewegen() von FlugTier ruft dann LandTier.bewegen() auf usw.
