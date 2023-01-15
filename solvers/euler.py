from sympy import symbols, Eq, solve
import math
import numpy as np

def solveEulerA(t0, tf , steps , q0, p0, eps):
    dt = (tf - t0)/steps

    tList = [t0]
    qList = [q0]
    pList = [p0]

    for i in range(steps):
        qi = qList[i]
        pi = pList[i]

        # Solving the implicit equation
        # qk1 = symbols('qk1')
        # eq1 = Eq(qk1 - qi - dt * 2 * pi, 0)
        # eq1Sol = solve(eq1)
        
        # Setting the values
        ti1 = tList[i] + dt
        #qi1 = eq1Sol[0]
        qi1 = qi + dt * 2 * pi
        pi1 = pi - dt * (-12 * eps * (pow(qi1, -13) - pow(qi1, -7)))

        tList.append(ti1)
        qList.append(qi1)
        pList.append(pi1)

    return [tList, qList, pList]

def solveEulerB(t0, tf , steps , q0, p0, eps):
    dt = (tf - t0)/steps

    tList = [t0]
    qList = [q0]
    pList = [p0]

    for i in range(steps):
        qi = qList[i]
        pi = pList[i]

        # Solving the implicit equation
        # pk1 = symbols('pk1')
        # eq1 = Eq(pk1 - pi + dt * (- 12 * eps * (pow(qi, -13) - pow(qi, -7))), 0)
        # eq1Sol = solve(eq1)
        
        # Setting the values
        ti1 = tList[i] + dt
        #pi1 = eq1Sol[0]
        pi1 = + pi - dt * (- 12 * eps * (pow(qi, -13) - pow(qi, -7)))
        qi1 = qi + dt * 2 * pi1

        tList.append(ti1)
        qList.append(qi1)
        pList.append(pi1)

    return [tList, qList, pList]

def solveEulerForward(t0, tf , steps , q0, p0, eps):
    dt = (tf - t0)/steps

    tList = [t0]
    qList = [q0]
    pList = [p0]

    for i in range(steps):
        qi = qList[i]
        pi = pList[i]

        # Setting the values
        ti1 = tList[i] + dt

        qi1 = qi + dt * 2 * pi
        pi1 = pi + dt * 12 * eps * (pow(qi, -13) - pow(qi, -7))

        tList.append(ti1)
        qList.append(qi1)
        pList.append(pi1)
    
    return [tList, qList, pList]