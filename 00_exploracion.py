#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:50:24 2020

@author: caribu
"""


import numpy as np
import matplotlib.pyplot as plt
import h5py


data = h5py.File('data/ITPCdata15Ch10Rep.mat')
mat = np.array(data['imagenes']) #10860,717,21
tarea = np.array(data['tarea'], dtype=np.int).squeeze()
sujeto = np.array(data['sujeto'], dtype=np.int).squeeze()


# Prueba con sujeto 1 y tarea 1
events = np.logical_and(sujeto == 1, tarea == 1)
mat_s1 = mat[events]

mean_sigs = np.mean(mat_s1, axis=0)
plt.plot(mean_sigs)

#