# def maxchocolates(mat,row,col,n,m,last):
#     if col<0 or col>m-1:
#         return 0
#     if row==n-1:
#         if row!=last:
#             last=row
#             return mat[n-1][col]
#         return 0
        
    
#     d=mat[row][col]
#     mat[row][col]=0
#     down=d+maxchocolates(mat,row+1,col,n,m,last)
#     dleft=d+maxchocolates(mat,row+1,col-1,n,m,last)
#     dright=d+maxchocolates(mat,row+1,col+1,n,m,last)
#     # print(dleft,dright,down)
#     return max(dleft,dright,down)

# def main(mat,n,m):
#     last=m+n
#     alice=maxchocolates(mat,0,0,n,m,last)
#     print(mat)
#     bob=maxchocolates(mat,0,m-1,n,m,last)
#     print(mat)
#     return bob+alice
# mat=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
# n=len(mat)
# m=len(mat[0])
# print(main(mat,n,m))


# here we need to write recurssion in one function only:
# basically we can take i1,j1 for alice and i2,j2 for bob but since they will move simutaneously we can take only one i 
# also for every moment of alice there can be 3 moments of bob:
# t.c= 3**n x 3**n
# s.c=0(n) auxialry stack space:
def maxchocolates(mat,row,col1,col2,n,m):
    # for base case:
    # 1 overbound:
    if (col1<0 or col1>m-1) or (col2<0 or col2>m-1):
        return float('-inf')
    # 2 destination:
    if row==n-1:
        if col1==col2:
            return mat[row][col1]
        else:
            return mat[row][col1]+mat[row][col2]
    maxi=float('-inf')
    for dj1 in range(-1,2,1):
        for dj2 in range(-1,2,1):
            if col1==col2:
                value=mat[row][col1]
            else:
                value=mat[row][col1]+mat[row][col2]
            value+=maxchocolates(mat,row+1,col1+dj1,col2+dj2,n,m)
            maxi=max(maxi,value)
    return maxi
mat=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
n=len(mat)
m=len(mat[0])
print(maxchocolates(mat,0,0,m-1,n,m))


# memoization:
# here we need to create a 3d vector to do dp:
# T.C=O(N*M*M) *9
# S.C=O(N*M*M) + O(N)
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