def bellmanford(n,m,edges,src):
    dist=[10**8 for i in range(n)]
    dist[src]=0
    for i in range(n):
        for edge in edges:
            u,v,w=edge[0],edge[1],edge[2]
            if dist[u]!=10**8 and dist[u]+w<dist[v]:
                dist[v]=dist[u]+w
    # nth relaxation to check negative cycle:
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        if dist[u]!=10**8 and dist[u]+w<dist[v]:
            return [-1]
    
    return dist[n-1]
