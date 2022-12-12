
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
 
fig, ax = plt.subplots()
x = range(30) 
y = [0] * 30
 
bars = ax.bar(x, y, color="blue")
ax.axis([0, 30, 0, 10])
 
def update(i):
    y[i] = np.random.randint(0, 10)
    bars[i].set_height(y[i])

title = ax.text(0.5,0.85, "", bbox={'facecolor':'w', 'alpha':0.5, 'pad':5},transform=ax.transAxes, ha="center")

anim = FuncAnimation(fig, update, frames = 30, interval=100)
anim.save('myanimation.gif') 
plt.show()