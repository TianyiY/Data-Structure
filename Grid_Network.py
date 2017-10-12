def make_link(Graph, node1, node2):
    if node1 not in Graph:
        Graph[node1]={}
    (Graph[node1])[node2]=1
    if node2 not in Graph:
        Graph[node2]={}
    (Graph[node2])[node1]=1
    return Graph

Graph={}

n=256

import math
side=int(math.sqrt(n))

# add in the edges
for i in range(side):
    for j in range(side):
        if i<side-1:
            make_link(Graph, (i, j), (i+1, j))
        if j<side-1:
            make_link(Graph, (i, j), (i, j+1))

# how many nodes?
print len(Graph)

# how many edges?
print sum([len(Graph[node]) for node in Graph.keys()])/2
