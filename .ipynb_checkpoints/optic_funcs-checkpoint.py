'''
Useful functions for tutorials.
Author: Grace E. Chesmore
'''
import numpy as np

def rad2arcmin(x_arr):
    '''
    Convert radians to arcminutes.
    '''
    return x_arr*60*180/np.pi

def arcmin2rad(x_arr):
    '''
    Convert arcminutes to radians.
    '''
    return x_arr*np.pi/180/60
    