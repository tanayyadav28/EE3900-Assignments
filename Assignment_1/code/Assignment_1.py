import numpy as np
from matplotlib import pyplot as plt

# from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

A = np.array([2, 2, -5])
B = np.array([2, 1, 3])

# given expression
C = A + B

# printing the vector C
print('A + B =', C)

# finding the norm of the vector C
norm_C = np.linalg.norm(C)

# calculation of unit vector
H = C / norm_C

# printing the unit vector
print('The unit vector H in the direction of vector C is:', H)

# plotting the vectors
ax.scatter(A[0], A[1], A[2], 'o', color='blue')
ax.scatter(B[0], B[1], B[2], 'o', color='red')
ax.scatter(C[0], C[1], C[2], 'o', color='green')
ax.scatter(H[0], H[1], H[2], 'o', color='yellow')
ax.scatter(0, 0, 0, 'o', color='black')
ax.text(2 * 1.05, 2 * 1.05, -5 * 1.05, 'A')
ax.text(2 * 1.05, 1 * 1.05, 3 * 1.05, 'B')
ax.text(4 * 1.05, 3 * 1.05, -2 * 1.05, 'C')
ax.text(H[0] * 1.05, H[1] * 1.05, H[2] * 1.05, 'H')
ax.text(0 + 0.05, 0 + 0.05, 0 + 0.05, 'O',)
plt.plot(np.array([0, 2]), np.array([0, 2]), np.array([0, -5]), 'b', label="$A$")
plt.plot(np.array([0, 2]), np.array([0, 1]), np.array([0, 3]), 'r', label="$B$")
plt.plot(np.array([0, 4]), np.array([0, 3]), np.array([0, -2]), 'g', label="$C$")
plt.plot(np.array([0, H[0]]), np.array([0, H[1]]), np.array([0, H[2]]), 'y', label="$H$")
plt.grid()
plt.legend()
plt.show()
