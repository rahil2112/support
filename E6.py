import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df=pd.read_csv("pseudo_facebook.csv")
print(df. head( ))

# Load edge list
fb_graph=nx.from_pandas_edgelist(df,source="age", target="dob_year")
type(fb_graph)

print('Display all the Edges')
print(fb_graph.edges())

print('\nDisplay all the nodes')
print(fb_graph.nodes())

print('\nAdd new node in graph')
fb_graph.add_edge("123","2154")
print(fb_graph.nodes())

G= nx.Graph(fb_graph)

print('\nVisualization of network')

nx.draw(fb_graph,with_labels=True)
plt.show()

print('\nDegree of each node')
print(nx.degree(fb_graph))

print('\ndegree of a particular node')
print(nx.degree(fb_graph,1999))
 
print('\ndegree centrality')
print(nx.degree_centrality(fb_graph))

print('\nsort degree centrality')
print(sorted(nx.degree_centrality(fb_graph).values()))

print('\nDisplay influential node')
m_influential=nx.degree_centrality(G)
for w in sorted(m_influential,key=m_influential.get,reverse=True):
 print(w,m_influential[w])

print('\nFind Betweenness centrality')
pos=nx.spring_layout(G)
betCent=nx.betweenness_centrality(G,normalized=True,endpoints=True)
node_color=[20000.0*G.degree(v)for v in G]
node_size=[v*10000 for v in betCent.values()]
print(plt.figure(figsize=(20,20)))
print(nx.draw_networkx(G,pos=pos,with_labels=False,node_color=node_color,node_size=node_size))
print(sorted(betCent,key=betCent.get,reverse=True)[:5])
plt.show()

print('\nCloseness centrality')
closeness_centrality=nx.centrality.closeness_centrality(G)
print((sorted(closeness_centrality.items(),key=lambda item:item[1],reverse=True))[:8])

print('\nFind Density of a network')
node_size=[v*50 for v in closeness_centrality.values()]
plt.figure(figsize=(15,8))
print(nx.draw_networkx(G,pos=pos,node_size=node_size,with_labels=False,width=0.15))
print(plt.axis("off"))
plt.show()

print('\nCheck is there any Bridges exist')
print(nx.has_bridges(G))

print('\nCount the number of bridges in network')
bridges=list(nx.bridges(G))
len(bridges)

print('\nTo find local bridges')
K = nx.cycle_graph(9)
(0, 8, 8) in set(nx.local_bridges(K))
print('Find complete graph')
G = nx.complete_graph(range(11, 14))
print(list(G.nodes()))

print('\nRemove node')
G = nx.path_graph(8) 
print(list(G.edges))

print('\nAfter removing Node')
G = nx.path_graph(8) 
print(list(G.edges))

print('\nRemove edges')
G = nx.path_graph(8)  # or DiGraph, etc
G.remove_edge(0, 1)
print(list(G.edges))

print('\nClustering')
print(nx.clustering(G))

print('\nCommunity detection')
#Edge betweenness
lst_b = nx.algorithms.community.girvan_newman(fb_graph)
type(lst_b)
#Print possible communities
for x in lst_b:
 print(x)
