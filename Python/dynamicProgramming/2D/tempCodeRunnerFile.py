def tabulation(mat,n):
    diagonal=0
    down=0
    dp=[]
    for i in range(n):
        temp=[0 for _ in range(i+1)]
        dp.append(list(temp))
    for j in range(n):
        dp[n-1][j]=mat[n-1][j]

    for row in range(n-2,-1,-1):
        for col in range(row+1):
            # if row==n-1:
            #     dp[row][col]=mat[row][col]
            
            diagonal=mat[row][col]+dp[row+1][col+1]
            down=mat[row][col]+dp[row+1][col]
            dp[row][col]=min(diagonal,down)
    return dp
mat=[[1], [2,3], [3,6,7], [8,9,6,1]]
n=len(mat)
print(tabulation(mat,n))