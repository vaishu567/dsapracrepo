# how  to takeinput for a graph:
# adjacency  list:
def inputgraph():
    n=int(input("ennter no of  nodes in graph:"))
    m=int(input("ennter no of edges in graph:"))
    adjacency=[[] for i in range(m+1)]
    for _ in range(m):
        u,v = map(int, input("Enter u and v values separated by a space: ").split())
        adjacency[u].append(v)
        adjacency[v].append(u)
    return adjacency
print(inputgraph())
#n=5
#m=6
#adjacency=[[] for i in range(n+1)]
#print(adjacency)


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
