import re

filename = r'data-2-1.txt'

maxDice = {
    'red' : 12,
    'green' : 13,
    'blue': 14
}



with open(filename) as file:
    
    countGameLowerThanMax = 0

    for line in file:
        # print(line)
        line = line.strip('\n')
        gameId = int(line.split(':')[0].split(' ')[1])
        games = line.split(':')[1].split(';')
        gameLessThanMaxDiceAllow = True
        for game in games:
            for dice in game.split(','):
                diceNumber = int(dice.split(' ')[1])
                diceColour = dice.split(' ')[-1]
                print(diceColour, diceNumber)
                if diceNumber > maxDice[diceColour]:
                    gameLessThanMaxDiceAllow = False
        if gameLessThanMaxDiceAllow:
            countGameLowerThanMax += gameId
    
    print( countGameLowerThanMax)

