def dfs(node,adj,vis):
    vis=[0]*(n)
    vis[node]=1
    for neighbour in adj[node]:
        if vis[neighbour]!=1:
            vis=dfs(neighbour,adj,vis)
    return vis
def provinces(roads):
    n=len(roads)
    vis=[0]*(n+1)
    count=0
    for i in range(1,n+1):
        if vis[i]==0:
            count+=1
            vis=dfs(i,roads,vis)
    return count


