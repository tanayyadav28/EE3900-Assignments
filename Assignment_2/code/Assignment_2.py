import numpy as np

# defining the matrices

A = np.array([[1, 0], [0, -1]])
B = np.array([[0, 1], [1, 0]])

# multiplying the matrices

P = np.dot(A, B)
Q = np.dot(B, A)

print('P = AB\nQ = BA')
print('P =\n', P, '\nQ =\n', Q)

# subtracting P and Q to check whether Z is 0

Z = P - Q

# condition to check if Z is 0 matrix

result = np.all(Z == 0)
print('Result')
if result:
    print('AB = BA')
else:
    print('AB != BA')
