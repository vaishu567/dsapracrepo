def findTheCity(n, edges, distanceThreshold):
    maxi=float('inf')
    cost=[[maxi for i in range(n)] for _ in range(n)]
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        cost[u][v]=w
        cost[v][u]=w
    for i in range(n):
        cost[i][i]=0


    for via in range(n):
        for i in range(n):
            for j in range(n):
                if cost[i][via]!=maxi and cost[via][j]!=maxi:
                    cost[i][j]=min((cost[i][via]+cost[via][j]),cost[i][j])
    cntmax=n
    city=-1
    for i in range(n):
        cnt=0
        for j in range(n):
            if cost[i][j]<=distanceThreshold:
                cnt+=1
        if cnt<=cntmax:
            cntmax=min(cntmax,cnt)
            city=i
    return city