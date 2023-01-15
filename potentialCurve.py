import matplotlib.pyplot as plt
import math
import numpy as np

q0 = 0.8
qf = 3
points = 200
eps = 1

qList = np.linspace(q0, qf, points)

VList = []
for q in qList:
    VList.append(eps * (pow(q, -12) - 2 * pow(q, -6)))

f, ax = plt.subplots(1)
ax.plot(qList, VList)

# Drawing Guidelines
ax.plot([q0, qf], [0, 0], 'k--')
ax.plot([pow(0.5, 1/6), pow(0.5, 1/6)], [min(VList), max(VList)], 'k--')
ax.set_xlabel('q', fontsize = 18.0)
ax.set_ylabel('V(q)', fontsize = 18.0)
ax.title.set_text('Potential function')

plt.show()