import numpy as np
import matplotlib.pyplot as plt

#-- Generate Data -----------------------------------------
# Using linspace so that the endpoint of 360 is included...
azimuths = np.radians(np.linspace(90, 30, 20))
zeniths = np.arange(0, 70, 10)

r, theta = np.meshgrid(zeniths, azimuths)
values = np.random.random((azimuths.size, zeniths.size))

#-- Plot... ------------------------------------------------
fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
ax.contourf(theta, r, values)

plt.show()

# import matplotlib.pyplot as plt
# from math import sin, cos, pi
# import math

# theta = 89
# l1 = 5
# l2 = 5

# x = [0, 0]
# y = [0, l1]

# plt.plot(x, y)

# plt.xlim([-10, 10])
# plt.ylim([-10, 10])

# x1 = [0,l2*cos(theta)]
# y1 = [0,l2*sin(theta)]

# plt.plot(x1, y1)

# plt.show()