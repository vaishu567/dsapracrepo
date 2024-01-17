def maxchocolates(mat,row,col1,col2,n,m,dp):
    if (col1<0 or col1>m-1) or (col2<0 or col2>m-1):
        return float('-inf')
    if row==n-1:
        if col1==col2:
            return mat[row][col1]
        else:
            return mat[row][col1]+mat[row][col2]
    if dp[row][col1][col2]!=-1:
        return dp[row][col1][col2]
    maxi=float('-inf')
    for dj1 in range(-1,2,1):
        for dj2 in range(-1,2,1):
            if col1==col2:
                value=mat[row][col1]
            else:
                value=mat[row][col1]+mat[row][col2]
            value+=maxchocolates(mat,row+1,col1+dj1,col2+dj2,n,m,dp)
            maxi=max(maxi,value)
    dp[row][col1][col2]=maxi
    return dp[row][col1][col2]
mat=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
n=len(mat)
m=len(mat[0])
dp=[[[-1 for i in range(m)] for i in range(m)] for i in range(n)]
print(maxchocolates(mat,0,0,m-1,n,m,dp))   
    




def maximumChocolates(n, m, mat):
    # write your code here
    dp=[[[0 for i in range(m)] for i in range(m)] for i in range(n)]
    # return maxchocolates(mat,0,0,m-1,n,m,dp)
    # base case: 
    for j1 in range(m):
        for j2 in range(m):
            if j1==j2:
                dp[n-1][j1][j2]=mat[n-1][j1]
            else:
                dp[n-1][j1][j2]=mat[n-1][j1]+mat[n-1][j2]
    for row in range(n-2,-1,-1):
        for col1 in range(m):
            for col2 in range(m):
                maxi=float('-inf')
                for dj1 in range(-1,2,1):
                    for dj2 in range(-1,2,1):
                        value=0
                        if col1==col2:
                            value=mat[row][col1]
                        else:
                            value=mat[row][col1]+mat[row][col2]
                        if (col1+dj1<0 or col1+dj1>=m) or (col2+dj2<0 or col2+dj2>=m):
                            value+=float('-inf')
                        else:
                            value+=dp[row+1][col1+dj1][col2+dj2]
                        maxi=max(maxi,value)
                dp[row][col1][col2]=maxi
    return dp[0][0][m-1]
    

mat=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
n=len(mat)
m=len(mat[0])
print( maximumChocolates(n,m,mat))  