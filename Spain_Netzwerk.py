import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
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
Leitung0 = List[np.random.randint(0,List.shape[0])]
Leitung1 = List[np.random.randint(0,List.shape[0])]
Leitung2 = List[np.random.randint(0,List.shape[0])]
Leitung3 = List[np.random.randint(0,List.shape[0])]
Leitung4 = List[np.random.randint(0,List.shape[0])]
Leitung5 = List[np.random.randint(0,List.shape[0])]
Leitung6 = List[np.random.randint(0,List.shape[0])]
Leitung7 = List[np.random.randint(0,List.shape[0])]
Leitung8 = List[np.random.randint(0,List.shape[0])]
Leitung9 = List[np.random.randint(0,List.shape[0])]


Kneu = np.zeros(K.shape,int)
Aneu = np.zeros(K.shape,int)


#for j in range(K.shape[0]):
#    for l in range(K.shape[0]):
#        Kneu[j][l] += K[j][l]
#Kneu[Leitung[0]][Leitung[1]] = 0

#for x in range(K.shape[0]):
#    for y in range(K.shape[0]):
#        Aneu[j][l] += A[j][l]
#Aneu[Leitung[0]][Leitung[1]] = 0
        
#Kspeicher = np.zeros(K.shape,int)
#for a in range(K.shape[0]):
#    for b in range(K.shape[0]):
#        Kspeicher[a][b] += K[a][b]





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
    
    if(i == Nt/2):
        K[Leitung0[0]][Leitung0[1]] = 0
        K[Leitung1[0]][Leitung1[1]] = 0
        K[Leitung2[0]][Leitung2[1]] = 0
        K[Leitung3[0]][Leitung3[1]] = 0
        K[Leitung4[0]][Leitung4[1]] = 0
        K[Leitung5[0]][Leitung5[1]] = 0
        K[Leitung6[0]][Leitung6[1]] = 0
        K[Leitung7[0]][Leitung7[1]] = 0
        K[Leitung8[0]][Leitung8[1]] = 0
        K[Leitung9[0]][Leitung9[1]] = 0
        
        A[Leitung0[0]][Leitung0[1]] = 0
        A[Leitung1[0]][Leitung1[1]] = 0
        A[Leitung2[0]][Leitung2[1]] = 0
        A[Leitung3[0]][Leitung3[1]] = 0
        A[Leitung4[0]][Leitung4[1]] = 0
        A[Leitung5[0]][Leitung5[1]] = 0
        A[Leitung6[0]][Leitung6[1]] = 0
        A[Leitung7[0]][Leitung7[1]] = 0
        A[Leitung8[0]][Leitung8[1]] = 0
        A[Leitung9[0]][Leitung9[1]] = 0
        
        
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
        v = 10000+i
        fig.savefig("video"+str(v)+".png")
    
       
        plt.pause(0.0001)
