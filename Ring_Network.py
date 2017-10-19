def make_link(Graph, node1, node2):
    if node1 not in Graph:
        Graph[node1]={}
    (Graph[node1])[node2]=1
    if node2 not in Graph:
        Graph[node2]={}
    (Graph[node2])[node1]=1
    return Graph

# make an empty Graph
ring={}

n=5

# add in the edges
for i in range(n):
    make_link(ring, i, (i+1)%n)

# how many nodes?
print len(ring)

# how many edges?
print sum([len(ring[node]) for node in ring.keys()])/2

print ring
print ring[1][0]
print ring.keys()
print ring[0]
print len(ring[0])
