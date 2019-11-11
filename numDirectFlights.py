# TESTING FOR DIFFERENT NUMBER OF DIRECT FLIGHTS
import graph
import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
from random import randint


# ====== TEST FOR DIFFERENT NUMBER OF DIRECT FLIGHTS ==========
# Initialise Graph and Parameters
flightPath= graph.Graph()
samplingArray = []
resultArray = []
testMin = 240
testMax = testMin * 5 + 1
testInterval = testMin
percentageCitiesArray = [0.15, 0.3, 0.45, 0.6, 0.75]
count = 0
testSamples = testMin * 5

# Loop through for the different number of direct flights
for i in range(5):
    percentageCities = percentageCitiesArray[i]

    print("====== TEST CASE:", i + 1, " - Number of Direct Flights", percentageCities * testSamples ,"========")
    timeArray = []
    numTrials = 1000
    flightPath()   
    flightPath.generateGraph(testSamples, percentageCities)
    # Loop through the number of trials (1000 used for stability)
    for j in range(numTrials):
        endpoint = randint(2, testSamples)
        print("TRIAL", j+1, end=" ")
        start = time.time()
        flightPath.BFS('1', str(endpoint))
        end = time.time()
        print("   || TIME TAKEN FOR BFS:", end - start)
        timeArray.append(end- start)
    averageTime = sum(timeArray)/ numTrials
    print(">>>>> AVERAGE OF", numTrials, "TRIALS:", averageTime)
    samplingArray.append(percentageCities * testSamples)
    resultArray.append(averageTime)
    print()

print("Number of Direct Flights:", samplingArray)
print("Computation Time", resultArray)

plt.style.use('dark_background')
plt.plot(samplingArray,resultArray)
plt.xlabel("Number of direct flights")
plt.ylabel("Computation time")
plt.title("Comparison of time with number of direct flights")
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig("./imgs/direct_flights.png")

