# the previous algo doesnot work becoz this is a directed graph:
def dfs(adj,node,n,vis,pathvis):
    vis[node]=1
    pathvis[node]=1
    for neighbour in adj[node]:
        # when the node is not visited:
        if vis[neighbour]!=1:
            if dfs(adj,neighbour,n,vis,pathvis)==True:
                return True
        # node is already visited but it has to be visited onthe same path:
        elif pathvis[neighbour]==1:
            return True

    pathvis[node]=0
    return False



def detectcycle(adj,n):
    vis=[0 for _ in range(n)]
    pathvis=[0 for _ in range(n)]
    for i in range(n):
        if vis[i]!=1:
            if dfs(adj,i,n,vis,pathvis)==True:
                return True
    return False