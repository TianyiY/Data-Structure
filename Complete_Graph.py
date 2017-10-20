def make_link(Graph, node1, node2):
    if node1 not in Graph:
        Graph[node1]={}
    (Graph[node1])[node2]=1
    if node2 not in Graph:
        Graph[node2]={}
    (Graph[node2])[node1]=1
    return Graph

# return the number of edges
def clique(n):
    Graph={}

    for i in range(n):
        for j in range(n):
            if i<j:
                make_link(Graph, i, j)
    return sum([len(Graph[node]) for node in Graph.keys()])/2

for n in range(1, 10):
    print n, clique(n)