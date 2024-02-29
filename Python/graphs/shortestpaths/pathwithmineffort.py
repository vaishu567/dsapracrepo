# we have to use PQ coz graph with weighted so:
import heapq as pq

def pathwithmineffort(mat):
    n=len(mat)
    m=len(mat[0])
    delta=[(0,1),(1,0),(0,-1),(-1,0)]
    dist=[[float("inf") for _ in range(m)] for _ in range(n)]
    dist[0][0]=0
    to_visit=[(0,(0,0))]
    while to_visit:
        w,node=pq.heappop(to_visit)
        row=node[0]
        col=node[1]
        # we are checking here beacuse pq gives min (max_diffs) value so when r==n-1 and col==n-1 it gives min diff vlaues
        if row==n-1 and col==m-1:
            return w
        for delr,delc in delta:
            newr=row+delr
            newc=col+delc
            if 0<=newr<n and 0<=newc<m:
                # diff here is max effort in that path
                diff=max(w,abs(mat[row][col]-mat[newr][newc]))  
                # since its dijkstra algo wie will always store min of diff in dist mat 
                if diff<dist[newr][newc]:
                    dist[newr][newc]=diff
                    pq.heappush(to_visit,(diff,(newr,newc)))
                # remember that we are carrying max effort not dist in pq
    return -1

heights = [[1, 8, 8],[3, 8, 9],[5,3,5]]

print(pathwithmineffort(heights))