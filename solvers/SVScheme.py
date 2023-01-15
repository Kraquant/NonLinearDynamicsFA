from sympy import symbols, Eq, solve
import math
import numpy as np


def solveSVAB(t0, tf , steps , q0, p0, eps):
    dt = (tf - t0)/steps

    tList = [t0]
    qList = [q0]
    pList = [p0]

    for i in range(steps):
    
        qi = qList[i]
        pi = pList[i]

        # Solving the implicit equation
        # pk12 = symbols('pk12')
        # eq1 = Eq(pk12 - pi + dt/2 * ( - 12 * eps * (pow(qi, -13) - pow(qi, -7))), 0)
        # eq1Sol = solve(eq1)
        # pi12 = eq1Sol[0]
        pi12 = + pi - dt/2 * ( - 12 * eps * (pow(qi, -13) - pow(qi, -7)))

        # Setting the values
        ti1 = tList[i] + dt
        qi1 = qi + dt/2 * (2*pi12 + 2*pi12)
        pi1 = pi12 - dt/2 * (- 12 * eps * (pow(qi1, -13) - pow(qi1, -7)))

        tList.append(ti1)
        qList.append(qi1)
        pList.append(pi1)

    return [tList, qList, pList]

def solveSVBA(t0, tf , steps , q0, p0, eps):
    dt = (tf - t0)/steps

    tList = [t0]
    qList = [q0]
    pList = [p0]

    for i in range(steps):
        qi = qList[i]
        pi = pList[i]

        # Solving the implicit equation
        # qk12 = symbols('qk12')
        # eq1 = Eq(qk12 - qi - dt/2 * (2 * pi), 0)
        # eq1Sol = solve(eq1)
        # qi12 = eq1Sol[0]
        qi12 = qi + dt/2 * (2 * pi)

        # Setting the values
        ti1 = tList[i] + dt
        pi1 = pi - 2 * dt/2 * (- 12 * eps * (pow(qi12, -13) - pow(qi12, -7)))
        qi1 = qi12 + dt/2 * 2*pi1

        tList.append(ti1)
        qList.append(qi1)
        pList.append(pi1)

    return [tList, qList, pList]