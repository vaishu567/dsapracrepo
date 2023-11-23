# spiral matrix:

def spiralMatrix(mat : List[List[int]]) -> List[int]:
    # Write your code here.
    n=len(mat)
    m=len(mat[0])
    top=0
    left=0
    right=m-1
    bottom=n-1
    l=[]
    while top<=bottom and left<=right:
        # move right:
        for i in range(left,right+1):
            l.append(mat[top][i])
        top+=1
        # move down:
        for i in range(top,bottom+1):
            l.append(mat[i][right])
        right-=1
        # move left:
        if top<=bottom:
            for i in range(right,left-1,-1):
                l.append(mat[bottom][i])
            bottom-=1
        # move up:
        if(left<=right):
            for i in range(bottom,top-1,-1):
                l.append(mat[i][left])
            left+=1
    return l


# set zero:
def zeroMatrix(matrix, n, m):
    # Write your code here.

    # this is better solution:
    # row=[0 for i in range(n)]
    # col=[0 for i in range(m)]
    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j]==0:
    #             row[i]=1
    #             col[j]=1
    # for i in range(n):
    #     for j in range(m):
    #         if row[i] or col[j]:
    #             matrix[i][j]=0
    # return matrix
    # optimal:
    col0=1
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                # mark i-th row
                matrix[i][0]=0
                # mark j-th col
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=0:
                # check for col and row
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(m):
            matrix[0][j]=0
    if col0==0:
        for i in range(n):
            matrix[i][0]=0
    return matrix

# zigzag
def zigzagOrder( mat):
    n=len(mat)
    l=[]
    for i in range(n):
        if i%2==0:
            j=0
            while j<n:
                l.append(mat[i][j])
                j+=1
        else:
            j=n-1
            while j>=0:
                l.append(mat[i][j])
                j-=1
    return l


def findDiagonalOrder(nums):
    newl=[]
    n=len(nums)
    # m=len(nums[0])
    groups={}
    for i in range(2*n-1):
        groups[i]=[]
    for i in range(n-1,-1,-1):
        for j in range(len(nums[i])):
            diagonal= i+j
            groups[diagonal].append(nums[i][j])
    curr=0
    while curr in groups:
        newl.extend(groups[curr])
        curr+=1
    return newl
    # for curr in groups:
    #     newl.extend(groups[curr])
    # return groups
nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
print(findDiagonalOrder(nums))