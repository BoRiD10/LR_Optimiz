import numpy as np
import random
import time
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go

data = np.load('Task9.npy')
# print(data)

def antWay(numIterat, numAnts, alfa, b, ro):
    phermony = np.ones((10, 10))
    WinPath = []
    WinLenght = 10000
    StartTime = time.process_time()
    # q0 = 0.3
    for n in range(0, numIterat):
        AllPath = []
        AllLenght = []
        for a in range(0, numAnts):
            cityes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            Way = []
            Punkt = 1
            LenghtWay = 0
            cityes.remove(Punkt)
            Way.append(Punkt)
            while len(cityes) != 0:
                # q = random.random()
                # if q < q0:
                #     NextPunkt = randNextPunkt(cityes, phermony, Punkt)
                # else:
                p = []
                for i in cityes:
                     p.append(pForNextPunkt(cityes, Punkt, phermony, data, i, alfa, b))
                NextPunkt = Roulette(cityes, p)
                LenghtWay += data[Punkt-1][NextPunkt-1]
                # AntColony(phermony, Punkt, NextPunkt, fi)
                Punkt = NextPunkt
                Way.append(Punkt)
                cityes.remove(Punkt)
                # for i in range(0, len(Way)):
                #     if i == len(Way) - 1: break
                #     addPheromony(phermony, Way[i], Way[i + 1], LenghtWay, ro)
            AllPath.append(Way)
            AllLenght.append(LenghtWay)
            if LenghtWay <= WinLenght:
                WinLenght = LenghtWay
                WinPath = Way
        for i in range(0, len(AllPath)):
            NWay = []
            NWay = AllPath[i]
            for j in range(0, len(NWay)):
                if j == len(NWay) - 1: break
                addPheromony(phermony, NWay[j], NWay[j + 1], AllLenght[i], ro)

        if WinLenght <=221: break
        # After finding the path, we change the pheromone matrix
        # for i in range(0, len(WinPath)):
        #     if i == len(WinPath) - 1: break
        #     addPheromony(phermony, WinPath[i], WinPath[i + 1], WinLenght, ro)
        # print(str(WinPath) + "  " + str(WinLenght))
        # print(phermony)
    EndTime = time.process_time()
    Time = EndTime - StartTime
    print("Way: " + str(WinPath))
    print("Way length: " + str(WinLenght))
    print("Time: " + str(Time))
    return Time


def pForNextPunkt(cityes, currentPunkt, phermony, data, NextPunkt, a, b):
    # a =
    # b = 1
    denominator = 0
    currentPunkt -= 1
    NextPunkt -= 1
    for i in cityes:
        denominator += (phermony[currentPunkt][i-1] ** a) / (data[currentPunkt][i-1] ** b)
    pForNextPunkt = (phermony[currentPunkt][NextPunkt] ** a) / (data[currentPunkt][NextPunkt] ** b) / denominator
    return pForNextPunkt


def Roulette(cities, P):
    randValue = random.random()
    summ = 0
    for i in P:
        summ += i
        if randValue < summ:
            IndexNextPoint = P.index(i)
            break
    nextPoint = cities[IndexNextPoint]
    return nextPoint


def addPheromony(pheromony, startPunkt, endPunkt, Lenght, ro):
    Q = 100
    pheromony[startPunkt - 1][endPunkt - 1] = ro * pheromony[startPunkt - 1][endPunkt - 1] + (Q / Lenght)


def AntColony(pheromony, startPunkt, endPunkt, fi):
    # fi = 0.5
    pheromony[startPunkt - 1][endPunkt - 1] = (1 - fi) * pheromony[startPunkt - 1][endPunkt - 1] + fi * 1


def randNextPunkt(cityes, phermony, Punkt):
    maxValue = 0
    for i in cityes:
        if phermony[Punkt-1][i-1] > maxValue:
            maxValue = phermony[Punkt-1][i-1]
            nextPunkt = i
    return nextPunkt

Ants = 10
antWay(100, Ants, 1, 1, 0.9)

#
# x = np.arange (0.1, 1, 0.1)
# y = []
# for i in x:
#     y.append(antWay(1000, 10, 1, 4, i))
#
#
# fig, ax = plt.subplots(figsize=(10, 5))
# ax.plot(x, y)
# ax.set_ylabel('Time, s')
# ax.set_xlabel('fi')
# plt.show()

#
# x = np.arange (0.5, 10.5, 0.5)
# y = np.arange (0.5, 10.5, 0.5)
# x2 = []
# y2 = []
# z = []
# n = 0
#
# for i in range (0, len(x)):
#     for j in range(0, len(y)):
#         z.append(antWay(100, 10, x[i], y[j], 0.9))
#         x2.append(x[i])
#         y2.append(y[j])
#         n += 1
#         print(n)
# print(z)
#
#
# fig1 = go.Scatter3d(x=x2,
#                     y=y2,
#                     z=z,
#                     marker=dict(opacity=0.9,
#                                 reversescale=True,
#                                 colorscale='Blues',
#                                 size=5),
#                     line=dict (width=0.02),
#                     mode='markers')
#
#
# mylayout = go.Layout(scene=dict(xaxis=dict( title="X"),
#                                 yaxis=dict( title="Y"),
#                                 zaxis=dict(title="Z")),)
#
#
# plotly.offline.plot({"data": [fig1],
#                      "layout": mylayout},
#                      auto_open=True,
#                      filename=("3DPlot.html"))