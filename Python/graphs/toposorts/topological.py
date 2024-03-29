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


# topological sort using bfs:
# kahn's algo:
def khanalgo(adj,n):
    indegree=[0 for i in range(n)]
    for i in range(n):
        for neighbor in adj[i]:
            indegree[neighbor]+=1
    to_visit=[]
    for i in range(n):
        if indegree[i]==0:
            to_visit.append(i)
    topo=[]
    while to_visit:
        node=to_visit.pop(0)
        topo.append(node)
        # node is in our topo sort 
        # so we need to remove it from the indegree
        for neighbor in adj[node]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0:
                to_visit.append(neighbor)
    return topo
adj=[[],[],[3],[1],[0,1],[0,2]]
n=len(adj)
print(khanalgo(adj,n))