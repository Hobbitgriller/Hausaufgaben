import numpy as np
import matplotlib.pyplot as plt

def AdjAnalyse(Adj):
    j = 0
    for i in range(Adj.shape[1]):
        for k in range(Adj.shape[1]):
            if (Adj[i][k] == 1):
                j += 1
    
    List = np.zeros((j,2),int)
    v = 0
    
    for i in range(Adj.shape[1]):
        for k in range(Adj.shape[1]):
            if (Adj[i][k] == 1):
                List[v][0] = i
                List[v][1] = k
                v += 1
    return List
    





#def ausfalltemp(Adj, i, Liste, Ausfalldauer):
#    Liste[i%Ausfalldauer] = i+1
#    if (Liste[i%Ausfalldauer-1] =/ 0 && Liste[((i%Ausfalldauer)+1)%Ausfalldauer] =/ 0):
        
    
        
    
    
    
    
    
    
    