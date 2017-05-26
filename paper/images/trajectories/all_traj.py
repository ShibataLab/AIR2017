# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
import matplotlib.ticker as ticker

class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
        FancyArrowPatch.__init__(self, (0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def draw(self, renderer):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, renderer.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        FancyArrowPatch.draw(self, renderer)

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
         org_tra[:, poselinear_left_z], label='Demonstration', c='b', lw=1)
ax.plot( org_dmp[:, poselinear_left_x], 
         org_dmp[:, poselinear_left_y], 
         org_dmp[:, poselinear_left_z], label='Initial DMP', c='g')
ax.plot( mod_dmp[:, poselinear_left_x], 
         mod_dmp[:, poselinear_left_y], 
         mod_dmp[:, poselinear_left_z], label='Modified DMP', c='r')

start_x=0.50; x_width=0.10
start_y=0.03; y_width=0.04
start_z=-0.1; z_width=0.10

a = Arrow3D([start_x-0.01, start_x + x_width], [start_y, start_y], [start_z, start_z], mutation_scale=15, lw=1, arrowstyle="->")
b = Arrow3D([start_x, start_x], [start_y-0.001, start_y + y_width], [start_z, start_z], mutation_scale=15, lw=1, arrowstyle="->")
c = Arrow3D([start_x, start_x], [start_y, start_y], [start_z-0.01, start_z + z_width], mutation_scale=15, lw=1, arrowstyle="->")

ax.text(start_x + x_width, start_y, start_z,'x')
ax.text(start_x, start_y + y_width, start_z,'y')
ax.text(start_x, start_y, start_z + z_width,'z')

ax.add_artist(a)
ax.add_artist(b)
ax.add_artist(c)

#ax.set_title('Left Arm Trajectory', y=1.1)
#ax.set_xlabel('x $(m)$')
#ax.set_ylabel('y $(m)$')
#ax.set_zlabel('z $(m)$')

ax.legend(loc='upper right')

#disable grid
ax.grid(False)

x_tick_spacing = 0.2
y_tick_spacing = 0.06
z_tick_spacing = 0.10
ax.xaxis.set_major_locator(ticker.MultipleLocator(x_tick_spacing))
ax.yaxis.set_major_locator(ticker.MultipleLocator(y_tick_spacing))
ax.zaxis.set_major_locator(ticker.MultipleLocator(z_tick_spacing))

# Get rid of the spines
# src: http://stackoverflow.com/a/29058250/1175065
ax.w_xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
ax.w_zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))

plt.savefig("all_traj.pdf", bbox_inches='tight')
plt.show()
