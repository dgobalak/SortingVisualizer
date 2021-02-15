import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import time
import sys

# ERROR: The last 2 bars might not get sorted

x_axis = [x for x in range(100)]
y_axis = [random.randint(-200, 200) for _ in range(100)]

c = count(start=-1)

def animate(i):
    plt.clf()
    a = next(c)
    bar = plt.bar(x_axis, y_axis,color="black", edgecolor="black")
    simple_sort(y_axis, a, bar)
    if a == len(y_axis) - 1:
        bar[a].set_color('black')
        bar[a].set_edgecolor('black')        
        time.sleep(5)
        sys.exit()

def simple_sort(y_axis, a, bar):
    bar[a].set_color('r')
    bar[a].set_edgecolor('r')
    min_val = 1000
    min_i = -1
    for i in range(a, len(y_axis)):
        # bar[i].set_color('r')
        if y_axis[i] < min_val:
            min_val = y_axis[i]
            min_i = i
    y_axis[min_i], y_axis[a] = y_axis[a], y_axis[min_i]
    bar[min_i].set_color('green')
    bar[min_i].set_edgecolor('green')

ani = FuncAnimation(plt.gcf(), animate, interval=0.1)
plt.show()