def floydWarshall(n, m, src, dest, edges):
    maxi=1000000000
    cost=[[maxi for i in range(n+1)] for _ in range(n+1)]
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        cost[u][v]=w
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                cost[i][j]=0


    for via in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if cost[i][via]!=maxi and cost[j][via]!=maxi:
                    cost[i][j]=min((cost[i][via]+cost[via][j]),cost[i][j])
    return cost[src][dest]
