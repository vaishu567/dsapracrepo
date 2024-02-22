def bfsonmatrix(mat,i,j,vis,n,m):
    vis[i][j]=1
    to_visit=[(i, j)]
    while to_visit:
        row, col=to_visit.pop(0)
        for delrow in range(-1,2):
            for delcol in range(-1,2):
                nrow=row+delrow
                ncol=col+delcol
                if (0<=nrow<n) and (0<=ncol<m) and mat[nrow][ncol]!=0 and vis[nrow][ncol]!= 1:
                    vis[nrow][ncol]=1
                    to_visit.append((nrow,ncol))
    return vis

def numofisl(grid):
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for i in range(m)]for j in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if vis[i][j]!=1 and grid[i][j]==1:
                count+=1
                vis=bfsonmatrix(grid,i,j,vis,n,m)
    return count

grid=[[0,1,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,0],[1,1,0,1]]
# grid=[[0,1],[1,0],[1,1],[1,0]]
# grid=[[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
print(numofisl(grid))

        
    # vis[node]=1
    # dfsa.append(node)
    # for neighbour in adj[node]:
    #     if vis[neighbour]!=1:
    #         dfsa=dfs(neighbour,adj,vis,dfsa)
    # return dfsa
# //////////no of islands using dfs:
def dfsonmatrix(mat,i,j,vis,n,m):
    vis[i][j]=1
    for delrow in range(-1,2):
        for delcol in range(-1,2):
            row=i+delrow
            col=j+delcol
            if (0<=row<n and 0<=col<m) and vis[row][col]!=1 and mat[row][col]==1:
                vis=dfsonmatrix(mat,row,col,vis,n,m)
    return vis
def numofisl(grid):
    n=len(grid)
    m=len(grid[0])
    vis=[[0 for i in range(m)]for j in range(n)]
    count=0
    for i in range(n):
        for j in range(m):
            if vis[i][j]!=1 and grid[i][j]==1:
                count+=1
                vis=dfsonmatrix(grid,i,j,vis,n,m)
    return count
grid=[[0,1,1,0],[0,1,1,0],[0,0,1,0],[0,0,0,0],[1,1,0,1]]
# grid=[[0,1],[1,0],[1,1],[1,0]]
# grid=[[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
print(numofisl(grid))