def networkdelay(edges,n,k):
    adj=[[] for _ in range(n+1)]
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        adj[u].append([v,w])
    dist=[float('inf') for _ in range(n+1)]
    to_visit=[]
    dist[k]=0
    # k is src and we are appending time,k
    to_visit.append((0,k))
    while to_visit:
        time,node=to_visit.pop(0)
        for neighbour in adj[node]:
            adjnode=neighbour[0]
            adjw=neighbour[1]
            if time+adjw<dist[adjnode]:
                dist[adjnode]=time+adjw
                to_visit.append((dist[adjnode],adjnode))
    maxi=max(dist[1:])
    if maxi==float('inf'):
        return -1
    else:
        return maxi