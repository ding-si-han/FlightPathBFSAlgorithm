# TESTING FOR DIFFERENT NUMBER OF DIRECT FLIGHTS
import graph
import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt


flightPath= graph.Graph()

samplingArray = []
resultArray = []
testMin = 200
testMax = testMin * 5 + 1
testInterval = testMin
percentageCitiesArray = [0.02, 0.04, 0.06, 0.08, 0.1]
count = 0
testSamples = 2000

for i in range(5):
    percentageCities = percentageCitiesArray[i]

    print("====== TEST CASE:", i + 1, " - Number of Direct Flights", percentageCities * testSamples ,"========")
    timeArray = []
    numTrials = 10
    for j in range(numTrials):
        flightPath()   
        flightPath.generateGraph(testSamples, percentageCities)
        print("TRIAL", j+1, end=" ")
        start = time.time()
        flightPath.BFS('1', str(testSamples))
        end = time.time()
        print("   || TIME TAKEN FOR BFS:", end - start)
        timeArray.append(end- start)
    
    averageTime = sum(timeArray)/ numTrials
    print(">>>>> AVERAGE OF 10 TRIALS:", averageTime)

    samplingArray.append(percentageCities * testSamples)
    resultArray.append(averageTime)
    print()

print("Number of Direct Flights:", samplingArray)
print("Computation Time", resultArray)
