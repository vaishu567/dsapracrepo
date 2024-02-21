# how  to takeinput for a graph:
# adjacency  list:
def inputgraph():
    n=int(input("ennter no of  nodes in graph:"))
    m=int(input("ennter no of edges in graph:"))
    adjacency=[[]*(m+1) for i in range(n+1)]
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
    
    


