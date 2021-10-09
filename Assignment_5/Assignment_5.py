import numpy as np
from matplotlib import pyplot as plt

len = 1000
x_axis = np.array([0]*len)

# standard parabola
X = np.linspace(-10, 10, len)
y = np.power(X, 2)

Y = np.vstack((X, y))

# parameters of the given parabola
V = np.array([[1, 0], [0, 0]])
u = np.array([0.5, 0])
f = 1

# Affine transformation
g = -np.array([0, 1])
vcm = g - u
vcp = g + u
A = np.vstack((V, vcp.T))
b = np.append(vcm, -f)
c = np.linalg.lstsq(A, b, rcond=None)[0]
c = c.reshape(2, 1)

# Generating the parabola
x_par = Y + c

# plotting the parabola
plt.plot(x_par[0, :], x_par[1, :], label='$x^2 + x + 1$')

# Plotting all points
plt.plot(c[0], c[1], 'o', color='red')
plt.plot(X, x_axis, label='x axis', color='black')
plt.text(c[0] * (1 - 1.5), c[1] * (1 + 1), '$(-0.5 , 0.75)$')
plt.ylim(-2, 10)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
