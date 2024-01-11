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