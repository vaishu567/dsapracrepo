def undirected(n,edges,src):
    vis=[0 for i in range(n)]
    adj=[[] for _ in range(n)]
    for edge in edges:
        u,v=edge[0],edge[1]
        adj[u].append(v)
        adj[v].append(u)
    dist=[float('inf') for _ in range(n)]
    dist[src]=0
    to_visit=[src]
    vis[src]=1
    while to_visit:
        node=to_visit.pop(0)
        for neighbour in adj[node]:
            if vis[neighbour]!=1:
                vis[neighbour]=1
                dist[neighbour]=min(dist[neighbour],dist[node]+1)
                to_visit.append(neighbour)
    return dist


edges=[[0,1],[1,4],[2,3],[2,4],[3,4]]
n=5
src=1
print(undirected(n,edges,src))