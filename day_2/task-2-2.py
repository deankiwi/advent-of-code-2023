filename = r"data-2-1.txt"


with open(filename) as file:
    # power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together
    countGamePower = 0

    for line in file:
        minDice = {"red": 0, "green": 0, "blue": 0}
        # print(line)
        line = line.strip("\n")
        gameId = int(line.split(":")[0].split(" ")[1])
        games = line.split(":")[1].split(";")
        gameLessThanMaxDiceAllow = True
        for game in games:
            for dice in game.split(","):
                diceNumber = int(dice.split(" ")[1])
                diceColour = dice.split(" ")[-1]
                # print(diceColour, diceNumber)
                if diceNumber > minDice[diceColour]:
                    minDice[diceColour] = diceNumber
        countGamePower += minDice["red"] * minDice["green"] * minDice["blue"]

print(f"Power for game --> {countGamePower}")
