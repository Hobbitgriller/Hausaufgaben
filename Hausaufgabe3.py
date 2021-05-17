# -*- coding: utf-8 -*-
"""
Created on Thu May 13 14:45:16 2021

@author: christoph
"""

import numpy as np
import matplotlib.pyplot as plt

#Dieses Programm dient der Beschreibung von gekoppelten Oszillatoren
#Dazu wird die Runge-Kutta Methode verwendet mit Ordnung 4

#adjacency matrix A:
# 0 1 1
# 1 0 1
# 1 1 0

#Anzahl gibt die Anzahl der Oszillatoren an
Anzahl = 3
Matrix = np.array([[0,1,1],[1,0,1],[1,1,0]])
AdMatrix = 50*Matrix
Frequenz = np.array([0.19,0.2,0.21])

Zeitschritt = 0.001	# dein Zeitschritt war zu groß
Zeit = np.arange(0,10,Zeitschritt)

xList = np.zeros([Zeit.size,Anzahl])
xList[0] = np.random.uniform(0., 2*np.pi, Anzahl)	# random Initial Conditions
print(xList[0])						# check ob ich scheiß gebaut hab
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

for i in range(1, Zeit.size):	# du musst bei 1 anfangen, da der 0. Schritt ja nicht erst ausgerechnet mist. [i-1] waere dann [-1] also der letzte Schritt, also immer 0.
#				  Deswegen war deinem Code die Anfangsbedingung egal. 
    
    k1 = Funktion(xList[i-1],Frequenz,AdMatrix)
    k2 = Funktion(xList[i-1]+Zeitschritt/2*k1,Frequenz,AdMatrix)
    k3 = Funktion(xList[i-1]+Zeitschritt/2*k2,Frequenz,AdMatrix)
    k4 = Funktion(xList[i-1]+Zeitschritt*k3,Frequenz,AdMatrix)
    xList[i] = xList[i-1]+ Zeitschritt/6*(k1+(2*k2)+(2*k3)+k4) 
    
print(xList) 	# check obs jetzt funktioniert
Ergebnisx1 = np.zeros(Zeit.size)
Ergebnisx2 = np.zeros(Zeit.size)
Ergebnisx3 = np.zeros(Zeit.size)

for i in range(Zeit.size):
    Ergebnisx1[i] = xList[i][0]
    Ergebnisx2[i] = xList[i][1]
    Ergebnisx3[i] = xList[i][2]

plt.plot(Zeit, (Ergebnisx1),label="Oszi 1", color="red")
plt.plot(Zeit, (Ergebnisx2),label="Oszi 2", color="blue")
plt.plot(Zeit, (Ergebnisx3),label="Oszi 3", color="green")
plt.legend()

plt.savefig('smallstep.pdf') # ich brauchte ein Beispiel für heute Nachmittag. 
plt.show()
