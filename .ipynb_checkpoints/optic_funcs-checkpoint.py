import numpy as np

def rad2arcmin(x):
    return x*60*180/np.pi

def arcmin2rad(x):
    return x*np.pi/180/60
    