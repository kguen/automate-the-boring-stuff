import zombiedice, random

class RandomRoll:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        
        while diceRollResults is not None:
            isContinue = random.randint(0, 1)
            if isContinue == 0:
                break
            else:
                diceRollResults = zombiedice.roll()

class UntilTwoBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        
        while diceRollResults is not None:
            brains = diceRollResults['brains']
            if brains == 2:
                break
            diceRollResults = zombiedice.roll()

class UntilTwoShotguns:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        
        while diceRollResults is not None:
            shotguns = diceRollResults['shotgun']
            if shotguns == 2:
                break
            diceRollResults = zombiedice.roll()

class NotMoreThan4Rolls:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        rolls = random.randint(0, 3)
        
        while diceRollResults is not None and rolls:
            shotguns = diceRollResults['shotgun']
            if shotguns == 2:
                break
            diceRollResults = zombiedice.roll()
            rolls -= 1

class UntilMoreGunsThanBrains:
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        while diceRollResults is not None:
            shotguns = diceRollResults['shotgun']
            brains = diceRollResults['brains']
            if shotguns > brains:
                break
            diceRollResults = zombiedice.roll()
            

zombies = (
    RandomRoll(name = 'Random'),
    UntilTwoBrains(name = 'Until Two Brains'),
    UntilTwoShotguns(name = 'Until Two Shotgun'),
    NotMoreThan4Rolls(name = 'Not More Than 4 Rolls'),
    UntilMoreGunsThanBrains(name = 'Until More Guns Than Brains')
)

#zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)