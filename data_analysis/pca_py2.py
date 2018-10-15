#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:52:36 2017

@author: Apple
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


from sklearn.decomposition import PCA

#Load data set
data = pd.read_csv('all_metabolic_genes_FPKM.csv')
labels = data[data.columns[0]] 
head = list(data)[1:] 
##convert it to numpy arrays
#data=data[:]
#X=data[1:].values

data2 = data.drop(data.columns[0], axis = 1)
data2 = pd.DataFrame.transpose(data2)
data2 = np.log2(data2 + 1)

centers = [[1, 1], [-1, -1], [1, -1]]

# 3d pca
pca_3 = PCA(3)

plot_columns = pca_3.fit_transform(data2)
variance_ratio = pca_3.explained_variance_ratio_



plt.scatter(x = plot_columns[:,0], y = plot_columns[:,1])



## figure size & axs
fig = plt.figure(1)

#plt.clf()

## Set/get 3d viewing direction for Matplotlib Axes3D
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=20, azim=117) # azim: make left handside axs to right



ax.grid(False)
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
# remove pane gray
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False


# grid
plt.cla()

# seven colors for seven types of cell
colors = ['#DDDDDD',
          '#0044BB',
          '#CC0000',
          '#CCEEFF',
          '#BBBB00',
          '#FF8C00',
          '#D28EFF']
labels = ['Ast', 'Neu', 'OPC', 'NFO', 'MO', 'MG', 'ECs']

X = plot_columns

for a in xrange(14):
    ax.scatter(X[:, 0][a], X[:, 1][a], X[:, 2][a], 
               s = 150, c = colors[a/2], label = labels[a/2])

# text format
from matplotlib import rc
rc('font', size=10, family='Sans serif', weight = 'bold')
ax.set_xlabel("PC1 (%.0f" % (variance_ratio[0] * 100)+'%)', weight = 'bold')
ax.set_ylabel("PC2 (%.0f" % (variance_ratio[1] * 100)+'%)', weight = 'bold')
ax.set_zlabel("PC3 (%.0f" % (variance_ratio[2] * 100)+'%)', weight = 'bold')



ax.xaxis.set_ticks_position('top') 
ax.yaxis.set_ticks_position('top')
ax.zaxis.set_ticks_position('top')



plt.legend(loc = 10, 
           scatterpoints = 1, ncol=7, fontsize=8, 
           bbox_to_anchor=(0.5, 1),markerscale = 0.8)


plt.show()
fig.savefig('3d_pca-2017-7-29.eps', format='eps', bbox_inches='tight')
