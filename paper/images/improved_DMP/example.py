import numpy as np
import matplotlib.pylab as plt
from dmp import DMPs_discrete, ImprovedFormulation

x = np.linspace(0, np.pi/2, 200)
pose = np.sin(x)

goal = np.array([1.5])
dt = 1.0/pose.shape[0]
nbfs = 100

improvedDmp = DMPs_discrete(dims=1, bfs=nbfs, ts=ImprovedFormulation(),dt=dt)
improvedDmp.learn(y_des=pose.T)
improvedDmp.set_goal_state(goal)

improvedDmp_y, improvedDmp_dy, improvedDmp_ddy = improvedDmp.plan()

plt.figure(1)
plt.plot(pose, label='Actual')
plt.plot(improvedDmp_y, label='DMP')
plt.legend(loc='upper right')
plt.title('Trajectories')
plt.figure(2)
plt.plot(improvedDmp.w.T)
plt.title('DMP Weights')
plt.figure(3)
plt.plot(improvedDmp.f_desired)
plt.title('Desired Force')

plt.show()
