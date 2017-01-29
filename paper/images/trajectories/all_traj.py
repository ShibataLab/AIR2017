# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# define index for plotting
time=0
poselinear_left_x=1;   poselinear_left_y=2;  poselinear_left_z=3
poselinear_right_x=8; poselinear_right_y=9; poselinear_right_z=10

# load csv tarjectories
org_tra = np.loadtxt('org_traj.csv', delimiter=',', skiprows=1)
org_dmp = np.loadtxt('org_dmp.csv', delimiter=',', skiprows=1)
mod_dmp = np.loadtxt('mod_dmp.csv', delimiter=',', skiprows=1)

org_tra = org_tra[:, range(15)]
org_dmp = org_dmp[:, range(15)]
mod_dmp = mod_dmp[:, range(15)]

#mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot( org_tra[:, poselinear_left_x], 
         org_tra[:, poselinear_left_y], 
         org_tra[:, poselinear_left_z], label='Original', c='b', lw=1)
ax.plot( org_dmp[:, poselinear_left_x], 
         org_dmp[:, poselinear_left_y], 
         org_dmp[:, poselinear_left_z], label='DMP', c='g')
ax.plot( mod_dmp[:, poselinear_left_x], 
         mod_dmp[:, poselinear_left_y], 
         mod_dmp[:, poselinear_left_z], label='Modified DMP', c='r')

#ax.set_title('Left Arm Trajectory', y=1.1)
ax.set_xlabel('x $(m)$')
ax.set_ylabel('y $(m)$')
ax.set_zlabel('z $(m)$')
ax.legend(loc='upper right')
plt.savefig("all_traj.pdf", bbox_inches='tight')
plt.show()
