import numpy as np
import matplotlib.pyplot as plt
from rk4 import *
from kuramoto import *
import matplotlib.gridspec as gridspec

# numerical parameter 
h = 0.001

# model parameters

positions = np.load('./networks/northernPos.npy')
A = np.load('./networks/northernAdj.npy')

N = A.shape[0]

Nt = 50

plt.ion()


K = 50*A

#np.random.seed(1234351)

omegas = np.random.normal(loc=0.2, scale=0.01, size=N)
thetas = np.random.uniform(0, 2.*np.pi, size=N)

xs = [thetas]
ts = [0]
r, psi = order_parameter(thetas)
rs = [r]

fig = plt.figure(figsize=(14, 8))
gs = gridspec.GridSpec(nrows=2, ncols=2,  height_ratios=[4,1])
ax_map = fig.add_subplot(gs[:, 0])
ax_circle = fig.add_subplot(gs[0, 1])
ax_synchro = fig.add_subplot(gs[1, 1])

update = 10

ax_map = plot_network(ax_map, positions, A, thetas)
circlex = np.linspace(0, 2*np.pi, 256)

for i in range(Nt):
    thetas = rk4_step(kuramoto, thetas, [omegas, K], h)
    xs += [thetas]
    ts += [ts[-1]+h]
    r, psi = order_parameter(thetas)
    rs += [r]
    x_node = np.cos(thetas)
    y_node = np.sin(thetas)
    x_r = r*np.cos(psi)
    y_r = r*np.sin(psi)
    
    if not i%update:
        # circle
        ax_circle.clear()
        ax_circle.plot(np.sin(circlex), np.cos(circlex), 'k-')
        ax_circle.scatter(x_node, y_node, c=thetas%(2*np.pi), cmap='hsv', vmin=0, vmax=2*np.pi)
        ax_circle.arrow(0., 0., x_r, y_r, head_width=0.05, color = 'k')
        ax_circle.set_xlim((-1.5, 1.5))
        ax_circle.set_ylim((-1.5, 1.5))
        ax_circle.set_aspect('equal')

        # order parameter
        ax_synchro.clear()
        ax_synchro.plot(ts, rs)
        ax_synchro.set_xlabel('Zeit')
        ax_synchro.set_ylabel('Synchronisation')
        
        # map
        ax_map = plot_network(ax_map, positions, A, thetas)
       # v = i/10
       # plt.savefig("Plot" + str(v) + ".jpeg")
       # plt.close()
        plt.pause(0.0001)
