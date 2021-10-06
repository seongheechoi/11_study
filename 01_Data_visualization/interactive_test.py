import matplotlib.pyplot as plt
import numpy as np

x_goal = 1
y_goal = 1
x = 1
y = 1
dt = 0.005
Kp = 7

def click(event):
    global x_goal, y_goal
    x_goal = event.xdata
    y_goal = event.ydata

fig = plt.figure()
fig.canvas.mpl_connect("button_press_event", click)

plt.ion()

while True:
    x = x + Kp * (x_goal - x) * dt
    y = y + Kp * (y_goal - y) * dt

    plt.cla()
    plt.plot(x_goal, y_goal, 'c+', markersize=15)
    plt.plot(x, y, 'g*')

    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    plt.show()
    plt.pause(dt)