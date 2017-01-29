import numpy as np
import matplotlib.pylab as plt
from dmp import DMPs_discrete, ImprovedFormulation

x = np.linspace(0, 2*np.pi, 500)
pose = np.sin(x)

goal = np.array([0.5])
dt = 1.0/pose.shape[0]
nbfs = 100

num_bfs = [10, 20, 50, 100, 500]

for ii, nbfs in enumerate(num_bfs):
    improvedDmp = DMPs_discrete(dims=1, bfs=nbfs, ts=ImprovedFormulation(),dt=dt)
    improvedDmp.learn(y_des=pose.T)
    improvedDmp.set_goal_state(goal)

    improvedDmp_y, improvedDmp_dy, improvedDmp_ddy = improvedDmp.plan()

    plt.figure(1)
    plt.plot(improvedDmp_y)

    plt.figure(2)
    plt.plot(improvedDmp.w.T)


plt.figure(1)
plt.plot(pose,lw=2)
plt.legend(['%i BFs' % i for i in num_bfs], loc='lower right')
plt.title('Actual Trajectory Vs DMP')

plt.figure(2)
plt.legend(['%i BFs' % i for i in num_bfs], loc='lower right')
plt.title('DMP Weights')

'''
plt.figure(3)
plt.plot(improvedDmp.f_desired, label='desired')
plt.plot(improvedDmp.f_predicted, label='predicted')
plt.legend(loc='upper right')
plt.title('Desired Force')

plt.figure(4)
plt.plot(improvedDmp_dy, label='vel')
plt.legend(loc='upper right')

plt.figure(5)
plt.plot(improvedDmp_ddy, label='acc')
plt.legend(loc='upper right')
'''
plt.show()
