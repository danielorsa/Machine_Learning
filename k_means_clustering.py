import random
import math
# This module employs k-means clustering to classify data into clusters

class Cluster:
    def __init__(self, initCenter, num):
        self.center = initCenter
        self.points = []
        self.clustNum = num
        self.oldCenter = None
        self.xPoints = []
        self.yPoints = []

    def findMean(self):
        xSum = 0
        ySum = 0
        count = len(self.points)
        for point in self.points:
            xSum += point[0]
            ySum += point[1]
        cx = xSum / count
        cy = ySum / count
        return [cx, cy]

    def updateMean(self):
        self.oldCenter = self.center
        self.center = self.findMean()

    def updateXY(self):
        self.xPoints = []
        self.yPoints = []
        for point in self.points:
            self.xPoints.append(point[0])
            self.yPoints.append(point[1])

    def addPoint(self, point):
        self.points.append(point)

    def clearPoints(self):
        self.points = []

    def displayCluster(self):
        for i in range(len(self.points)):
            for j in range(2):
                print(self.points[i][j], "\t", end="")
            print("")

    def __str__(self):
        return "cluster-{0}({1}): center: {2}-->{3}".format(self.clustNum, len(self.points), self.oldCenter, self.center)

def distForm(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    xDiff = (x2-x1)**2
    yDiff = (y2-y1)**2
    return math.sqrt(xDiff + yDiff)

def initCenters(k):
    clusterCenters = []
    for i in range(k):
        randomX = random.random()
        randomY = random.random()
        cluster = Cluster([randomX, randomY], i)
        clusterCenters.append(cluster)
    return clusterCenters

def assignDataToCluster(dataList, clusters, k):
    for clust in clusters:
        clust.clearPoints()
    for point in dataList:
        shortest = distForm(point, clusters[0].center)
        clusterIdx = 0
        for i in range(1, len(clusters)):
            dist = distForm(point, clusters[i].center)
            if dist < shortest:
                shortest = dist
                clusterIdx = i
        clusters[clusterIdx].addPoint(point)
    for clust in clusters:
        clust.updateXY()

def updateAgain(clusters, k):
    again = False
    for clust in clusters:
        xDiff = clust.oldCenter[0] - clust.center[0]
        yDiff = clust.oldCenter[1] - clust.center[1]
        if xDiff != 0 or yDiff != 0:
            again = True
    return again

def run_kmeans(initData, k):
    clusters = initCenters(k)
    running = True
    iterationCount = 0
    while running:
        print("\n##### iteration: {0} #####".format(iterationCount))
        assignDataToCluster(initData, clusters, k)
        for clust in clusters:
            print(clust)
            clust.displayCluster()
        for clust in clusters:
            clust.updateMean()
        if updateAgain(clusters, k):
            iterationCount += 1
        else:
            running = False
    print("\n#### done #####")
    print("final iteration center updates:")
    for clust in clusters:
        print(clust)
