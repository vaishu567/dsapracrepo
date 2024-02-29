import heapq
def shortestpath(adj,n,src):
    mindistheap=[]
    heapq.heappush(mindistheap,(0,src))
    dist=[float("inf") for _ in range(n+1)]
    parent=[i for i in range(n+1)]
    while mindistheap:
        d,node=heapq.heappop(mindistheap)
        for neighbour in adj[node]:
            adjw=neighbour[1]
            adjnode=neighbour[0]
            if d+adjw<dist[adjnode]:
                parent[adjnode]=node
                dist[adjnode]=d+adjw
                heapq.heappush(mindistheap,(dist[adjnode],adjnode))
    node=n
    ans=[]
    while parent[node]!=node:
        ans.append(node)
        node=parent[node]
    ans.append(src)
    return ans


