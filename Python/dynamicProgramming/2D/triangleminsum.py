def trianglesum(mat,diagonal,down,row,col,n):
    if row==n-1:
        return mat[row][col]
    if col>len(mat[row])-1 or row>n-1:
        return float('inf')
    # movingright:
    # if col<len(mat[row+1]):
    diagonal=mat[row][col]+trianglesum(mat,diagonal,down,row+1,col+1,n)
    down=mat[row][col]+trianglesum(mat,diagonal,down,row+1,col,n)
    # print(diagonal,down)
    return min(diagonal,down)
mat=[[1], [2,3], [3,6,7], [8,9,6,1]]
n=len(mat)
diagonal=0
down=0
print(trianglesum(mat,diagonal,down,0,0,n))


# memoization:
def memoization(mat, diagonal,down,row,col,n,dp):
    if row==n-1:
        return mat[row][col]
    if dp[row][col]!=-1:
        return dp[row][col]
    diagonal=mat[row][col]+memoization(mat,diagonal,down,row+1,col+1,n,dp)
    down=mat[row][col]+memoization(mat,diagonal,down,row+1,col,n,dp)
    dp[row][col]=min(diagonal,down)
    return dp[row][col]
def main(mat,n):
    diagonal=0
    down=0
    dp=[]
    for i in range(n):
        temp=[-1 for _ in range(i+1)]
        dp.append(list(temp))

    # dp=[[-1 for i in range(n)] for _ in range(n)]
    # print(dp)
    # return dp
    return memoization(mat, diagonal,down,0,0,n,dp)

mat=[[1], [2,3], [3,6,7], [8,9,6,1]]
n=len(mat)
print(main(mat,n))


# tabulation:
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
    return dp[0][0]
mat=[[1], [2,3], [3,6,7], [8,9,6,1]]
n=len(mat)
print(tabulation(mat,n))

                



    
    
    

