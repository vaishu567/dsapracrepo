
def dfssafe(adj,vis,pathvis,node,check):
    vis[node]=1
    pathvis[node]=1
    for neighbour in adj[node]:
        if vis[neighbour]!=1:
            if dfssafe(adj,vis,pathvis,neighbour,check)==True:
                check[neighbour]=0
                return True
        elif pathvis[neighbour]==1:
            check[neighbour]=0
            return True
    # if dfsis succses fully completed for a node then it is a safe node
    
    pathvis[node]=0
    check[node]=1
    return False





def safenode(adj,n):
    vis=[0 for _ in range(n)]
    pathvis=[0 for _ in range(n)]
    safenodes=[]
    check=[0 for _ in range(n)]
    for i in range(n):
        if vis[i]!=1:
            dfssafe(adj,vis,pathvis,i,check)
    for i in range(n):
        if check[i]==1:
            safenodes.append(i)
    return safenodes

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
n=len(graph)
print(safenode(graph,n))