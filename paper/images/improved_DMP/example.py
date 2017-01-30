import numpy as np
import matplotlib.pylab as plt
from dmp import DMPs_discrete, ImprovedFormulation

x = np.linspace(0, np.pi/2, 200)
pose = np.sin(x)

goal = np.array([1.5])
dt = 1.0/pose.shape[0]
nbfs = 10

delta_t = 0.001

improvedDmp = DMPs_discrete(dims=1, bfs=nbfs, ts=ImprovedFormulation(),dt=dt)
improvedDmp.learn(y_des=pose.T)
improvedDmp.set_goal_state(goal)

improvedDmp_y, improvedDmp_dy, improvedDmp_ddy = improvedDmp.plan()

plt.figure(1)
x = np.array(range(improvedDmp.w.T.shape[0]))
pose = pose[::20]
improvedDmp_y = improvedDmp_y[::20]

plt.bar(x, improvedDmp.w.T)
plt.plot(x, pose, label='Actual')
plt.plot(x, improvedDmp_y, label='DMP')

plt.legend(loc='upper left')
plt.title('DMP Weights')

plt.show()
