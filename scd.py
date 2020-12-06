# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 22:17:38 2020

@author: LENI

Return a SCD (Spectral Correlation Density Function) of x
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def scd(x):
    M = x.size
    X = np.fft.fft(x)
    X_aux = (1/M)*np.conj(X)
    Sx = np.empty((M, M))
    
    for tau in range(M):
        Sx[tau,:] = X*np.roll(X_aux,tau)        
    
    return Sx
        
if __name__ == "__main__":
    M = 512
    x = np.random.random(M)
    Sx = scd(x)
    alpha = np.linspace(0,M-1,M)
    f = np.linspace(0,M-1,M)
    alpha, f = np.meshgrid(alpha,f)
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    ax.plot_surface(alpha,f,np.abs(Sx),cmap=cm.coolwarm)
    plt.show()
    