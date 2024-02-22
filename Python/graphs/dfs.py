# dfs using adjlist:

def dfs(node,adj,vis,dfsa):
    vis[node]=1
    dfsa.append(node)
    for neighbour in adj[node]:
        if vis[neighbour]!=1:
            dfsa=dfs(neighbour,adj,vis,dfsa)
    return dfsa
def dfsofgraph(n,adj):
    vis=[0]*(n)
    start=0
    dfsa=[]
    dfsa=dfs(start,adj,vis,dfsa)
    return dfsa

# dfs using adjMatrix:
def dfs(node,adj,vis,dfsa):
    vis[node]=1
    dfsa.append(node)
    for neighbour in adj[node]:
        if vis[neighbour]!=1:
            dfsa=dfs(neighbour,adj,vis,dfsa)
    return dfsa
def dfsadjmat(adjmat,n,m):
    adjarr=[[]for i in range(n+1)]
    for i in range(n):
        for j in range(m+1):
            if adjmat[i][j]==1:
                adjarr[i].append(j)
    vis=[0]*n
    start=0
    dfsa=[]
    dfsa=dfs(start,adjarr,vis,dfsa)
    return dfsa




