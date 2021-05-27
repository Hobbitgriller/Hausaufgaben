# -*- coding: utf-8 -*-
"""
Created on Wed May 26 19:12:51 2021

@author: christoph
"""

import numpy as np
import matplotlib.pyplot as plt
import random

Anzahl = 20
Kopplung = 5
matrixA = np.ones((Anzahl,Anzahl)) - np.identity((Anzahl))
matrix = matrixA*Kopplung

Zeitschritt = 0.001
Zeit = 0.2
Zeitintervall = np.arange(0, Zeit, Zeitschritt)

Frequenz = np.zeros(Anzahl)

for i in range(0,Anzahl):
    Frequenz[i] = random.uniform(4,10)

xList = np.zeros([Zeitintervall.size,Anzahl])
k1 = np.zeros(Anzahl)
k2 = np.zeros(Anzahl)
k3 = np.zeros(Anzahl)
k4 = np.zeros(Anzahl)

FunktionList = np.zeros(Anzahl)
Zahl = 0

def Funktion(xWerte, Alphas, AdjMatrix):
    global Zahl
    for i in range(Anzahl):
        for j in range(Anzahl):
           Zahl += AdjMatrix[i][j]*np.sin(xWerte[j]-xWerte[i])
        
        FunktionList[i] = Alphas[i] + Zahl
        Zahl = 0
        
    x_Ableitung = FunktionList
    return x_Ableitung

for i in range(0,Anzahl):
    xList[0][i] = random.uniform(0, 2*np.pi)
    

for i in range(1,Zeitintervall.size):
    k1 = Funktion(xList[i-1],Frequenz,matrix)
    k2 = Funktion(xList[i-1]+Zeitschritt/2*k1,Frequenz,matrix)
    k3 = Funktion(xList[i-1]+Zeitschritt/2*k2,Frequenz,matrix)
    k4 = Funktion(xList[i-1]+Zeitschritt*k3,Frequenz,matrix)
    xList[i] = xList[i-1]+ Zeitschritt/6*(k1+(2*k2)+(2*k3)+k4)
   

#for i in range(0,Anzahl):
#    plt.plot(Zeitintervall,xList[:,i])

    
rx = 0
ry = 0
v= 0

for n in range(0,Zeitintervall.size):
    rx = 0
    ry = 0
    for k in range(0,Anzahl):
        rx  += np.cos(xList[n][k])
        ry  += np.sin(xList[n][k])
    rx = rx/Anzahl
    ry = ry/Anzahl
    plt.arrow(0,0,rx,ry,color="red",head_width=0.10)   
    circle = np.linspace(0,2*np.pi,100)
    plt.plot(np.sin(circle),np.cos(circle))
    plt.plot(np.cos(xList[n]),np.sin(xList[n]),"o")
    plt.axis('scaled')
    for i in range(0,Anzahl):
        plt.arrow(0,0,np.cos(xList[n][i]),np.sin(xList[n][i]),color="black",head_width=0.05)
    v = 1000+n
    plt.savefig("video"+str(v)+".png")
    plt.close()

    
