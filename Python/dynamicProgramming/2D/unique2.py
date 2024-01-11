def findUniquePath(mat,right,down,row,col,n,m):
    if row==n-1 and col==m-1:
        if mat[row][col]!=-1:
            return 1
        return 0
    if col>m-1 or row>n-1:
        return 0
    # movingright:
    if mat[row][col]!=-1:
        right=findUniquePath(mat,right,down,row,col+1,n,m)
        down=findUniquePath(mat,right,down,row+1,col,n,m)
        return right+down
    else:
        return 0
mat=[[2,-1],[-1,1]]
n=2
m=2
right=0
down=0
col=0
row=0
print(findUniquePath(mat,right,down,row,col,n,m))

# memoization:
def memoization(mat,right,down,row,col,n,m,dp):
    if row==n-1 and col==m-1:
        if mat[row][col]!=-1:
            return 1
        return 0
    if col>m-1 or row>n-1:
        return 0
    if dp[row][col]!=0:
        return dp[row][col]
    if mat[row][col]!=-1:
        right=memoization(mat,right,down,row,col+1,n,m,dp)
        down=memoization(mat,right,down,row+1,col,n,m,dp)
        dp[row][col]=right+down
        print(dp)
    return dp[row][col]

mat=[[2,2,0],[2,-1,1],[2,2,0]]
n=len(mat)
m=len(mat[0])
right=0
down=0
col=0
row=0
dp=[[0 for _ in range(m)]for _ in range(n)]
print(memoization(mat,right,down,row,col,n,m,dp))

# tabulation:
def tabulation(mat,n,m):
    dp=[[0 for _ in range(m+1)]for _ in range(n+1)]
    for row in range(n-1,-1,-1):
        for col in range(m-1,-1,-1):
            if row==n-1 and col==m-1:
                if mat[row][col]!=-1:
                    dp[n-1][m-1]=1
            else:
                if mat[row][col]!=-1:
                # right=memoization(mat,right,down,row,col+1,n,m,dp)
                    right=dp[row][col+1]
                # down=memoization(mat,right,down,row+1,col,n,m,dp)
                    down=dp[row+1][col]
                    dp[row][col]=right+down
    return dp[0][0]
mat=[[2,2,0],[2,-1,1],[2,2,0]]
n=len(mat)
m=len(mat[0])
print(tabulation(mat,n,m))



