# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:58:38 2020

@author: LENI

seq=pam(len,M,Var)
Raw M-PAM stream with length 'len' and variance 'Var' acording with PAM
modulation signal model.

"""

import numpy as np


def pam(len,M,Var):
    return (2*np.floor(M*np.random.rand(1,len))-M+1)*np.sqrt(3*Var/((M**2)-1))


if __name__ == "__main__":
    pam(10,2,1)
