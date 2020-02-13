# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:42:20 2019

@author: jupiter
"""
import numpy as np
import configparser
    

    


def smartcomb(type1, type2):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    type1arr = np.array([float(i) for i in config['TYPES'][type1].split()])
    type2arr = np.array([float(j) for j in config['TYPES'][type2].split()])
    
    comb = type1arr*type2arr
    return comb
    

