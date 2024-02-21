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