import numpy as np
import lcapy as lc
from lcapy.discretetime import n

trans_func_x = np.array([1])
trans_func_y = np.array([1, -5/6, 1/6])

poles = np.roots(trans_func_y)

print('The poles are:',poles)