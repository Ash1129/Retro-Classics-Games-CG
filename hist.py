# import numpy as np
# from matplotlib import pyplot as plt

# img = [[25, 100, 150, 75, 0, 75, 75, 50, 100, 75],
#          [75, 75, 100, 50, 50, 125, 100, 100, 75, 50],
#          [125, 150, 75, 100, 125, 175, 25, 250, 150, 100],
#          [250, 175, 125, 125, 75, 50, 175, 225, 175, 125],
#          [225, 250, 150, 175, 50, 200, 200, 175, 250, 175],
#          [200, 200, 75, 200, 150, 250, 225, 100, 200, 200],
#          [175, 125, 250, 225, 250, 225, 250, 75, 125, 225],
#          [125, 100, 200, 250, 25, 200, 225, 50, 100, 250],
#          [150, 75, 225, 25, 50, 175, 200, 75, 75, 25],
#          [100, 25, 125, 0, 0, 100, 175, 100, 25, 0],
#          ]
#


from math import *
import random
import numpy as np
vals = range(0, 250, 25)
img = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(random.choice(vals))
    img.append(row)
print(np.array(img))

import matplotlib.pyplot as plt

arr = np.array(img)
magnitude = np.zeros((8, 8), dtype = int)
angle = np.zeros((8, 8), dtype = int)
for j in range(1, 9):
    for i in range(1, 9):
        Gx = arr[j][i + 1] - arr[j][i - 1]
        Gy = arr[j + 1][i] - arr[j - 1][i]
        magnitude[j - 1][i - 1] = (Gx**2 + Gy**2)**0.5
        if Gx != 0:
            angle[j - 1][i - 1] = 180 * (atan(Gy/Gx))/np.pi
        else:
            if Gy > 0:
                angle[j - 1][i - 1] = 90
            elif Gy < 0:
                angle[j - 1][i - 1] = -90

array = np.zeros((19), dtype = int)
for i in range(len(angle.flatten())):
    array[(90 + angle.flatten()[i])//10] += magnitude.flatten()[i]
print(magnitude)
print(angle)
print(array)
plt.plot(array)
plt.show()