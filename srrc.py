# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 16:37:10 2020

@author: LENI

s=srrc(syms, beta, P, t_off)
Create a Square-Root Raised Cosine Pulse that
     'syms' is 1/2 the length of srrc pulse in symbol durations;
     'beta' is the rolloff factor: beta=0 gives the sinc function;
     'P' is the oversampling factor;
     't_off' is the phase (or timing) offset.


"""

import numpy as np
import warnings


def srrc(syms, beta, P, t_off=0):
    t=np.arange(-syms*P+t_off,syms*P+1+t_off)            # sampling indices as a multiple of T/P
    """
    if (beta==0):
        beta=np.finfo(float).tiny                     # numerical problems if beta=0
    
    return (4*beta/np.sqrt(P)*(np.cos((1+beta)*np.pi*t/P)+\
    np.sin((1-beta)*np.pi*t/P)/(4*beta*t/P))/\
    (np.pi*(1-16*(beta*t/P)**2)))              # calculation of srrc pulse
    """
    #with warnings.catch_warnings():
    try:
        warnings.simplefilter("ignore")
        srrc_w = ((np.sin((1-beta)*np.pi*t/P)+\
                 (4*beta*t/P)*np.cos((1+beta)*np.pi*t/P))/\
                (np.sqrt(P)*(np.pi*t/P)*(1-16*(beta*t/P)**2))) # calculation of srrc pulse
 #       warnings.simplefilter("default")
    finally:
        srrc_w[t==0] = (1-beta+4*beta/np.pi)/np.sqrt(P)     # replace when t=0
        if beta !=0 :
            # replace when t=+/- P/(4*beta)
            srrc_w[np.abs(t)==P/(4*beta)] = (beta/(np.pi*np.sqrt(2*P)))*\
                ((np.pi+2)*np.sin(np.pi/(4*beta))+\
                (np.pi-2)*np.cos(np.pi/(4*beta)))
    return srrc_w
        
if __name__ == "__main__":
    print(srrc(3,0.1,2))
