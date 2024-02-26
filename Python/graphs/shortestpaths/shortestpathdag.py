def dfs(adj,n,node,vis,topostackarr):
    vis[node]=1
    for neighbour in adj[node]:
        ininode=neighbour[0]
        if vis[ininode]!=1:
            dfs(adj,n,ininode,vis,topostackarr)
    topostackarr.append(node)
    return 

def shortestpath(n,m,edges):
    adj=[[] for i in range(n)]
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        adj[u].append([v,w])
    dist=[float('inf') for _ in range(n)]
    vis=[0 for _ in range(n)]
    topostackarr=[]
    # we will perform topological sort using dfs
    for i in range(n):
        if vis[i]!=1:
            dfs(adj,n,i,vis,topostackarr)
    # doing relaxation thing:
    dist[0]=0
    while topostackarr:
        node=topostackarr.pop(-1)
        for nodein in adj[node]:
            neighbour=nodein[0]
            distance=nodein[1]
            dist[neighbour]=min(dist[neighbour],(dist[node]+distance))
    return dist


