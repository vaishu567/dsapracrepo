def dfs(node,adj,vis):
    vis[node]=1
    for neighbour in adj[node]:
        if vis[neighbour]!=1:
            vis=dfs(neighbour,adj,vis)
    return vis
def dfsadjmat(adjmat,n,m):
    adjarr=[[]for i in range(n+1)]
    for i in range(n):
        for j in range(m+1):
            if adjmat[i][j]==1 and i!=j:
                adjarr[i].append(j)
    vis=[0]*n
    count=0
    for ind in range(n):
        if vis[ind]==0:
            count+=1
            vis=dfs(ind,adjarr,vis) 
    return count
adjmat= [ [1, 1, 1, 0],[1, 1, 1, 0],[1, 1, 1, 0],[0, 0, 0, 1] ]  
n=len(adjmat)
m=3
print(dfsadjmat(adjmat,n,m))
    


