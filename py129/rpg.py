import random

class ArmorMixin:
    def attach_armor(self):
        self.armor = 'on'

    def remove_armor(self):
        self.armor = 'off'

class MagicMixin:
    def cast_spell(self, spell):
        #STUB
        pass

class Player:
    RANDOM_LOW = 2
    RANDOM_HIGH = 12
    FULL_HEALTH = 100

    def __init__(self, name):
        self.name = name
        self.health = Player.FULL_HEALTH
        self.strength = 0
        self.intelligence = 0
        self.set_strength()
        self.set_intelligence()
        

    def __str__(self):
        return f"""
            Name: {self.name}
            Class: {self.__class__.__name__}
            Health: {self.health}
            Strength: {self.strength}
            Intelligence: {self.intelligence}
            """

    def set_strength(self):
        self.strength = self._roll_dice()

    def set_intelligence(self):
        self.intelligence = self._roll_dice()

    def _roll_dice(self):
        return random.randint(self.__class__.RANDOM_LOW, self.__class__.RANDOM_HIGH)

    def heal(self, value):
        self.health += value

    def hurt(self, value):
        self.health -= value

class Warrior(ArmorMixin, Player):
    def __init__(self, name):
        super().__init__(name)
        self.strength += 2
        self.armor = 'off'

class Paladin(MagicMixin, ArmorMixin, Player):
    def __init__(self, name):
        super().__init__(name)
        self.armor = 'off'

class Magician(MagicMixin, Player):
    def __init__(self, name):
        super().__init__(name)
        self.intelligence += 2

class Bard(Magician):
    def __init__(self, name):
        super().__init__(name)

    def create_potion(self):
        #STUB
        pass

class RPG:
    PLAYER_TYPES = [Warrior, Paladin, Bard, Magician]

    def __init__(self, player_type):
        self.player = player_type()

    def play(self):
        #STUB
        pass

magician = Magician('Merlin')
print(magician)
bard = Bard('Shakespeare')
print(bard)
paladin = Paladin('Snoop')
print(paladin)
warrior = Warrior('Atilla')
print(warrior)