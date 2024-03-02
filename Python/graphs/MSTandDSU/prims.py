import heapq as pq
def prims(n,m,edges):
    adj=[[] for i in range(n)]
    for edge in edges:
        u,v,w=edge[0],edge[1],edge[2]
        adj[u].append([v,w])
        adj[v].append([u,w])
    mst=[]
    sumofmst=0
    vis=[0 for i in range(n)]
    # (wt,node,parent)
    to_visit=[(0,0,-1)]
    while to_visit:
        w,node,parent=pq.heappop(to_visit)
        if vis[node]==1:
            continue
        vis[node]=1
        # we are adding to sum after popping out of minheap becoz we only need min sum
        sumofmst+=w
        if parent!=-1:
            mst.append((parent,node))
        for neighbour in adj[node]:
            adjnode=neighbour[0]
            adjw=neighbour[1]
            if vis[adjnode]==1:
                continue
            elif vis[adjnode]==0:
                pq.heappush(to_visit,(adjw,adjnode,node))
    return mst
            

            


