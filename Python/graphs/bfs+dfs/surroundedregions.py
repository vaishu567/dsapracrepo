# here we first perform boundary O's check by traversing


def dfs(mat,i,j,vis,n,m):
    vis[i][j]=1
    delta=[-1,1]
    for d in delta:
        row=i+d
        col=j+d
        if 0<=row<n and vis[row][j]!=1 and mat[row][j]=='O':
            vis=dfs(mat,row,j,vis,n,m)
        if 0<=col<m and vis[i][col]!=1 and mat[i][col]=='O':
            vis=dfs(mat,i,col,vis,n,m)
    return vis
def surrounded(mat):
    n=len(mat)
    m=len(mat[0])
    vis=[[0 for _ in range(m)]for _ in range(n)]
    boun=[0,n-1]
    boum=[0,m-1]
    for i in boun:
        for j in range(m):
            if mat[i][j]=='O' and vis[i][j]!=1:
                vis=dfs(mat,i,j,vis,n,m)
    for j in boum:
        for i in range(n):
            if mat[i][j]=='O' and vis[i][j]!=1:
                vis=dfs(mat,i,j,vis,n,m)
    for i in range(n):
        for j in range(m):
            if vis[i][j]==0:
                vis[i][j]='X'
            else:
                vis[i][j]='O'
    return vis
board =[["X","O","X","O","X","O"],["O","X","O","X","O","X"],["X","O","X","O","X","O"],["O","X","O","X","O","X"]]
print(surrounded(board))