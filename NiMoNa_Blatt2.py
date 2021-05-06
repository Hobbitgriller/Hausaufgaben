# -*- coding: utf-8 -*-
"""
Created on Wed May  5 17:36:39 2021

@author: Christoph test
"""
import numpy as np
import matplotlib.pyplot as plt

print("Diese Programm stellt ein sehr simples Räuber Beute Schema dar")

#Die Beute Population beträgt zu Begin 1000 die Räuber Population 100.
#e_1 gibt die Reproduktionsrate der Beute pro Zeitintervall an.
#y_1 gibt die Wahrscheinlichkeit an mit der ein Räuber eine Beute frisst.
#e_2 gibt die Wahrscheinlichkeit an das ein Räuber stirbt.
#y_2 gibt die Reproduktionsrate ein Räuber Beute findet UND sich fortpflanzt.

h = 0.025
ZeitSchritte = np.arange(0, 30, h)
e1 = 2.0
e2 = 0.8
y1 = 0.02
y2 = 0.0002

#Berechnung mittels Euler Methode

BeuteAnzahl = np.zeros(ZeitSchritte.size)
JägerAnzahl = np.zeros(ZeitSchritte.size)

BeuteAnzahl[0] = 1000
JägerAnzahl[0] = 100

for i in range(1,BeuteAnzahl.size):
    BeuteAnzahl[i] = BeuteAnzahl[i-1] + h*BeuteAnzahl[i-1]*(e1-y1*JägerAnzahl[i-1]) 
    JägerAnzahl[i] = JägerAnzahl[i-1] - h*JägerAnzahl[i-1]*(e2-y2*BeuteAnzahl[i-1]) 
    
#plt.plot(ZeitSchritte, BeuteAnzahl, label="Beutetiere" , color="Green")
#plt.plot(ZeitSchritte, JägerAnzahl, label="Jäger" , color="red")
plt.plot(JägerAnzahl, BeuteAnzahl, label="Euler J-B",  color="Blue")


#Berechnung mittels Heun Verfahren

BeuteAnzahl2 = np.zeros(ZeitSchritte.size)
JägerAnzahl2 = np.zeros(ZeitSchritte.size)

BeuteAnzahlz = np.zeros(ZeitSchritte.size)
JägerAnzahlz = np.zeros(ZeitSchritte.size)

BeuteAnzahl2[0] = 1000
JägerAnzahl2[0] = 100

BeuteAnzahlz[0] = 1000
JägerAnzahlz[0] = 100

for i in range(1, BeuteAnzahl2.size):

    BeuteAnzahlz[i] = BeuteAnzahlz[i-1] + h*BeuteAnzahlz[i-1]*(e1-y1*JägerAnzahlz[i-1]) 
    JägerAnzahlz[i] = JägerAnzahlz[i-1] - h*JägerAnzahlz[i-1]*(e2-y2*BeuteAnzahlz[i-1])
    BeuteAnzahl2[i] = BeuteAnzahl2[i-1] + h/2*( BeuteAnzahl2[i-1]*( e1-y1*JägerAnzahl2[i-1] ) + 
                                               (BeuteAnzahlz[i]*(e1-y1*JägerAnzahlz[i]) ) )
    JägerAnzahl2[i] = JägerAnzahl2[i-1] - h/2*( JägerAnzahl2[i-1]*( e2-y2*BeuteAnzahl2[i-1] ) + 
                                               (JägerAnzahlz[i]*(e2-y2*BeuteAnzahlz[i]) ) ) 
    BeuteAnzahlz[i] = BeuteAnzahl2[i]
    JägerAnzahlz[i] = JägerAnzahl2[i]

#plt.plot(ZeitSchritte, BeuteAnzahl2, label="Beutetiere" , color="Violet")
#plt.plot(ZeitSchritte, JägerAnzahl2, label="Jäger" , color="Brown")
plt.plot(JägerAnzahl2, BeuteAnzahl2, label="Heun J-B", color="Pink")

plt.legend()

