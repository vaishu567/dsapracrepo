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