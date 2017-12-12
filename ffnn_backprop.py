import math
import random

# This module employs a feedforward neural network with back propagation to learn XOR
# After the network is trained, is is tested with inpt pairs ranging from 0 to 1

class Neuron:
    def __init__(self, name):
        self.name = name
        self.bias = 1
        self.biasWeight = random.choice((random.randint(-9, -1), random.randint(1,9)))/10
        self.inWeightA = random.choice((random.randint(-9, -1), random.randint(1,9)))/10
        self.inWeightB = random.choice((random.randint(-9, -1), random.randint(1,9)))/10
        self.outWeight = 0
        self.inA = 0
        self.inB = 0
        self.output = 0

    def displayWeights(self):
        print(self, "- inA: ", self.inWeightA, ", inB: ", self.inWeightB, ", out: ", self.outWeight, ", bias: ", self.biasWeight)

    def saveWeights(self):
        return [[self, ""],
                ["inA:", self.inWeightA],
                ["inB:", self.inWeightB],
                ["out:", self.outWeight],
                [",bias:",self.biasWeight]]

    def setInputs(self, valA, valB):
        self.inA = valA
        self.inB = valB

    def setOutput(self, output):
        self.output = output

    def calcBiasWeightAdj(self, error, learningRate):
        adj = learningRate * error * self.bias
        self.biasWeight += adj

    def calcNeuronWeightAdj(self, error, learningRate):
        adj = learningRate * error * self.output
        self.outWeight += adj

    def calcInputWeightAdj(self, error, learningRate):
        adjA = learningRate * error * self.inA
        adjB = learningRate * error * self.inB
        # print(self, "inA weight: ", self.inWeightA, "+ adj:", adjA)
        self.inWeightA += adjA
        # print(self, "new inA weight:", self.inWeightA)
        # print(self, "inB weight: ", self.inWeightB, "+ adj:", adjB)
        self.inWeightB += adjB
        # print(self, "new inB weight:", self.inWeightB)
        # print()

    def calcNet(self):
        net = (self.bias * self.biasWeight) + (self.inWeightA * self.inA) + (self.inWeightB * self.inB)
        return net

    def calcErrorOut(self, target):
        error = (target - self.output) * (self.output) * (1 - self.output)
        return error

    def calcErrorNeuron(self, out, target):
        error = (self.output) * (1 - self.output) * (self.outWeight * out.calcErrorOut(target))
        return error

    def setOutWeight(self, neuron0, neuron1):
        neuron0.outWeight = self.inWeightA
        neuron1.outWeight = self.inWeightB

    def __str__(self):
        return self.name

def transFunc(x):
    x *= -1
    val = 1 / (1 + math.e ** x)
    return val

def neuralNetwork():
    learningRate = 0.5
    networkError = .99
    outputCount = 0

    # create neurons and output node with bias and random weights
    h1 = Neuron("h1")
    h2 = Neuron("h2")
    out = Neuron("out")
    out.setOutWeight(h1, h2)

    h1initWeights = h1.saveWeights()
    h2initWeights = h2.saveWeights()
    outinitWeights = out.saveWeights()

    trainingSet = [[0.1, 0.1, 0.1],
                   [0.1, 0.9, 0.9],
                   [0.9, 0.1, 0.9],
                   [0.9, 0.9, 0.1]]

    while networkError > 0.001:
        totalOutDiff = 0
        # trainingSet = random.sample(trainingSet0, 4)
        for i in range(len(trainingSet)):

            #set patterns as inputs
            inA = trainingSet[i][0]
            inB = trainingSet[i][1]
            target = trainingSet[i][2]

            h1.setInputs(inA, inB)
            h2.setInputs(inA, inB)

            # calculate net of each hidden neuron layer
            h1Net = h1.calcNet()
            h2Net = h2.calcNet()

            # calculate neuron outputs and set as inputs to output node
            h1Trans = transFunc(h1Net)
            h1.setOutput(h1Trans)
            h2Trans = transFunc(h2Net)
            h2.setOutput(h2Trans)

            # calculate network output
            out.setInputs(h1Trans, h2Trans)
            outNet = out.calcNet()
            outTrans = transFunc(outNet)
            out.setOutput(outTrans)

            # calculate error signals
            outError = out.calcErrorOut(target)
            h1error = h1.calcErrorNeuron(out, target)
            h2error = h2.calcErrorNeuron(out, target)

            # bias weight adjustments
            h1.calcBiasWeightAdj(h1error, learningRate)
            h2.calcBiasWeightAdj(h2error, learningRate)
            out.calcBiasWeightAdj(outError, learningRate)

            # neuron -> in weight adjustments
            h1.calcInputWeightAdj(h1error, learningRate)
            h2.calcInputWeightAdj(h2error, learningRate)
            out.calcInputWeightAdj(outError, learningRate)

            print("\n""A = ", inA)
            print("B = ", inB)
            print("target: ", target)
            print("actual output: ", out.output)

            patternOutDiff = (target - out.output)**2
            totalOutDiff += patternOutDiff

        outputCount += 1

        # calculate network error
        tsse = 0.5 * totalOutDiff
        networkError = math.sqrt((2*tsse)/16)
        print("\ntsse: ", tsse)
        print("\nrmse: ", networkError)
        print("iterations: ", outputCount)
        print("\n#######################\n")

    h1finalWeights = h1.saveWeights()
    h2finalWeights = h2.saveWeights()
    outfinalWeights = out.saveWeights()

    testRange = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    testPairs = []
    for i in testRange:
        for j in testRange:
            h1.setInputs(i, j)
            h2.setInputs(i, j)

            # calculate net of each hidden neuron layer
            h1Net = h1.calcNet()
            h2Net = h2.calcNet()

            # calculate neuron outputs and set as inputs to output node
            h1Trans = transFunc(h1Net)
            h1.setOutput(h1Trans)
            h2Trans = transFunc(h2Net)
            h2.setOutput(h2Trans)

            # calculate network output
            out.setInputs(h1Trans, h2Trans)
            outNet = out.calcNet()
            ijOut = transFunc(outNet)
            print(ijOut, end="\t")
        print()

neuralNetwork()