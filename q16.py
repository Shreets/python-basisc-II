# 16. Imagine you are creating a Super Mario game. You need to define a class to represent Mario. What would it look like?
# If you aren't familiar with SuperMario, use your own favorite video or board game to model a player.


class Wizard:
    attack = 15

    def __init__(self, name, spell, power):
        self.name = name
        self.spell = spell
        self.power = power

    def spells(self):
        print(f'{self.name}! You have now possessed spell of {self.spell}. With this you can {self.power}')

    def attacks(self):
        self.attack -= 1
        print(f'Total attack remaining for {self.name} :  {self.attack}')


player1 = Wizard('Gandalf', 'Enchantment', 'stun the enemy for 30 seconds')
player1.spells()
player1.attacks()
player1.attacks()
player1.attacks()

player2 = Wizard('Saruman', 'Posession', 'make use of enemy\'s spell of your liking')
player2.spells()
player2.attacks()

# output

# Gandalf! You have now possessed spell of Enchantment. With this you can stun the enemy for 30 seconds
# Total attack remaining for Gandalf :  14
# Total attack remaining for Gandalf :  13
# Total attack remaining for Gandalf :  12

# Saruman! You have now possessed spell of Posession. With this you can make use of enemy's spell of your liking
# Total attack remaining for Saruman :  14