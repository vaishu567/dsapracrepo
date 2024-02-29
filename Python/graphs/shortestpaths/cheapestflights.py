def cheapestflights(flights,src,dst,k):
    adjmat=[[]]
    for edge in flights:
        u,v,w=edge[0],edge[1],edge[2]
        adjmat[u].append([v,w])
    n=len(adjmat)
    dist=[float('inf') for i in range(n)]
    dist[src]=0
    to_visit=[]
    # steps,node,dist
    to_visit.append((0,src,0))
    while to_visit:
        steps,node,cost=to_visit.pop(0)
        if steps>k:
            continue
        for negibour in adjmat[node]:
            adjnode=negibour[0]
            adjw=negibour[1]
            if cost+adjw<dist[adjnode] and steps<=k:
                dist[adjnode]=cost+adjw
                to_visit.append((steps+1,adjnode,dist[adjnode]))
    if dist[dst]==float('inf'):
        return -1