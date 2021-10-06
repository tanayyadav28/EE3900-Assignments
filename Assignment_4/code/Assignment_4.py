import matplotlib.pyplot as plt
import numpy as np


def line_dir_pt(m, A, k1, k2):
    len = 10
    dim = A.shape[0]
    x_AB = np.zeros((dim, len))
    lam_1 = np.linspace(k1, k2, len)
    for i in range(len):
        temp1 = A + lam_1[i] * m
        x_AB[:, i] = temp1.T
    return x_AB


# creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
# setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plane points
A1 = np.array([1, 2, 3]).T
A2 = np.array([4, 5, 6]).T
m1 = np.array([1, -3, 2]).T
m2 = np.array([2, 3, 1]).T
k1 = -4
k2 = 4
x2_dist_skew = line_dir_pt(m2, A2, k1, k2)
x1_dist_skew = line_dir_pt(m1, A1, k1, k2)

M = np.array([m1, m2]).T

M_T = M.T
temp = M_T @ (A1 - A2)
temp = temp.reshape(2, 1)
lambda_ = (np.linalg.inv(M_T @ M) @ temp).T

P = A1 - lambda_[0][0] * m1
Q = A2 + lambda_[0][1] * m2


# Plotting all lines
plt.plot(x1_dist_skew[0, :], x1_dist_skew[1, :], x1_dist_skew[2, :], label='$L_1$')
plt.plot(x2_dist_skew[0, :], x2_dist_skew[1, :], x2_dist_skew[2, :], label='$L_2$')
# plotting points
ax.scatter(A1[0], A1[1], A1[2], 'o')
ax.scatter(A2[0], A2[1], A2[2], 'o')
ax.scatter(P[0], P[1], P[2], 'o')
ax.scatter(Q[0], Q[1], Q[2], 'o')
ax.text(1.25, 2.25, 3.25, "A1", color='red')
ax.text(4.5, 5.5, 6.5, "A2", color='green')
ax.text(P[0] + 0.5, P[1] + 0.5, P[2] + 0.5, 'p1', color='blue')
ax.text(Q[0] + 0.5, Q[1] + 0.5, Q[2] + 0.5, 'p2', color='blue')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()
