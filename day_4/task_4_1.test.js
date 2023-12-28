const task4 = require("./task_4_1");

describe("loadTxt()", () => {
  test("Return text contained in given file path", () => {
    fileName = "givenExampleData.txt";

    expect(task4.loadTxt(fileName)).toBe("Card 1: 41 | 41");
  });
});
