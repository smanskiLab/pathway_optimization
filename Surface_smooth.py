# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 07:38:35 2016

@author: msmanski

This script is used to create model surfaces on a 10000 x 10000 grid that 
reflect smooth NK ruggedness.

"""


from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

# Initialize matrices
X = np.zeros([1000,1000])
Y = np.zeros([1000,1000])
Z = np.zeros([1000,1000])
Za = np.zeros([1000,1000])
Zb = np.zeros([1000,1000])
Zc = np.zeros([1000,1000])
Zd = np.zeros([1000,1000])

Y[0,:] = -500
X[:,0] = -500
i = 1
while i < 1000:
    Y[i,:] = Y[i-1,0]+1
    X[:,i] = X[0,i-1]+1
    i = i+1

#Create a matrix Z, which constitutes the Z value for each of the x,y coordinates in X,Y; make this 3d gausian functions
Aa=50
xaCenter=100
xaWidth=600
yaCenter=200
yaWidth=300
x=0
while x < 1000:
    y = 0
    while y < 1000:
        Za[x,y] = np.power(Aa,1-1*(np.divide(np.power(X[0,x]-xaCenter,2),2*np.power(xaWidth,2))+np.divide(np.power(Y[y,0]-yaCenter,2),2*np.power(yaWidth,2))))
        y=y+1
    x=x+1


Ac=35
xcCenter=-200
xcWidth=230
ycCenter=-150
ycWidth=300
x=0
while x < 1000:
    y = 0
    while y < 1000:
        Zb[x,y] = np.power(Ac,1-1*(np.divide(np.power(X[0,x]-xcCenter,2),2*np.power(xcWidth,2))+np.divide(np.power(Y[y,0]-ycCenter,2),2*np.power(ycWidth,2))))
        y=y+1
    x=x+1

Ad=30
xdCenter=300
xdWidth=900
ydCenter=-100
ydWidth=300
x=0
while x < 1000:
    y = 0
    while y < 1000:
        Zc[x,y] = np.power(Ad,1-1*(np.divide(np.power(X[0,x]-xdCenter,2),2*np.power(xdWidth,2))+np.divide(np.power(Y[y,0]-ydCenter,2),2*np.power(ydWidth,2))))
        y=y+1
    x=x+1

Z = Za + Zb + Zc


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z, rstride=50, cstride=50)

plt.show()

np.savetxt('Z-values_smooth.csv', Z, delimiter=',')