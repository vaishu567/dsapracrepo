def dfs(adj,node,stack,vis):
    vis[node]=1
    for neighbour in adj[node]:
        if vis[neighbour]!=1:
            stack=dfs(adj,neighbour,stack,vis)
    stack.append(node)
    return stack



def topologicalsort(adj,n):
    # adj=[[] for _ in range(n)]
    # for _ in range(e):
    #     u,v = map(int, input().split())
    #     adj[u].append(v)
    vis=[0 for _ in range(n)]
    stack=[]
    for i in range(n):
        if vis[i]!=1:
            dfs(adj,i,stack,vis)
    return stack[::-1]

adj=[[2,4],[2],[],[1],[]]
n=5
print(topologicalsort(adj,n))