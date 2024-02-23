def dfs(mat,i,j,n,m,vis):
    vis[i][j]=1
    delta=[-1,1]
    for d in delta:
        row=i+d
        col=j+d
        if 0<=row<n and mat[row][j]==1 and vis[row][j]==0:
            vis=dfs(mat,row,j,n,m,vis)
        if 0<=col<m and mat[i][col]==1 and vis[i][col]==0:
            vis=dfs(mat,i,col,n,m,vis)
    return vis
def numberofenclaves(mat,n,m):
    loop_n=[0,n-1]
    loop_m=[0,m-1]
    vis=[[0 for _ in range(m)]for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i in loop_n or j in loop_m) and mat[i][j] == 1:
                vis = dfs(mat, i, j, n, m, vis)
    count = 0
    count=0
    for i in range(n):
        for j in range(m):
            if vis[i][j]==0 and mat[i][j]==1:
                count+=1
    return count
grid = [[0,0,1,1,1,0,1,1,1,0,1],[1,1,1,1,0,1,0,1,1,0,0],[0,1,0,1,1,0,0,0,0,1,0],[1,0,1,1,1,1,1,0,0,0,1],[0,0,1,0,1,1,0,0,1,0,0],[1,0,0,1,1,1,0,0,0,1,1],[0,1,0,1,1,0,0,0,1,0,0],[0,1,1,0,1,0,1,1,1,0,0],[1,1,0,1,1,1,0,0,0,0,0],[1,0,1,1,0,0,0,1,0,0,1]]
n=len(grid)
m=len(grid[0])
print(numberofenclaves(grid,n,m))