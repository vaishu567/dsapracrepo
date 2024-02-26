# in this question they have given edges in the form of pre-requisites
# so first we need to create the adj list:
def courseschedule(prerequisites,n):
    adj=[[] for _ in range(n)]
    for edge in prerequisites:
        u,v=edge[0],edge[1]
        adj[u].append(v)
    to_visit=[]
    topo=[]
    indegree=[0 for i in range(n)]
    for i in range(n):
        for node in adj[i]:
            indegree[node]+=1
    for i in range(n):
        if indegree[i]==0:
            to_visit.append(i)
    while to_visit:
        node=to_visit.pop(0)
        topo.append(node)
        for i in adj[node]:
            indegree[i]-=1
            if indegree[i]==0:
                to_visit.append(i)
    if len(topo)==n:
        return 1
    return 0

prereq=[[1,0],[2,0],[3,1],[3,2]]
n=len(prereq)
print(courseschedule(prereq,n))
