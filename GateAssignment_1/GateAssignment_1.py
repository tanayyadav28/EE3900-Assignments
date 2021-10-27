import numpy as np
from matplotlib import pyplot as plt

n, radii = 50, [0.33, 0.5]
pole1 = [0.33, 0]
pole2 = [0.5, 0]
zero = [0, 0]

theta = np.linspace(0, 2 * np.pi, n, endpoint=True)
xs = np.outer(radii, np.cos(theta))
ys = np.outer(radii, np.sin(theta))

# in order to have a closed area, the circles
# should be traversed in opposite directions
xs[1, :] = xs[1, ::-1]
ys[1, :] = ys[1, ::-1]

n, radii = 50, [0.5, 5]
theta = np.linspace(0, 2 * np.pi, n, endpoint=True)
xs1 = np.outer(radii, np.cos(theta))
ys1 = np.outer(radii, np.sin(theta))

# in order to have a closed area, the circles
# should be traversed in opposite directions
xs1[1, :] = xs1[1, ::-1]
ys1[1, :] = ys1[1, ::-1]
ax = plt.subplot(111, aspect='equal')
# ax.fill(np.ravel(xs), np.ravel(ys), color='green', edgecolor='#000000', label="$\\frac{1}{4}< |z|$\n ROC of H(z)")
ax.fill(np.ravel(xs1), np.ravel(ys1), edgecolor='#000000', label="$\\frac{1}{2} < |z|$\nROC of H(z)")
plt.plot(np.sin(theta), np.cos(theta), 'k-', label="Unit Circle: $|z| = 1$")
plt.plot([pole1[0], pole2[0]], [pole1[1], pole2[1]], 'rx', label="Poles of $H(z)$")
plt.plot(zero[0], zero[1], 'ro', label="Zeroes of $H(z)$")
plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.title("Pole-Zero Plot with ROC")
plt.grid(True)
plt.legend(loc='lower right')
plt.show()
