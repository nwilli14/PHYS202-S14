import numpy as np
import matplotlib.pyplot as plt
def twoPtForwardDiff(x,y):
    """Function that takes two arrays as inputs and returns the approximate
    derivative from 2 points, x and x+h. 
    df/dx = lim h->0[f(x+h)-f(x)/h]"""
    dy = np.diff(y)
    dx = np.diff(x)
    dydx = np.zeros(y.shape, float)
    
    dydx[0:-1] = dy/dx
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx

def twoPtCenteredDiff(x,y):
    """Function that takes two arrays as inputs and returns the approximate
    derivative from 2 points, x-h and x+h. 
    df/dx = lim h->0[f(x+h)-f(x-h)/2h]"""
    dy = np.diff(y)
    dx = np.diff(x)
    dydx = np.zeros(y.shape, float)
    
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx

def FourPtCenteredDiff(x,y):
    """function that takes two arrays as inputs and returns the approximate 
    derivative from 4 points.  used to get a more accurate derivative"""
    dy = np.diff(y)
    dx = np.diff(x)
    dydx = np.zeros(y.shape, float)
    dydx[2:-2] = (y[0:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:])/(12*(x[1]-x[0]))
    
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    dydx[1] = (y[2] - y[1])/(x[2] - x[1])
    dydx[-2] = (y[-3] - y[-2])/(x[-3] - x[-2])
    return dydx