import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import random
from rk4 import *
from kuramoto import *
from KaskadenAusfall import *

# numerical parameter 
h = 0.001

# model parameters

positions = np.load('./networks/spainPos.npy')
A = np.load('./networks/spainAdj.npy')

N = A.shape[0]

Nt = 1000

plt.ion()


K = 50*A



# Einzelner Ausfall bei festgelegter Zeit
List = AdjAnalyse(A)


Kneu = np.zeros(K.shape)
Aneu = np.zeros(K.shape)

Aneu = A*1
Kneu = K*1

#Variation der Kopplungsgerade
#for i in range(K.shape[0]):
#    for k in range(K.shape[0]):
#        if (K[i][k] != 0):
#           K[i][k] = random.randint(30, 70)

#Entfernen
#Aneu[51][39] = 3.
#Aneu[39][51] = 3.
#Kneu[51][39] = 0.
#Kneu[39][51] = 0.

Aneu[83][91] = 3.
Aneu[91][83] = 3.
Kneu[83][91] = 0.
Kneu[91][83] = 0.

#Aneu[90][95] = 3.
#Aneu[95][90] = 3.
#Kneu[90][95] = 0.
#Kneu[95][90] = 0.

#Hinzufügen
#Aneu[59][97] = 2.
#Aneu[97][59] = 2.
#Kneu[59][97] = 50.
#Kneu[97][59] = 50.



A = Aneu*1
K = Kneu*1


np.random.seed(1237356)
#seed(1237356) nutzen, Synchronisation tritt auf
#bei anderen Seeds ohne Kappen schneller

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
        
        #Mein Shit zum plotten und speichern
        v = 60000+i
        fig.savefig("video"+str(v)+".png")
    
       
        plt.pause(0.0001)
