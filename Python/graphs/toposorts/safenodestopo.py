def eventualSafeNodes(n, adj):
    # code here
    adjrev=[[] for i in range(n)]
    indegree=[0 for i in range(n)]
    safenodes=[]
    to_visit=[]
    for i in range(n):
        for neighbour in adj[i]:
            adjrev[neighbour].append(i)
            indegree[i]+=1
    for i in range(n):
        if indegree[i]==0:
            to_visit.append(i)
    while to_visit:
        node=to_visit.pop(0)
        safenodes.append(node)
        for neighbour in adjrev[node]:
            indegree[neighbour]-=1
            if indegree[neighbour]==0:
                to_visit.append(neighbour)
                
    safenodes.sort()
    return safenodes  