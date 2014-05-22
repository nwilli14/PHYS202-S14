import numpy as np
import matplotlib.pyplot as plt
def traps(func, a, b, N):
    """This takes a function and approximates the definite integral
    from a to b by using N trapizodes
    h is the width of each trapizode"""
    h = (b-a)/N
    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())
    #print "Trap rule integral ="
    return I
    
    
def simps(func, a, b, N):
    """This takes a function and approximates the definite integral
    form a to b by using N quadratics"""
    h = (b-a)/N
    
    k1 = np.arange(1,N/2+1)
    K2 = np.arange(1,N/2)
    I = (1./3.)*h*(func(a) +func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*K2*h).sum())
    #print "simps rule integral ="
    return I