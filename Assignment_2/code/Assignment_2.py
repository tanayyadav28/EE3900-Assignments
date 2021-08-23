import numpy as np

# defining the matrices

A = np.array([[1, 0], [0, -1]])
B = np.array([[0, 1], [1, 0]])

# multiplying the matrices

AB = A @ B
BA = B @ A

print('AB =\n', AB, '\nBA =\n', BA)

# subtracting P and Q to check whether Z is 0

Z = AB - BA

# condition to check if Z is 0 matrix

result = np.all(Z == 0)
print('\nResult')
if result:
    print('AB = BA')
else:
    print('AB != BA')
