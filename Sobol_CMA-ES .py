# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 11:07:48 2017

@author: msmanski
"""

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
import cma
import numpy as np


from deap import benchmarks


def gaussians(coordinate,H,M,W):
    """Coordinate is the point to evaluate, 
    H is a matrix of peak heights
    M is a matrix with the x,y coordinates of peaks
    W is a matrix with the x and y 'peak widths for non normal distributions
    """
    return np.multiply(-1,sum((np.power(H[i],1-1*(sum((np.divide(np.power(x-M[i][j],2),2*np.power(W[i][j],2))) for j,x in enumerate(coordinate))))) for i in range(len(H))))

def gaussiansObjFunc(coordinate):
    return gaussians(coordinate,H,M,W)


fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(-500, 500, 10)
Y = np.arange(-500,500, 10)
X, Y = np.meshgrid(X, Y)
Z = np.zeros(X.shape)

landscape = 'medium'
# The CMA-ES algorithm requires that the landscape be represented as a function rather than loaded from a csv file.

if landscape == 'smooth':
    M = [[200, 100], [-150, -200], [-100, 300]]
    H = [50, 35, 30]
    W = [[300, 600], [300, 230], [300, 900]]
elif landscape == 'medium':
    M = [[200, 100], [-150, -200], [-100, 300]]
    H = [50, 35, 30]
    W = [[200, 400], [200, 150], [200, 600]]
elif landscape == 'rugged':
    M = [[200, 100], [-150, -200], [-100, 300]]
    H = [50, 35, 30]
    W = [[150, 300], [150, 120], [150, 450]]

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        Z[i,j] = gaussians((X[i,j],Y[i,j]), H, M, W)

ax.plot_surface(X, Y, Z, rstride=1, cstride=1,  norm=LogNorm(), cmap=cm.jet, linewidth=0.2)
 
plt.xlabel("x")
plt.ylabel("y")

plt.show()
    


startingCoordinate = [-200,200]
sigma0=180
NumberDesigns = 50
KeepSet = 1
NumIter = 15

es = cma.CMAEvolutionStrategy(startingCoordinate,sigma0, {'popsize': NumberDesigns,'CMA_mu':KeepSet})

es.mean = startingCoordinate

i=0
while i<5:
    print('a',es.mean)
    solutions = es.ask()
    plt.figure()
    plt.contour(X, Y, Z)
    plt.scatter(np.vstack(solutions)[:,0],np.vstack(solutions)[:,1], color = 'grey')
    plt.show()
    es.tell(solutions,[gaussiansObjFunc(x) for x in solutions])
    print('b',es.mean)
    es.disp()
    i=i+1
es.result_pretty()
es.plot()

