import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve
import math
import numpy as np

from solvers.euler import *
from solvers.SVScheme import *

#user input
def askYNInput(message):
    userInput = input(message)
    while(userInput != 'y' and userInput != 'n'):
        userInput = input(message)
    if (userInput == 'y'):
        return True
    return False

drawEulerA = askYNInput("Draw with Euler A method ? [y/n]: ")
drawEulerB = askYNInput("Draw with Euler B method ? [y/n]: ")
drawSVAB = askYNInput("Draw with SV-AB method ? [y/n]: ")
drawSVBA = askYNInput("Draw with SV-BA method ? [y/n]: ")
drawEulerForward = askYNInput("Draw with EulerForward method ? [y/n]: ")

# Variable
t0 = 0
tf = 4
steps = 300
q0 = 0.9
p0 = 0

eps = 1

# Solving equation
if drawEulerA:
    solEulerA = solveEulerA(t0, tf, steps, q0, p0, eps)
    print("Euler A solved")
if drawEulerB:
    solEulerB = solveEulerB(t0, tf, steps, q0, p0, eps)
    print("Euler B solved")
if drawEulerForward:
    solEulerForward = solveEulerForward(t0, tf, steps, q0, p0, eps)
    print("Euler Forward solved")
if drawSVAB:
    solSVAB = solveSVAB(t0, tf, steps, q0, p0, eps)
    print("SV-AB solved")
if drawSVBA:
    solSVBA = solveSVBA(t0, tf, steps, q0, p0, eps)
    print("SV-BA solved")

# Plotting values
def plotpqtValues():
    f, ax = plt.subplots(2)

    if drawEulerA:
        ax[0].plot(solEulerA[0], solEulerA[1], label='Euler A method')
        ax[1].plot(solEulerA[0], solEulerA[2], label='Euler A method')

    if drawEulerB:
        ax[0].plot(solEulerB[0], solEulerB[1], label='Euler B method')
        ax[1].plot(solEulerB[0], solEulerB[2], label='Euler B method')
    if drawSVAB: 
        ax[0].plot(solSVAB[0], solSVAB[1], label='SV-AB method')
        ax[1].plot(solSVAB[0], solSVAB[2], label='SV-AB method')

    if drawSVBA:
        ax[0].plot(solSVBA[0], solSVBA[1], label='SV-BA method')
        ax[1].plot(solSVBA[0], solSVBA[2], label='SV-BA method')

    if drawEulerForward:
        ax[0].plot(solEulerForward[0], solEulerForward[1], label='Euler Forward method')
        ax[1].plot(solEulerForward[0], solEulerForward[2], label='Euler Forward method')

    ax[0].grid()
    ax[0].legend()
    ax[0].set_title("Variations of q")
    ax[0].set(xlabel='t', ylabel='q(t)')

    ax[1].grid()
    ax[1].legend()
    ax[1].set_title("Variations of p")
    ax[1].set(xlabel='t', ylabel='p(t)')

    return
def getdqdp(solvedqp): # Get the derivatives for the phase portrait
    dq = []
    dp = []

    if (len(solvedqp[0]) != len(solvedqp[1]) or len(solvedqp[0]) != len(solvedqp[2])):
        raise ValueError('Arrays size do not match')

    for i in range(len(solvedqp[0])):
        pi = solvedqp[2][i]
        qi = solvedqp[1][i]

        dq.append(2*pi)
        dp.append(12*eps*(pow(qi, -13) - pow(qi, -7)))

    return [dq, dp]

def plotphasePortraits():
    f, ax = plt.subplots(2)

    if drawEulerA:
        solEulerA_Derivatives = getdqdp(solEulerA)
        ax[0].plot(solEulerA[1], solEulerA_Derivatives[0], label='Euler A method')
        ax[1].plot(solEulerA[2], solEulerA_Derivatives[1], label='Euler A method')

    if drawEulerB:
        solEulerB_Derivatives = getdqdp(solEulerB)
        ax[0].plot(solEulerB[1], solEulerB_Derivatives[0], label='Euler B method')
        ax[1].plot(solEulerB[2], solEulerB_Derivatives[1], label='Euler B method')
    
    if drawSVAB:
        solSVAB_Derivatives = getdqdp(solSVAB)
        ax[0].plot(solSVAB[1], solSVAB_Derivatives[0], label='SV-AB method')
        ax[1].plot(solSVAB[2], solSVAB_Derivatives[1], label='SV-AB method')

    if drawSVBA:
        solSVBA_Derivatives = getdqdp(solSVBA)
        ax[0].plot(solSVBA[1], solSVBA_Derivatives[0], label='SV-BA method')
        ax[1].plot(solSVBA[2], solSVBA_Derivatives[1], label='SV-BA method')

    if drawEulerForward:
        solEulerForward_Derivatives = getdqdp(solEulerForward)
        ax[0].plot(solEulerForward[1], solEulerForward_Derivatives[0], label='Euler Forward method')
        ax[1].plot(solEulerForward[2], solEulerForward_Derivatives[1], label='Euler Forward method')

    ax[0].grid()
    ax[0].legend()
    ax[0].set_title("Phase portrait of q")
    ax[0].set(xlabel='q', ylabel='dq')

    ax[1].grid()
    ax[1].legend()
    ax[1].set_title("Phase portrait of p")
    ax[1].set(xlabel='p', ylabel='dp')

    return

plotpqtValues()
plotphasePortraits()
plt.pause(0)