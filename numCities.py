import graph
import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

# TEST FOR DIFFERENT NUMBER OF CITIES
flightPath= graph.Graph()

samplingArray = []
resultArray = []
testMin = 200
testMax = testMin * 5 + 1
testInterval = testMin
percentageCities = 0.01

for i in range(testMin, testMax, testInterval):
     
    print("==================== Number of Cities: ", i, "====================")
    timeArray = []
    numTrials = 10
    for j in range(numTrials):
        flightPath()   
        flightPath.generateGraph(i, percentageCities)
        print("TRIAL", j+1, end=" ")
        start = time.time()
        flightPath.BFS('1', str(i))
        end = time.time()
        print("   || TIME TAKEN FOR BFS:", end - start)
        timeArray.append(end- start)
    
    averageTime = sum(timeArray)/ numTrials
    print(">>>>> AVERAGE OF 10 TRIALS:", averageTime)

    samplingArray.append(i)
    resultArray.append(averageTime)
    print()

print("Number of Cities:", samplingArray)
print("Computation Time", resultArray)




