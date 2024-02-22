# flood fill using bfs:
def floodfill(x,y,mat,p,n,m,inp,vis):
    vis[x][y]=1
    to_visit=[(x,y)]
    mat[x][y]=p
    while to_visit:
        row,col=to_visit.pop(0)
        delta=[-1,1]
        for i in delta:
            delrow=row+i
            delcol=col+i
            if 0<=delrow<n and mat[delrow][col]==inp and vis[delrow][col]!=1:
                to_visit.append((delrow,col))
                vis[delrow][col]=1
                mat[delrow][col]=p
            if 0<=delcol<m and mat[row][delcol]==inp and vis[row][delcol]!=1:
                to_visit.append((row,delcol))
                vis[row][delcol]=1
                mat[row][delcol]=p
    return mat
mat=[[1,1,1],[2,2,0],[2,2,2]]
n=len(mat)
m=len(mat[0])
x=2
y=2
p=3
inp=mat[x][y]
vis=[[0 for i in range(m)]for i in range(n)]
print(floodfill(x,y,mat,p,n,m,inp,vis))


# def floodFill(mat: List[List[int]], n: int, m: int, x: int, y: int, p: int) -> List[List[int]]:
#     # write your code here
#     if mat[x][y]==p:
#         return mat
#     inp=mat[x][y]
#     vis=[[0 for i in range(m)]for i in range(n)]
#     vis[x][y]=1
#     to_visit=[(x,y)]
#     mat[x][y]=p
#     while to_visit:
#         row,col=to_visit.pop(0)
#         delta=[-1,1]
#         for i in delta:
#             delrow=row+i
#             delcol=col+i
#             if 0<=delrow<n and mat[delrow][col]==inp and vis[delrow][col]!=1:
#                 to_visit.append((delrow,col))
#                 vis[delrow][col]=1
#                 mat[delrow][col]=p
#             if 0<=delcol<m and mat[row][delcol]==inp and vis[row][delcol]!=1:
#                 to_visit.append((row,delcol))
#                 vis[row][delcol]=1
#                 mat[row][delcol]=p
#     return mat


# T.C:
# if n*m=x in worst case if they are all equal then for every node we check 4 directions so:
# T.C=O(x*4)
# S.C=O(vis arr)+O(to_visit)
# in worst case S.C=O(2(N*M))


# using dfs we can avoid using visited matrix becoz we can check of mat[i][j]==inp if its not then no need of checking it and already visited one we will change its color to p 
# thus we can avoid using visited matrix