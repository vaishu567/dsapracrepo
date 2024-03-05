def numberofprovinces(adjmat,n):
    rank=[0 for i in range(n)]
    parent=[i for i in range(n)]
    def findUlparent(parent,x):
        if x==parent[x]:
            return x
        return findUlparent(parent,parent[x])
    def unionbyrank(parent,u,v):
        ulpu=findUlparent(parent,u)
        ulpv=findUlparent(parent,v)
        if ulpu==ulpv:
            return
        if rank[ulpu]<rank[ulpv]:
            parent[ulpu]=ulpv
        elif rank[ulpv]<rank[ulpu]:
            parent[ulpv]=ulpu
        else:
            parent[ulpv]=ulpu
            rank[ulpu]+=1
    for i in range(n):
        for j in range(n):
            if adjmat[i][j]==1:
                unionbyrank(parent,i,j)
    cnt=0
    for i in range(n):
        if findUlparent(parent,i)==i:
            cnt+=1
    return cnt
