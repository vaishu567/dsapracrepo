def printAdjacency(n, m, edges):
    # n=int(input("ennter no of  nodes in graph:"))
    # m=int(input("ennter no of edges in graph:"))
    adjacency=[[i] for i in range(n)]
    for i in edges:
        u,v=i[0],i[1]
        adjacency[u].append(v)
        adjacency[v].append(u)
    return adjacency
    
# 3 2
# 2 1
# 2 0
n=3
m=2
edges=[(2,1),(2,0)]
adjacency=[[i] for i in range(n)]
print(adjacency)
print(printAdjacency(n, m, edges))