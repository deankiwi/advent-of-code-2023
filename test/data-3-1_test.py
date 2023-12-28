import day_3.task_3_1 as task3
import pytest


@pytest.mark.skip()
def test_checkIfNumberIsToBeCounted_centre_true():
    inputArray = [
        [".", ".", "."],
        [".", "7", "."],
        [".", ".", "x"],
    ]
    numDigitSize = 1
    xLoc = 2
    yLoc = 1
    output = task3.checkIfNumberIsToBeCounted(inputArray, numDigitSize, xLoc, yLoc)

    assert output == True


@pytest.mark.skip()
def test_checkIfNumberIsToBeCounted_middleRight_true():
    inputArray = [
        [".", ".", "."],
        [".", ".", "7"],
        [".", ".", "x"],
    ]
    numDigitSize = 1
    xLoc = 2
    yLoc = 1
    output = task3.checkIfNumberIsToBeCounted(inputArray, numDigitSize, xLoc, yLoc)

    assert output == True


@pytest.mark.skip()
def test_checkIfNumberIsToBeCounted_bottom_right_true():
    inputArray = [
        [".", ".", "."],
        [".", ".", "x"],
        [".", ".", "7"],
    ]
    numDigitSize = 1
    xLoc = 2
    yLoc = 2
    output = task3.checkIfNumberIsToBeCounted(inputArray, numDigitSize, xLoc, yLoc)

    assert output == True


@pytest.mark.skip()
def test_gearRatios_bottom_right():
    inputArray = [
        [".", ".", "."],
        [".", ".", "x"],
        [".", ".", "7"],
    ]
    expectedTotal = 7
    output = task3.gearRatios(inputArray)

    assert output == expectedTotal


@pytest.mark.skip()
def test_gearRatios_middle_right():
    inputArray = [
        [".", ".", "."],
        [".", ".", "7"],
        [".", ".", "x"],
    ]
    expectedTotal = 7
    output = task3.gearRatios(inputArray)

    assert output == expectedTotal


def test_gearRatios_middle_right():
    inputArray = [
        [".", ".", "."],
        [".", "7", "7"],
        [".", ".", "x"],
    ]
    expectedTotal = 77
    output = task3.gearRatios(inputArray)

    assert output == expectedTotal


def test_gearRatios_provided_data():
    inputArray = task3.txtFileToArray(
        r"/Users/deanwelchmain/Documents/Programming/advent-of-code-2023/test/testdata-3.txt"
    )
    expectedTotal = 4361
    output = task3.gearRatios(inputArray)

    assert output == expectedTotal


def test_gearRatios_middleRight():
    inputArray = task3.txtFileToArray(
        r"/Users/deanwelchmain/Documents/Programming/advent-of-code-2023/test/testData1.txt"
    )
    expectedTotal = 111
    output = task3.gearRatios(inputArray)

    assert output == expectedTotal


def test_gearRatios_BottomRight():
    inputArray = task3.txtFileToArray(
        r"/Users/deanwelchmain/Documents/Programming/advent-of-code-2023/test/testData2.txt"
    )
    expectedTotal = 123
    output = task3.gearRatios(inputArray)

    assert output == expectedTotal


def test_gearRatios_provided_data():
    inputArray = task3.txtFileToArray(
        r"/Users/deanwelchmain/Documents/Programming/advent-of-code-2023/day_3/data-3.txt"
    )
    expectedTotal = 551094
    output = task3.gearRatios(inputArray)
    assert output == expectedTotal

    # assert output == expectedTotal
