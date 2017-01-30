import numpy as np
import matplotlib.pylab as plt
from dmp import DMPs_discrete, TdwFormulation, OriginalFormulation, ImprovedFormulation

x = np.linspace(0, np.pi/2, 200)
poses = np.sin(x)

goal = np.array([1.5])
dt = 1.0/poses.shape[0]
nbfs = 100

tdwFormulationDmp = DMPs_discrete(dims=1, bfs=nbfs, ts=TdwFormulation(), dt=dt)
tdwFormulationDmp.learn(y_des=poses.T)
tdwFormulationDmp.set_goal_state(goal)

originalFormulationDmp = DMPs_discrete(dims=1, bfs=nbfs, ts=OriginalFormulation(), dt=dt)
originalFormulationDmp.learn(y_des=poses.T)
originalFormulationDmp.set_goal_state(goal)

improvedFormulationDmp = DMPs_discrete(dims=1, bfs=nbfs, ts=ImprovedFormulation(),dt=dt)
improvedFormulationDmp.learn(y_des=poses.T)
improvedFormulationDmp.set_goal_state(goal)

tdwFormulationDmp_y, tdwFormulationDmp_dy, tdwFormulationDmp_ddy = tdwFormulationDmp.plan()
originalFormulationDmp_y, originalFormulationDmp_dy, originalFormulationDmp_ddy = originalFormulationDmp.plan()
improvedFormulationDmp_y, improvedFormulationDmp_dy, improvedFormulationDmp_ddy = improvedFormulationDmp.plan()

plt.figure(1)
plt.plot(poses, label='Actual Trajectory')
plt.plot(tdwFormulationDmp_y, '--', label='DMP [Tdw Formulation]')
plt.plot(originalFormulationDmp_y, label='DMP [Original Formulation]')
plt.plot(improvedFormulationDmp_y, label='DMP [Improved Formulation]')
plt.legend(loc='upper left')
plt.grid(True)
plt.title('Comparison between various DMP Formulations (DMP.goal=%.1f)' % goal[0])
plt.show()
