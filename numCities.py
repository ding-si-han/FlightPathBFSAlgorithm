import graph
import random
from itertools import chain
import time
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt
from random import randint


# ====== TEST FOR DIFFERENT NUMBER OF CITIES ==========
# Initialise Graph and Parameters
flightPath= graph.Graph()
samplingArray = []
resultArray = []
testMin = 2000
testMax = testMin * 5 + 1
testInterval = testMin
percentageCities = 0.01

# Loop through for the different number of cities
for i in range(testMin, testMax, testInterval):
    print("==================== Number of Cities: ", i, "====================")
    timeArray = []
    numTrials = 1000
    flightPath()   
    flightPath.generateGraph(i, percentageCities)
    # Loop through the number of trials (1000 used for stability)
    for j in range(numTrials):
        endpoint = randint(2,i)
        print("TRIAL", j+1, end=" ")
        start = time.time()
        flightPath.BFS('1', str(endpoint))
        end = time.time()
        print("   || TIME TAKEN FOR BFS:", end - start)
        timeArray.append(end- start)
    averageTime = sum(timeArray)/ numTrials
    print(">>>>> AVERAGE OF", numTrials, "TRIALS:", averageTime)
    samplingArray.append(i)
    resultArray.append(averageTime)
    print()

print("Number of Cities:", samplingArray)
print("Computation Time", resultArray)


plt.style.use('dark_background')

plt.plot(samplingArray,resultArray)
plt.xlabel("Number of cities")
plt.ylabel("Computation time (seconds)")
plt.title("Comparison of time with number of cities")
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(18.5, 10.5)
fig.savefig("./imgs/num_cities.png")


