
def aliendict(dict,n,k):
    adj=[[] for _ in range(k)]
    indegree=[0 for i in range(k)]
    to_visit=[]
    topo=[]
    alpha=[chr(i) for i in range(97,k+97)]
    for i in range(n-1):
        s1=dict[i]
        s2=dict[i+1]
        leni=min(len(s1),len(s2))
        for ptr in range(leni):
            if s1[ptr]!=s2[ptr]:
                nodeu=ord(s1[ptr])-ord('a')
                nodev=ord(s2[ptr])-ord('a')
                adj[nodeu].append(nodev)
                indegree[nodev]+=1
                break
    for i in range(k):
        if indegree[i]==0:
            to_visit.append(i)
    while to_visit:
        node=to_visit.pop(0)
        topo.append(alpha[node])
        for neighbour in adj[node]:
            indegree[neighbour]-=1
            if indegree[neighbour]==0:
                to_visit.append(neighbour)
    return topo
    
dict=["baa","abcd","abca","cab","cad"]
n=len(dict)
k=4
print(aliendict(dict,n,k))


