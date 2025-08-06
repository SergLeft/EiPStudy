import random


class Game:
    def __init__(self):
        self.characters = []

    def add_character(self, character):
        self.characters.append(character)

    def play(self):
        while len(self.characters) > 1:
            attacker = random.choice(self.characters)
            defender = random.choice(self.characters)
            if attacker != defender:
                attacker.attack(defender)
                if defender.health <= 0:
                    self.characters.remove(defender)
                    print(f"{defender.name} has died.")
        print(f"{self.characters[0].name} has won the game.")


# Base class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.take_damage(self.attack_power, self)

    def compute_damage(self, damage):
        return damage

    def take_damage(self, damage, from_):
        damage = self.compute_damage(damage)
        self.health -= damage
        print(f"{self.name} takes {damage} damage from {from_.name} and has {self.health} health left.")


# Don't change the code above
# -----------------------------

class Knight(Character):
    def __init__(self, name, health, attack_power, armor):
        super().__init__(name, health, attack_power)
        self.armor = armor

    def compute_damage(self, damage):
        return max(0, damage - self.armor)


class Wizard(Character):
    def __init__(self, name, health, attack_power, mana):
        super().__init__(name, health, attack_power)
        self.mana = mana

    def attack(self, other):
        if self.mana >= 10:
            spell_damage = self.attack_power * 2
            self.mana -= 10
        else:
            spell_damage = self.attack_power // 2
        other.take_damage(spell_damage, self)


class Thief(Character):
    def __init__(self, name, health, attack_power, dodge_chance: float):
        super().__init__(name, health, attack_power)
        self.dodge_chance = dodge_chance

    def take_damage(self, damage, from_):
        r = random.random()
        if r < self.dodge_chance:
            print(f"{self.name} dodged the attack from {from_.name} and has {self.health} health left.")
        else:
            super().take_damage(damage, from_)


game = Game()
game.add_character(Character("Gollum", 50, 10))
game.add_character(Knight("Batman", 70, 10, 5))
game.add_character(Wizard("Harry Potter", 80, 14, 40))
game.add_character(Thief("Robin Hood", 70, 9, 0.2))
game.play()
