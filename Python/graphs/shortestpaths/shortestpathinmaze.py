def binarymaze(mat,src,dest):
    sr,sc=src
    dr,dc=dest
    if src==dest and mat[sr][sc]==1:
        return 0
    elif src==dest and mat[sr][sc]==0:
        return -1
    to_visit=[]
    n=len(mat)
    m=len(mat[0])
    delta=[(0,1),(1,0),(0,-1),(-1,0)]
    dist=[[float("inf") for _ in range(m)] for _ in range(n)]
    dist[sr][sc]=0
    to_visit.append([sr,sc])
    while to_visit:
        node=to_visit.pop(0)
        row=node[0]
        col=node[1]
        for delr,delc in delta:
            newr=row+delr
            newc=col+delc
            if 0<=newr<n and 0<=newc<m and mat[newr][newc]==1:
                newval=dist[row][col]+1
                curr=dist[newr][newc]
                if newr==dr and newc==dc:
                    return min(newval,curr)
                if newval<curr:
                    dist[newr][newc]=newval
                    to_visit.append([newr,newc])

    return -1


# for 8 direction:
        # n=len(mat)
        # sr,sc=0,0
        # dr,dc=n-1,n-1
        # if mat[sr][sc]==1 or mat[n-1][n-1]==1:
        #     return -1
        # if n==1:
        #     return 1
        # to_visit=[]
        # n=len(mat)
        # m=len(mat[0])
        # delta=[(0,1),(1,0),(1,1),(0,-1),(-1,1),(1,-1),(-1,0),(-1,-1)]
        # dist=[[float("inf") for _ in range(n)] for _ in range(n)]
        # dist[sr][sc]=1
        # to_visit.append([sr,sc])
        # while to_visit:
        #     node=to_visit.pop(0)
        #     row=node[0]
        #     col=node[1]
        #     for delr,delc in delta:
        #         newr=row+delr
        #         newc=col+delc
        #         if 0<=newr<n and 0<=newc<n and mat[newr][newc]==0:
        #             newval=dist[row][col]+1
        #             curr=dist[newr][newc]
        #             if newr==dr and newc==dc:
        #                 return min(newval,curr)
        #             if newval<curr:
        #                 dist[newr][newc]=newval
        #                 to_visit.append([newr,newc])

        # return -1
