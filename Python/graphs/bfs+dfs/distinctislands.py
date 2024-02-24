def dfs(mat,i,j,vis,temp,n,m,row0,col0):
    vis[i][j]=1
    delta=[-1,1]
    temp.append((i-row0,j-col0))
    for d in delta:
        row=i+d
        col=j+d
        if 0<=row<n and mat[row][j]==1 and vis[row][j]==0:
            temp=dfs(mat,row,j,vis,temp,n,m,row0,col0)
        if 0<=col<m and mat[i][col]==1 and vis[i][col]==0:
            temp=dfs(mat,i,col,vis,temp,n,m,row0,col0)
    return temp
def distinctislands(mat,n,m):
    vis=[[0 for _ in range(m)]for _ in range(n)]
    s=set()
    for i in range(n):
        for j in range(m):
            if mat[i][j]==1 and vis[i][j]!=1:
                temp=[]
                temp=dfs(mat,i,j,vis,temp,n,m,i,j)
                s.add(tuple(temp))
    return len(s)
# grid = [[1, 1, 0, 0, 0],
#             [1, 1, 0, 0, 0],
#             [0, 0, 0, 1, 1],
#             [0, 0, 0, 1, 1]]
grid=[[1, 1, 0, 1, 1],
            [1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [1, 1, 0, 1, 1]]
n=len(grid)
m=len(grid[0])
print(distinctislands(grid,n,m))
