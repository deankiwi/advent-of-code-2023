import re


def txtFileToArray(fileName):
    array = []
    print("<----- NEXT FILE ")
    with open(fileName) as file:
        for line in file:
            line = line.strip("\n")
            array.append(list(line))
            print(len(array[-1]))
    return array


def checkIfNumberIsToBeCounted(array, numDigitSize, xLoc, yLoc):
    dataYLen = len(array)
    dataXLen = len(array[0])
    addToTotal = False
    boxXStart = max(xLoc - 1 - numDigitSize, 0)
    boxXFinish = min(xLoc - 1 + 1, dataXLen)
    boxYStart = max(yLoc - 1, 0)
    boxYFinish = min(yLoc + 2, dataYLen)
    for boxY in range(boxYStart, boxYFinish):
        for boxX in range(boxXStart, boxXFinish + 1):
            if re.match(r"[^\d.]", array[boxY][boxX]):
                addToTotal = True
                break
        if addToTotal:
            break
    return addToTotal


# ignore


def gearRatios(dataAsArray):
    dataYLen = len(dataAsArray)
    dataXLen = len(dataAsArray[0])
    # digitLen used to track how digits are in the number
    numArray = []
    total = 0
    addToTotal = False

    for yLoc in range(dataYLen):
        # print(dataAsArray(yLoc))
        for xLoc in range(dataXLen):
            if re.match(r"[\d]", dataAsArray[yLoc][xLoc]) and xLoc < dataXLen - 1:
                numArray.append(dataAsArray[yLoc][xLoc])

            elif len(numArray) > 0 or re.match(r"[\d]", dataAsArray[yLoc][xLoc]):
                if re.match(r"[\d]", dataAsArray[yLoc][xLoc]):
                    numArray.append(dataAsArray[yLoc][xLoc])
                    # REMOVE
                    addToTotal = True

                # create box around number
                addToTotal = checkIfNumberIsToBeCounted(
                    dataAsArray, len(numArray), xLoc, yLoc
                )

                if not addToTotal:
                    numArray = []

                if addToTotal:
                    numToAdd = int("".join(numArray))
         
                    total += numToAdd
                    addToTotal = False

                    numArray = []

    return total
