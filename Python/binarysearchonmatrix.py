#  Row with max 1s:

"""
    Time Complexity: O(N * M)
    Space Complexity: O(1)

    Where N is the number of rows and M is the number of columns in the given matrix.
"""
def lowerBound(arr, n, x):
    # Write your code here
    s=0
    e=n-1
    lowerb=n
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>=x:
            lowerb=min(mid,lowerb)
            e=mid-1
        elif arr[mid]<x:
            s=mid+1
    return lowerb

def rowWithMax1s(matrix: [[int]], n: int, m: int) -> int:

    #    maxCount stores the maximum number of 1s found till now and ans is the index of that particular row.4
    maxi=-float('inf')
    ans=float('inf')
    for row in range(n):
        lower=lowerBound(matrix[row],m,1)
        if m-lower>maxi:
            maxi=m-lower
            ans=row
        elif m-lower==maxi:
            maxi=m-lower
            ans=min(ans,row)
    return ans

# /////////////////////////////////////////////////////////////////////
# search in a 2D matrix:
# better:
# T.C= O(rows+log(col)) here it is performing bs for only one row:
def bs(arr,target):
    s=0
    e=len(arr)-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==target:
            return True
        elif arr[mid]>target:
            e=mid-1
        else:
            s=mid+1
    return False

def searchMatrix(mat: [[int]], target: int) -> bool:
    # Write your code here.
    # rows=len(mat)
    # cols=len(mat[0])
    # # low=0
    # # high=rows-1
    # for row in range(rows):
    #     if mat[row][0]<=target and target<=mat[row][-1]:
    #         booli=bs(mat[row],target)
    #         if booli==True:
    #             return True
    # return False
    n=len(mat)
    m=len(mat[0])
    s=0
    e=(n*m)-1
    while s<=e:
        mid=(s+e)//2
        row=mid//m
        col=mid%m
        if (mat[row][col])==target:
            return True
        elif (mat[row][col])<target:
            s=mid+1
        else:
            e=mid-1
    return False
# search on matrix-II:
# t.c=o(n+m) in worst case
def searchMatrix(matrix, target):
    m=len(matrix)
    n=len(matrix[0])
    col=n-1
    row=0
    while row<m and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            col-=1
        else:
            row+=1
    return False

# /////////////////////////////////////////////////////////////////////////////
# findpeak element:
def findmaxelrow(mat,n,m,col):
    maxValue=-1
    index=-1
    for i in range(n):
        if mat[i][col]>maxValue:
            maxValue=mat[i][col]
            index=i
    return index


def findPeakGrid(g: [[int]]) -> [int]:
    # Write your code here.
    n=len(g)
    m=len(g[0])
    s=0
    e=m-1
    while s<=e:
        mid=(s+e)//2
        midrow=findmaxelrow(g,n,m,mid)
        if mid-1>=0:
            left=g[midrow][mid-1]
        else:
            left=-1
        if mid+1<m:
            right=g[midrow][mid+1]
        else:
            right=-1
        if left<g[midrow][mid] and g[midrow][mid]>right:
            return [midrow,mid]
        elif left>g[midrow][mid] and g[midrow][mid]>right:
            e=mid-1
        else:
            s=mid+1
    return [-1,-1]
# ///////////////////////////////////////////////////////////////////////////////
# findmedian:
# T.C=O(log(10^9)x(m)x(log(n)))
def upperbound(arr,x):
    n=len(arr)
    upperb=n
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>x:
            upperb=min(upperb,mid)
            e=mid-1
        else:
            s=mid+1
    return upperb



def countforsmallel(matrix,n,m,el):
    count=0
    for i in range(m):
        count+=upperbound(matrix[i],el)
    return count





def median(matrix: [[int]], m: int, n: int) -> int:
    # Write your code here.
    # extremebruteforce:
    # arr=[]
    # for i in range(m):
    #     for j in range(n):
    #         arr.append(matrix[i][j])
    # arr.sort()
    # s=0
    # e=len(arr)-1
    # mid=(s+e)//2
    # return arr[mid]
    # optimal:
    req=(n*m)//2
    low=float('inf')
    high=float('-inf')
    for i in range(m):
        low=min(low,matrix[i][0])
    for i in range(m):
        high=max(high,matrix[i][n-1])
    while low<=high:
        mid=(low+high)//2
        if countforsmallel(matrix,n,m,mid)<=req:
            low=mid+1
        elif countforsmallel(matrix,n,m,mid)>req:
            high=mid-1
    return low

x="67"
a=ord('5')-48
print(a)
print(chr(a+48))
print(int('456'))

print(chr(35427))

s="hi my name is vaishnavi"
l=list(s)
# print(l)

def reverse_word(s, start, end):
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return s
print(reverse_word(l,0,len(l)-1))
