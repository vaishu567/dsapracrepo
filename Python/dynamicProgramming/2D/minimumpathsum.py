def minsumpath(mat,right,down,row,col,n,m):
    if row==n-1 and col==m-1:
        return mat[row][col]
    if col>m-1 or row>n-1:
        return float('inf')
    # movingright:
    right=mat[row][col]+minsumpath(mat,right,down,row,col+1,n,m)
    down=mat[row][col]+minsumpath(mat,right,down,row+1,col,n,m)
    # print(right,down)
    return min(right,down)
mat=[[5,9,6],[11,5,2]]
n=len(mat)
m=len(mat[0])
right=0
down=0
col=0
row=0
print(minsumpath(mat,right,down,row,col,n,m))



# Memoization:
def minsumpath(mat,right,down,row,col,n,m,dp):
    if row==n-1 and col==m-1:
        return mat[row][col]
    if col>m-1 or row>n-1:
        return float('inf')
    if dp[row][col]!=-1:
        return dp[row][col]
    right=mat[row][col]+minsumpath(mat,right,down,row,col+1,n,m,dp)
    down=mat[row][col]+minsumpath(mat,right,down,row+1,col,n,m,dp)
    dp[row][col]=min(right,down)
    print(dp)
    return dp[row][col]

    
mat=[[5,9,6],[11,5,2]]
n=len(mat)
m=len(mat[0])
right=0
down=0
col=0
row=0
dp=[[-1 for _ in range(m)] for _ in range(n)]
print(minsumpath(mat,right,down,row,col,n,m,dp))
