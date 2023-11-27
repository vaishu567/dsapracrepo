from math import *

def binarySearch(arr, n, x) :
    #Your code goes here
    s=0
    e=n-1
    while s<=e:
        m=(s+e)//2
        if arr[m]>x:
            e=m-1
        elif arr[m]<x:
            s=m+1
        else:
            return m
    return -1


# lowerbound:
def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    s=0
    e=n-1
    lowerb=n
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>x:
            lowerb=min(mid,lowerb)
            e=mid-1
        elif arr[mid]<x:
            s=mid+1
        else:
            lowerb=min(mid,lowerb)
            e=mid-1
    return lowerb
# upper bound:
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
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

# search insert position:
# this is similar to lower bound if element range is not in 
# arr we should hypothetically place it in the nth position 
def searchInsert(arr: [int], m: int) -> int:
    # Write your code here.
    n=len(arr)
    s=0
    e=n-1
    insert=n
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>m:
            insert=min(mid,insert)
            e=mid-1
        elif arr[mid]<m:
            s=mid+1
        else:
            insert=min(mid,insert)
            e=mid-1      
    return insert

# ////////////////////////////////////////////////////////

# find floor and ceil:
# def getFloorAndCeil(a, n, x):
#     # Write your code here.
#     ceili=-1
#     floori=-1
#     s=0
#     e=n-1
#     while s<=e:
#         mid=(s+e)//2
#         if a[mid]>x:
#             ceili=a[mid]
#             e=mid-1
#         elif a[mid]<x:
#             floori=a[mid]
#             s=mid+1
#         else:
#             floori=a[mid]
#             ceili=a[mid]
#             s=mid+1
#             e=mid-1
#     return floori,ceili

def findFloor(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] <= x:
            ans = arr[mid]
            # look for smaller index on the left
            low = mid + 1
        else:
            high = mid - 1  # look on the right

    return ans


def findCeil(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] >= x:
            ans = arr[mid]
            # look for smaller index on the left
            high = mid - 1
        else:
            low = mid + 1  # look on the right

    return ans
def getFloorAndCeil(arr, n, x):
    f = findFloor(arr, n, x)
    c = findCeil(arr, n, x)
    return (f, c)


# /////////////////////////////////////////////////
# first and last occurance of element in sorted array:
# using upper and lower bound:
def lb(arr,n,k):
    s=0
    e=n-1
    lowerb=n
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>=k:
            lowerb=min(lowerb,mid)
            e=mid-1
        else:
            s=mid+1
    return lowerb

def up(arr,n,k):
    s=0
    e=n-1
    upperb=n
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>k:
            upperb=min(upperb,mid)
            e=mid-1
        else:
            s=mid+1
    return upperb

def firstAndLastPosition(arr, n, k):
    # Write your code here
    first=lb(arr,n,k)
    sec=up(arr,n,k)
    if arr[first]!=k or first==n:
        return -1,-1
    return first,sec-1
# without using upper and lower bound:

def searchRange( nums, t) :
    first=-1
    last=-1
    n=len(nums)
    # for finding first occurance:
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if nums[mid]==t:
            first=mid
            e=mid-1
        elif nums[mid]>t:
            e=mid-1
        else:
            s=mid+1
    # for finding last occurance:
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if nums[mid]==t:
            last=mid
            s=mid+1
        elif nums[mid]>t:
            e=mid-1
        else:
            s=mid+1
    return [first,last]

        