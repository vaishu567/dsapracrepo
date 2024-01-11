def tabulation(mat,n,m):
    dp=[[float("inf") for _ in range(m+1)] for _ in range(n+1)]
    for row in range(n-1,-1,-1):
        for col in range(m-1,-1,-1):
            if row==n-1 and col==m-1:
                dp[row][col]=mat[row][col]
                # return dp[row][col]
            else:
                right=mat[row][col]+dp[row][col+1]
                down=mat[row][col]+dp[row+1][col]
                dp[row][col]=min(right,down)
    return dp[0][0]

mat=[[5,9,6],[11,5,2]]
n=len(mat)
m=len(mat[0])
print(tabulation(mat,n,m))