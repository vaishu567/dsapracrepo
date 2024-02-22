# bfs using adjacency list:
def bfs(adj,n):
    bfsa=[]
    visited=set()
    start=0
    to_visit=[start]
    visited.add(start)
    while to_visit:
        node=to_visit.pop(0)
        bfsa.append(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                to_visit.append(neighbor)
                visited.add(neighbor)
    return bfsa


graph = [[1,2,3], [4,7], [5], [6], [], [], [], []]
n=len(graph)
print(bfs(graph,n))


# bfs using adjacency matrix:
def bfsmat(adjmat,n,m):
    adjarr=[[]for i in range(n+1)]
    for i in range(n):
        for j in range(m+1):
            if adjmat[i][j]==1 and i!=j:
                adjarr[i].append(j)
    bfsa=[]
    visited=set()
    start=0
    to_visit=[start]
    visited.add(start)
    while to_visit:
        node=to_visit.pop(0)
        bfsa.append(node)
        for neighbor in adjarr[node]:
            if neighbor not in visited:
                to_visit.append(neighbor)
                visited.add(neighbor)
    return bfsa

adjmat=[[0, 1, 1, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 1], [1, 0, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
n=7
m=7
print(bfsmat(adjmat,n,m)) 

    


