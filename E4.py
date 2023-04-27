import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats

print('Histogram')
sns.distplot(df['age']);
plt.show()

print('Correlation Matrix')
corrmat = df.corr()
f, ax = plt.subplots(figsize=(12, 9))
sns.heatmap(corrmat, vmax=.8, square=True);
plt.show()

print('Scatter plot for 6 variable')
sns.set()
cols = ['age','dob_day','dob_year', 'dob_month','gender', 'tenure','likes']
sns.pairplot(df[cols], size = 2.5)
plt.show();

import networkx as nx
print('Draw graph G with a circular layout.')
G = nx.complete_graph(df['age'])
pos = nx.circular_layout(G)
nx.draw(G, pos=pos) 
nx.draw(G.subgraph([0, 1, 2]), pos=pos, node_color="red")
plt.show()

print('Draw graph G with a random layout.')
G = nx.complete_graph(df['age'])
pos = nx.random_layout(G)
nx.draw(G, pos=pos) 
nx.draw(G.subgraph([0, 1, 2]), pos=pos, node_color="red")
plt.show()

print(' Draw graph G with a spectral 2D layout.')
G = nx.complete_graph(df['age'])
pos = nx.spectral_layout(G)
nx.draw(G, pos=pos)  
nx.draw(G.subgraph([0, 1, 2]), pos=pos, node_color="red") 
plt.show()

print('Draw graph G with a spiral layout.')
G = nx.complete_graph(df['age'])
pos = nx.spiral_layout(G)
nx.draw(G, pos=pos)  
nx.draw(G.subgraph([0, 1, 2]), pos=pos, node_color="red")
plt.show()


print('Draw graph G with a shell layout.')
G = nx.complete_graph(df['age'])
pos = nx.shell_layout(G)
nx.draw(G, pos=pos)  
nx.draw(G.subgraph([0, 1, 2]), pos=pos, node_color="red")
plt.show()