import numpy as np
from matplotlib import pyplot as plt

# defining the vertices of the quadrilateral MIST
I = np.array([[-3.25], [0]])
S = np.array([[3.25], [0]])
M = np.array([[-4.15], [3.38]])

# angle made by vector ST with positive x-axis in radians
IST = np.pi / 3

# angle made by the vector MT with positive x-axis in radians
IMT = (7 * np.pi) / 9

# plotting the graph
x = np.linspace(-10, 10, 10000)
plt.plot(-3.25, 0, 'o', color='black')
plt.text(-3.25 + 0.25, 0 + 0.25, 'I')

plt.plot(3.25, 0, 'o', color='black')
plt.text(3.25 + 0.25, 0 + 0.25, 'S')

plt.plot(-4.15, 3.38, 'o', color='black')
plt.text(-4.15 + 0.25, 3.38 + 0.25, 'M')

plt.plot(np.array([-3.25, 3.25]), np.array([0, 0]), color='blue')
plt.plot(np.array([-4.15, -3.25]), np.array([3.38, 0]), color='green')
plt.plot(x, np.tan(IST) * (x - 3.25), color='red')
plt.plot(x, (np.tan(IMT) * (x + 4.15) + 3.38), color='yellow')
plt.xlim(-10, 10)
plt.ylim(-5, 10)
plt.show()
