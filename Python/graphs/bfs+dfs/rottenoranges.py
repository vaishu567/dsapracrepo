# to solve this we should use bfs only becoz if we use dfs it does depth wise search and returns maximum time but here we want max(min(time))
def rottenoranges(grid, n, m):
    time=-1
    to_visit=[]
    vis=[[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j]==2 and vis[i][j]!=2:
                to_visit.append(((i,j),0))
                vis[i][j]=2
    if not to_visit:
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    return -1
        return 0
    while to_visit:
        (row,col),t=to_visit.pop(0)
        delta=[-1,1]
        time=max(time,t)
        for i in delta:
            delrow=row+i
            delcol=col+i
            if 0<=delrow<n and grid[delrow][col]==1 and vis[delrow][col]!=2:
                to_visit.append(((delrow,col),t+1))
                vis[delrow][col]=2
                grid[delrow][col]=2
            if 0<=delcol<m and grid[row][delcol]==1 and vis[row][delcol]!=2:
                to_visit.append(((row,delcol),t+1))
                vis[row][delcol]=2
                grid[row][delcol]=2
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1:
                return -1
    return time
grid=[[2,1,1],[1,1,0],[0,1,1]]
n=3
m=3
print(rottenoranges(grid,n,m))