# here originally we use priorty queue:
import heapq
def dijkstrapq(adj,n,src):
    dist=[float('inf') for _ in range(n)]
    dist[src]=0
    minheap=[(dist[src],src)]
    while minheap:
        d,node=heapq.heappop(minheap)
        for neighbour in adj[node]:
            adjw=neighbour[1]
            adjnode=neighbour[0]
            if (d+adjw) < dist[adjnode]:
                dist[adjnode]=min(dist[adjnode],d+adjw)
                heapq.heappush(minheap,(dist[adjnode],adjnode))
    return dist
print(dijkstrapq(adj,n,src))

