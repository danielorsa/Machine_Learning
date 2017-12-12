from matrixOps import *

# This module employs bayes classification to validate points in two classes of data


def createClassMats(class1data, class2data):
    classMatrices = []

    class1 = Matrix()
    class1.intakeFromList(class1data)
    class1.setClassNum(1)
    classMatrices.append(class1)

    class2 = Matrix()
    class2.intakeFromList(class2data)
    class2.setClassNum(2)
    classMatrices.append(class2)

    return classMatrices, class1, class2


def classifyByDiscrim(classMatrix, classNum, class1, class2):
    shouldBe_class1 = []
    shouldBe_class2 = []
    for i in range(len(classMatrix.matrix)):
        vector = Matrix()
        v = []
        for j in range(2):
            v.append([classMatrix.matrix[i][j]])
        vector.intakeFromList(v)
        c1disc = discriminant(vector, class1)
        c2disc = discriminant(vector, class2)
        if c2disc > c1disc:
            shouldBe_class2.append(vector)
        elif c1disc > c2disc:
            shouldBe_class1.append(vector)

    print("\nclass {0} - should be class 1 ({1} points):".format(classNum, len(shouldBe_class1)))
    for point in shouldBe_class1:
        for i in range(2):
            print(point.matrix[i][0], "\t", end="")
        print("")

    print("\nclass {0} - should be class 2 ({1} points):".format(classNum, len(shouldBe_class2)))
    for point in shouldBe_class2:
        for i in range(2):
            print(point.matrix[i][0], "\t", end="")
        print("")


def findContourLine(class1, class2, x1, x2, y1, y2):
    epsilon = .2
    step = .1
    contourPoints = []
    xRange = []
    for i in range(x1, x2):
        xRange.append(i)
        xRange.append(i + .1)
        xRange.append(i + .2)
        xRange.append(i + .3)
        xRange.append(i + .4)
        xRange.append(i + .5)
        xRange.append(i + .6)
        xRange.append(i + .7)
        xRange.append(i + .8)
        xRange.append(i + .9)
    yRange = []
    for i in range(y1, y2):
        yRange.append(i)
        yRange.append(i + .1)
        yRange.append(i + .2)
        yRange.append(i + .3)
        yRange.append(i + .4)
        yRange.append(i + .5)
        yRange.append(i + .6)
        yRange.append(i + .7)
        yRange.append(i + .8)
        yRange.append(i + .9)

    for x in xRange:
        for y in yRange:
            vector = Matrix()
            vector.intakeFromList([[x],
                                   [y]])
            discClass1 = discriminant(vector, class1)
            discClass2 = discriminant(vector, class2)
            if abs(discClass1 - discClass2) < epsilon:
                contourPoints.append(vector)

    print("\nBoundary Contour:")
    print("Classes: {0} and {1}".format(class1.classNum, class2.classNum))
    print("Epsilon:", epsilon)
    print("Domain Used: [{0}, {1}] // Step: {2}".format(x1, x2, step))
    print("Range Used: [{0}, {1}] // Step: {2}".format(y1, y2, step))
    print("Points:")
    for i in contourPoints:
        print("{0}\t{1}".format(i.matrix[0][0], i.matrix[1][0]))


def run_bayes(class1data, class2data, x1, x2, y1, y2):
    classMatrices, class1, class2 = createClassMats(class1data, class2data)
    for i in range(2):
        print("##### Class {0} Classification #####".format(i))
        classifyByDiscrim(classMatrices[i], (i+1), class1, class2)
        print("")

    print("##### Class 1/2 Contour ####")
    findContourLine(class1, class2, x1, x2, y1, y2)
