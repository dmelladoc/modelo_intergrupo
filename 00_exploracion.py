#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 13:50:24 2020

@author: caribu
"""


import numpy as np
import matplotlib.pyplot as plt
import h5py
from sklearn.manifold import TSNE

data = h5py.File('data/ITPCdata15Ch10Rep.mat', mode="r")
mat = np.array(data['imagenes']) #10860,717,21
tarea = np.array(data['tarea'], dtype=np.int).squeeze()
sujeto = np.array(data['sujeto'], dtype=np.int).squeeze()

tsne = TSNE(n_components=2, init="pca")
x0 = mat.reshape(len(mat), -1)
xt = tsne.fit_transform(x0)


plt.scatter(xt[:,0], xt[:,1], c=sujeto)