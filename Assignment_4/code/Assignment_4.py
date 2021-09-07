import matplotlib.pyplot as plt
import numpy as np

def line_dir_pt(m,A,k1,k2):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB
#creating x,y for 3D plotting
xx, yy = np.meshgrid(range(10), range(10))
#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')



#Plane points
A1 = np.array([1,2,3])
A2 = np.array([4,5,6])
m1 =np.array([1,-3,2])
m2 =np.array([2,3,1])
k1 = -4
k2=4
x2_dist_skew = line_dir_pt(m2,A2,k1,k2)
x1_dist_skew = line_dir_pt(m1,A1,k1,k2)

#Plotting all lines
plt.plot(x1_dist_skew[0,:],x1_dist_skew[1,:], x1_dist_skew[2,:],label='$L_1$')
plt.plot(x2_dist_skew[0,:],x2_dist_skew[1,:], x2_dist_skew[2,:], label='$L_2$')
#plotting points
ax.scatter(A1[0],A1[1],A1[2],'o')
ax.scatter(A2[0],A2[1],A2[2],'o')
ax.text(1.25,2.25,3.25, "A1", color='red')
ax.text(4.5,5.5,6.5, "A2", color='green')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.show()