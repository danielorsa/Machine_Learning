import random

# This module employs a Markov Chain to generate words from a given list of words

filename = 'some_file.txt'
inFile = open(filename, 'r')

wordList = []
for line in inFile:
    wordList.append(line)
for i in range(len(wordList) - 1):
    wordList[i] = wordList[i][:-1]


def markov():
    indexLookUp = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7,
                   "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17,
                   "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25, "#": 26}

    letterLookUp = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h",
                    8: "i", 9: "j", 10: "k", 11: "l", 12: "m", 13: "n", 14: "o", 15: "p", 16: "q", 17: "r",
                    18: "s", 19: "t", 20: "u", 21: "v", 22: "w", 23: "x", 24: "y", 25: "z", 26: "#"}

    letters1 = ["S", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    letters2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "E"]

    transitions = []
    for i in range(27):
        transitions.append([0] * 27)

    for word in wordList:
        transitions[0][indexLookUp[word[0]]] += 1
        for i in range(1, len(word)):
            transitions[indexLookUp[word[i - 1]] + 1][indexLookUp[word[i]]] += 1
        transitions[indexLookUp[word[-1]] + 1][26] += 1

    for i in range(len(transitions)):
        rowSum = 0
        for j in range(len(transitions[0])):
            rowSum += transitions[i][j]
        for k in range(len(transitions[0])):
            if rowSum > 0:
                transitions[i][k] = (transitions[i][k] / rowSum)

    randomChance = random.random()

    newWord = ""

    #### FIRST LETTER ####
    transChanceSum = 0
    i = 0
    while transChanceSum < randomChance:
        transChanceSum += transitions[0][i]
        i += 1
    startingLetter = letterLookUp[i - 1]
    newWord += startingLetter

    #### REST OF WORD ####
    while newWord[-1] != "#":
        lastLetter = newWord[-1]
        lastLetterIndexLookup = indexLookUp[lastLetter] + 1
        randomChance = random.random()
        transChanceSum = 0
        nextLetter = ""
        i = 0
        while len(nextLetter) < 1:
            transChanceSum += transitions[lastLetterIndexLookup][i]
            if transChanceSum < randomChance:
                i += 1
            else:
                nextLetter = letterLookUp[i]
                newWord += nextLetter
        print("new word: ", newWord)

    return newWord[:-1]
