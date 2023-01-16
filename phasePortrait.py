import matplotlib.pyplot as plt
import math
import numpy as np

def getLevelCurve(qList, E, eps):
    qListFiltered = [[]]
    pList = [[[]], [[]]]
    for q in qList:

        if (q==0):
            continue
        
        qm6 = pow(q, -6)
        p2 = E - eps * ( qm6 * qm6 - 2 * qm6)

        if ( p2 < 0 ):
            if (len(qListFiltered[-1]) !=0):
                qListFiltered.append([])
                pList[0].append([])
                pList[1].append([])
                
            continue
        
        qListFiltered[-1].append(q)
        pList[0][-1].append(math.sqrt(p2))
        pList[1][-1].append(-math.sqrt(p2))
    return [qListFiltered, pList]

def drawPhasePortrait(qList, EList, eps):
    f, ax = plt.subplots(1)
    for E in EList:
        Htuples = getLevelCurve(q, E, eps)
        for i in range(len(Htuples[0])):
            ax.plot(Htuples[0][i], Htuples[1][0][i], 'c')
            ax.plot(Htuples[0][i], Htuples[1][1][i], 'c')
    ax.grid()
    ax.set_xlabel('q', fontsize = 18.0)
    ax.set_ylabel('p', fontsize = 18.0)

# Setting up parameters
qmin = -3
qmax = 3

Emin = -.1
Emax = .1

curveNumber = 10

qStep = 0.001
eps = 1

# Computing values
q = list(np.arange(qmin, qmax, qStep))
E = np.linspace(Emin, Emax, curveNumber)

drawPhasePortrait(q, E, eps)

plt.pause(0)