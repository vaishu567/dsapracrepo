def recursivemaxpath(mat,row,col,n,m):
    if col<0 or col>=m:
        return float('-inf')
    if row==n-1:
        return mat[n-1][col]
    down=mat[row][col]+recursivemaxpath(mat,row+1,col,n,m)
    dgleft=mat[row][col]+recursivemaxpath(mat,row+1,col-1,n,m)
    dgright=mat[row][col]+recursivemaxpath(mat,row+1,col+1,n,m)
    return max(dgleft,max(dgright,down))
def main(mat,n,m):
    finmaxi=float('-inf')
    for col in range(m):
        maxi=recursivemaxpath(mat,0,col,n,m)
        finmaxi=max(maxi,finmaxi)
    return finmaxi
mat=[[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
n=len(mat)
m=len(mat[0])
print(main(mat,n,m))


# memoization:
def recursivemaxpath(mat,row,col,n,m,dp):
    if col<0 or col>=m:
        return float('-inf')
    if row==n-1:
        return mat[n-1][col]
    if dp[row][col]!=-1:
        return dp[row][col]
    down=mat[row][col]+recursivemaxpath(mat,row+1,col,n,m,dp)
    dgleft=mat[row][col]+recursivemaxpath(mat,row+1,col-1,n,m,dp)
    dgright=mat[row][col]+recursivemaxpath(mat,row+1,col+1,n,m,dp)
    dp[row][col]=max(dgleft,max(dgright,down))
    return dp[row][col]
def main(mat,n,m):
    finmaxi=float('-inf')
    dp=[[-1 for i in range(m)] for j in range(n)]
    for col in range(m):
        maxi=recursivemaxpath(mat,0,col,n,m,dp)
        finmaxi=max(maxi,finmaxi)
    return finmaxi


mat=[[1,2,10,4],[100,3,2,1],[1,1,20,2],[1,2,2,1]]
n=len(mat)
m=len(mat[0])
print(main(mat,n,m))

# tabulation:
def main(mat,n,m):
    finmaxi=float('-inf')
    dp=[[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        dp[n-1][j]=mat[n-1][j]
    for row in range(n-2,-1,-1):
        for col in range(m):
            down=mat[row][col]+dp[row+1][col]
            if col-1>=0:
                dgleft=mat[row][col]+dp[row+1][col-1]
            else:
                dgleft=float('-inf')
            if col+1<m:
                dgright=mat[row][col]+dp[row+1][col+1]
            else:
                dgright=float('-inf')

            dp[row][col]=max(dgleft,dgright,down)
        # finmaxi=max(maxi,finmaxi)

    return dp
    # for i in range(m):
    #     finmaxi=max(dp[0][i],finmaxi)
    # return finmaxi

mat=[[2,1,3],[6,5,4],[7,8,9]]
n=len(mat)
m=len(mat[0])
print(main(mat,n,m))



s="vaishnavi"
print(int(s))