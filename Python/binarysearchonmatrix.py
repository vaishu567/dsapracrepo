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
    rows=len(mat)
    cols=len(mat[0])
    # low=0
    # high=rows-1
    for row in range(rows):
        if mat[row][0]<=target and target<=mat[row][-1]:
            booli=bs(mat[row],target)
            if booli==True:
                return True
    return False