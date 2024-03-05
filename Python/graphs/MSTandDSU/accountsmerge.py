def accountsmerger(accounts,n):
    nodeindexmap={}
    parent=[i for i in range(n+1)]
    rank=[0 for i in range(n+1)]
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
    # original code :
    # first we are mapping the mails with their respective nodes:
    for i in range(n):
        for j in range(1,len(accounts[i])):
            mail=accounts[i][j]
            if mail not in nodeindexmap:
                nodeindexmap[mail]=i
            else:
                unionbyrank(i,nodeindexmap[mail])
    mergedmail=[[] for i in range(len(nodeindexmap))]
    for it in nodeindexmap:
        strmail=it
        node=nodeindexmap[it]
        parnode=findUlparent(parent,node)
        mergedmail[parnode].append(strmail)
    # return mergedmail
    ans=[]
    for i in range(n):
        if len(mergedmail[i])==0:
            continue
        mergedmail[i].sort()
        temp=[]
        temp.append(accounts[i][0])
        for it in mergedmail[i]:
            temp.append(it)
        ans.append(list(temp))
    return ans




accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
print(accountsmerger(accounts,len(accounts)))