def nearestone(grid):
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for i in range(m)]for i in range(n)]
    dis=[[0 for i in range(m)]for i in range(n)]
    to_visit=[]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                to_visit.append(((i,j),0))
                vis[i][j]=1
    while to_visit:
        ((row,col),d)=to_visit.pop(0)
        dis[row][col]=d
        delta=[-1,1]
        for i in delta:
            delrow=row+i
            delcol=col+i
            if 0<=delrow<n and grid[delrow][col]==0 and vis[delrow][col]==0:
                vis[delrow][col]=1
                to_visit.append(((delrow,col),d+1))
            if 0<=delcol<m and grid[row][delcol]==0 and vis[row][delcol]==0:
                vis[row][delcol]=1
                to_visit.append(((row,delcol),d+1))

    return dis


    
