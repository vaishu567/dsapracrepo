def mstkruskals(n,edges):
    # MlogM
    edges = sorted(edges, key=lambda x: x[2])
    parent=[i for i in range(n+1)]
    rank=[0 for i in range(n+1)]
    mstWt=0

    # findUparent:
    def findUlparent(parent,x):
        if x==parent[x]:
            return x
        return findUlparent(parent,parent[x])
    def unionbyrank(u,v):
        ulpu=findUlparent(parent,u)
        ulpv=findUlparent(parent,v)
        if rank[ulpu]<rank[ulpv]:
            parent[ulpu]=ulpv
        elif rank[ulpv]<rank[ulpu]:
            parent[ulpv]=ulpu
        else:
            parent[ulpv]=ulpu
            rank[ulpu]+=1
    # O(4^alpha) * M
    
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        if findUlparent(parent,u)!=findUlparent(parent,v):
            mstWt+=w
            unionbyrank(u,v)
    return mstWt
# so T.C=O(MlogM+M(4*alpha))