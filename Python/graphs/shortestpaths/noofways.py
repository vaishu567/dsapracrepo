
import heapq as pq
def noofways(n,m,edges):
    mod=(10**9)+7
    adj=[[] for i in range(n)]
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        adj[u].append([v,w])
        adj[v].append([u,w])
    ways=[0 for i in range(n)]
    dist=[float('inf') for i in range(n)]
    dist[0]=0
    ways[0]=1
    to_visit=[(0,0)]
    while to_visit:
        d,node=pq.heappop(to_visit)
        for neighbour in adj[node]:
            adjnode=neighbour[0]
            adjw=neighbour[1]
            # this is the first time i am coming with short distance:
            if d+adjw<dist[adjnode]:
                dist[adjnode]=d+adjw
                ways[adjnode]=ways[node]
                pq.heappush(to_visit,(dist[adjnode],adjnode))
            elif d+adjw==dist[adjnode]:
                ways[adjnode]=(ways[adjnode]+ways[node])%mod
    return ways[n-1]