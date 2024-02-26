def detectcycle(adj,n):
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
    if len(topo)==n:
        return True
    return False
adj=[[],[],[3],[1],[0,1],[0,2]]
n=len(adj)
print(detectcycle(adj,n))