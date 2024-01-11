# we need to find unique paths to reach from mat[0][0] to mat[n-1][m-1]
# recursion:
# TIME COMPLEXITY WILL BE EXPONENTIAL BECAUSE FOR EVERY CALL WE ARE MOVING RIGHT AND DOWN 2ways:
# T.C=O(2**(N*M))
# S.C=O(path length)
# path length usually is m-1+n-1
def findUniquePath(right,down,row,col,n,m):
    if row==n-1 and col==m-1:
        return 1
    if col>m-1 or row>n-1:
        return 0
    # movingright:
    right=findUniquePath(right,down,row,col+1,n,m)
    down=findUniquePath(right,down,row+1,col,n,m)
    return right+down
# mat=[[2,2],[1,1]]
n=2
m=2
right=0
down=0
col=0
row=0
print(findUniquePath(right,down,row,col,n,m))

# Memoization:
# T.C=O(n*m)
# S.C=O((n-1)+(m-1))+O(n*m)
def memoization(right,down,row,col,n,m,dp):
    if row==n-1 and col==m-1:
        return 1
    if col>m-1 or row>n-1:
        return 0
    if dp[row][col]!=-1:
        return dp[row][col]
    right=memoization(right,down,row,col+1,n,m,dp)
    down=memoization(right,down,row+1,col,n,m,dp)
    dp[row][col]=right+down
    return dp[row][col]


n=1
m=6
dp=[[-1 for _ in range(m)] for _ in range(n)]
print(dp)
right=0
down=0
col=0
row=0
print(memoization(right,down,row,col,n,m,dp))



# tabulation:
