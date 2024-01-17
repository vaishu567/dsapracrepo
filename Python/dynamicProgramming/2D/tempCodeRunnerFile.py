def maxchocolates(mat,row,col,n,m):
    if col<0 or col>m-1:
        return 0
    if row==n-1:
        return mat[n-1][col]
    d=mat[row][col]
    mat[row][col]=0
    down=d+maxchocolates(mat,row+1,col,n,m)
    dleft=d+maxchocolates(mat,row+1,col-1,n,m)
    dright=d+maxchocolates(mat,row+1,col+1,n,m)
    # print(dleft,dright,down)
    return max(dleft,dright,down)

def main(mat,n,m):
    alice=maxchocolates(mat,0,0,n,m)
    print(mat)
    bob=maxchocolates(mat,0,m-1,n,m)
    print(bob)
    return bob+alice
mat=[[2,3,1,2],[3,4,2,2],[5,6,3,5]]
n=len(mat)
m=len(mat[0])
print(main(mat,n,m))