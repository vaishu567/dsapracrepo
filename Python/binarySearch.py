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

# ////////////////////////////////////////////////////

# count number of occurences of a given element:
def searchRange(nums, t) :
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
def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    [x,y]=searchRange(arr,x)
    if x==-1:
        return 0
    return y-x+1

# ///////////////////////////////////////////////

# search in rotated sorted array-I:
def binarySearch(arr,s,e,k):
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>k:
            e=mid-1
        elif arr[mid]<k:
            s=mid+1
        else:
            return mid
    return -1
def search(arr, n, k):

    # Write your code here
    i=0
    pivot=0
    while i<n-1:
        if arr[i]>arr[i+1]:
            pivot=i
            break
        else:
            i+=1
    ans=binarySearch(arr,0,pivot,k)
    ans2=binarySearch(arr,pivot+1,n-1,k)
    if ans==-1:
        return ans2
    elif ans2==-1:
        return ans
    return -1

# 2nd approach:
def search(arr, n, k):
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==k:
            return mid
        # check for left sorted:
        if arr[s]<=arr[mid]:
            if arr[s]<=k and k<=arr[mid]:
                e=mid-1
            else:
                s=mid+1
        # check for right sorted:
        else:
            if arr[mid]<=k and k<=arr[e]:
                s=mid+1
            else:
                e=mid-1
    return -1
# ///////////////////////////////////////////////////////////////////


# Search in Rotated Sorted Array-II:
# approach-1:
def binarySearch(arr,s,e,k):
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>k:
            e=mid-1
        elif arr[mid]<k:
            s=mid+1
        else:
            return mid
    return -1

def searchInARotatedSortedArrayII(arr, k ):
    # Write your code here.
    n=len(arr)
    i=0
    pivot=0
    while i<n-1:
        if arr[i]>arr[i+1]:
            pivot=i
            break
        else:
            i+=1
    ans=binarySearch(arr,0,pivot,k)
    ans2=binarySearch(arr,pivot+1,n-1,k)
    if ans!=-1 or ans2!=-1 :
        return True
    return False

# approach-2:

def searchInARotatedSortedArrayII(arr, k):
    # Write your code here.
    n=len(arr)
    s=0
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if arr[mid]==k:
            return True
        # check for mid==high==low:
        if arr[mid]==arr[s] and arr[mid]==arr[e]:
            s+=1
            e-=1
            continue
        # check for left sorted:
        if arr[s]<=arr[mid]:
            if arr[s]<=k and k<=arr[mid]:
                e=mid-1
            else:
                s=mid+1
        # check for right sorted:
        else:
            if arr[mid]<=k and k<=arr[e]:
                s=mid+1
            else:
                e=mid-1
    return False






# minimum in rotated sorted array:
# def findMin(arr):
    # Write your code here.
    # bruteforce:
    # i=0
    # n=len(arr)
    # pivot=0
    # while i<n-1:
    #     if arr[i]>arr[i+1]:
    #         pivot=i+1
    #         break
    #     else:
    #         i+=1
    # return arr[pivot]
    # optimal:
def findMin( nums):
    n=len(nums)
    s=0
    ans=100000000
    e=n-1
    while s<=e:
        mid=(s+e)//2
        if nums[s]<=nums[e]:
            ans=min(ans,nums[s])
            break
        # check for left sorted:
        if nums[s]<=nums[mid]:
            ans=min(ans,nums[s])
            s=mid+1
        # check for right sorted:
        else:
            ans=min(ans,nums[mid])
            e=mid-1
    return ans

# find number of rotations in array:
def findKRotation(arr):
    # Write your code here.
    n=len(arr)
    s=0
    e=n-1
    ans=1000000000
    indexmin=-1
    while s<=e:
        mid=(s+e)//2
        if arr[s]<=arr[e]:
            if arr[s]<ans:
                ans=arr[s]
                indexmin=s
            break

        # check for lefthalf
        if arr[s]<=arr[mid]:
            if arr[s]<ans:
                ans=arr[s]
                indexmin=s
            s=mid+1
        # check for righthalf:
        else:
            if arr[mid]<ans:
                ans=arr[mid]
                indexmin=mid
            e=mid-1
    if indexmin==-1:
        return 0
    return indexmin

# //////////////////////////////////////////////////////////////////////////////////
# single element in sorted:
def singleNonDuplicate(arr):
    # Write your code here
    # bruteforce:
    n=len(arr)
    # check for elements front and back elements same or not
    if n==1:
        return arr[0]
    for i in range(n):
        if i==0:
            if arr[i]!=arr[i+1]:
                return arr[i]

        elif i==n-1:
            if arr[i-1]!=arr[i]:
                return arr[i]
        else:
            if arr[i]!=arr[i+1] and arr[i]!=arr[i-1]:
                return arr[i]
            
def singleNonDuplicate(arr):
    # Write your code here
    # bruteforce:
    n=len(arr)
    # check for elements front and back elements same or not
    if n==1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    s=1
    e=n-2
    while s<=e:
        mid=(s+e)//2
        if arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
            return arr[mid]
        # we are on left and element lies on right:
        # here we are checking for (even, odd) condition:
        if (mid%2!=0 and arr[mid]==arr[mid-1]) or (mid%2==0 and arr[mid]==arr[mid+1]) :
            # our elemnt is on right so need to eliminate left half:
            s=mid+1
        # other are (odd, even) conditions:
        else:
            # eliminating right half
            e=mid-1
    return 
# //////////////////////////////////////////////////////////////////////////////

# find peak element in array:
def findPeakElement(arr):
    # Write your code here
    n=len(arr)
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0 
    if arr[n-1]>arr[n-2]:
        return n-1
    s=1
    e=n-2
    while s<=e:
        mid=(s+e)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
        # checking if arr[mid] is on increasing curve:
        elif arr[mid]>arr[mid-1] or arr[mid]<arr[mid+1]:
                s=mid+1
        # checking if arr[mid] is on decreasing curve:
        else:
                e=mid-1


# Binary Search on Answers:
# Find square root of a number:
def sqrrt(n):
    ans=1
    for i in range(1,n+1):
        if (i*i)<=n:
            ans=i
        else:
            break
    return (ans)//1
print(sqrrt(36))

# ///////////////////////////////////////////////////////
# Nth root of a number:
def NthRoot(n, m) :
    # Write Your Code Here
    s=1
    e=m-1
    while s<=e:
        mid=(s+e)//2
        if (mid**n)==m:
            return mid
        elif mid**n>m:
            e=mid-1
        else:
            s=mid+1
    return -1
# //////////////////////////////////////////////////////////////////////////
# koko eating bananas:
from math import *

def minimumRateToEatBananas(v, h) :
    # Write Your Code Here.
    # brute force:
    # for i in range(1,max(v)+1):
    #     total=0
    #     for j in range(0,len(v)):
    #         total+=(ceil((v[j]/i)))
    #     if total<=h:
    #         return i
    # optimal:
    s=1
    e=max(v)
    ans=0
    while s<=e:
        mid=(s+e)//2
        total=0
        for i in range(0,len(v)):
            total+=ceil(v[i]/mid)
        if total<=h:
            ans=mid
            e=mid-1
        elif total>h:
            s=mid+1
    return ans


# ////////////////////////////////////////////////////////////
# minimum days to make m bouquets:
def roseGarden(arr, k, m):
    # write yur code here
    # bruteforce:
    # i=min(arr)
    # j=max(arr)
    # for day in range(i,j+1):
    #     count=0
    #     Bou=0
    #     for l in range(len(arr)):
    #         if arr[l]<=day:
    #             count+=1
    #         else:
    #             Bou+=floor(count/k)
    #             count=0
    #     Bou+=floor(count/k)
    #     if Bou>=m:
    #         return day
    # return -1
    s=min(arr)
    e=max(arr)
    ans= float('inf')
    if len(arr)<m*k:
        return -1
    while s<=e:
        daymid=(s+e)//2
        count=0
        bouq=0
        for i in range(len(arr)):
            if arr[i]<=daymid:
                count+=1
            else:
                bouq+=floor(count/k)
                count=0
        bouq+=floor(count/k)
        if bouq>=m:
            ans=min(ans,daymid)
            e=daymid-1
        else:
            s=daymid+1
    if ans!=float('inf'):
        return ans
    return -1


# ////////////////////////////////////////////////////////////////////
# smallest divisor:
def smallestDivisor(arr, limit):
    # Write your code here.
    # bruteforce:
    # ans=float('inf')
    # for divisor in range(1,max(arr)+1):
    #     sumd=0
    #     for i in range(len(arr)):
    #         sumd+=ceil(arr[i]/divisor)
    #     if sumd<=limit:
    #         ans=min(divisor,ans)
    # return ans
    s=1
    e=max(arr)
    ans=float('inf')
    while s<=e:
        divisormid=(s+e)//2
        sumd=0
        for i in range(len(arr)):
            sumd+=ceil(arr[i]/divisormid)
        if sumd<=limit:
            ans=min(ans,divisormid)
            e=divisormid-1
        else:
            s=divisormid+1
    return ans


# //////////////////////////////////////////////////////////////////////////////////
# capacity of ship:
def shipWithinDays(weights, days):
    ans=float('inf')
    s=max(weights)
    e=sum(weights)
    # bruteforce:
    # for capacity in range(s,e+1):
    #     sumcap=0
    #     daycount=1
    #     for l in range(len(weights)):
    #         if sumcap+weights[l]>capacity:
    #             daycount+=1
    #             sumcap=weights[l]
    #         else:
    #             sumcap+=weights[l]
    #     if daycount<=days:
    #         ans=min(ans,capacity)
    # return ans
    while s<=e:
        capacitymid=(s+e)//2
        sumcap=0
        daycount=1
        for i in range(len(weights)):
            if sumcap+weights[i]>capacitymid:
                daycount+=1
                sumcap=weights[i]
            else:
                sumcap+=weights[i]
        if daycount<=days:
            ans=min(ans,capacitymid)
            e=capacitymid-1
        else:
            s=capacitymid+1
    return ans


# ///////////////////////////////////////////////////////////////////////
# find missing positive element at kth position:
def findKthPositive(self, vec: List[int], k: int) -> int:
    # for i in range(len(arr)):
    #     if arr[i]<=k:
    #         k+=1
    #     else:
    #         break
    # return k
    s=0
    n=len(vec)
    e=n-1
    while s<=e:
        mid=(s+e)//2
        missing=vec[mid]-(mid+1)
        if missing<k:
            s=mid+1
        else:
            e=mid-1
    return e+k+1
# ////////////////////////////////////////////////////////////////////////


# max(min) and min(max) variations:
# aggresivecows:
def aggressiveCows(stalls, k):
    # Write your code here.
    # brutefrce:
    # stalls.sort()
    # n=len(stalls)
    # maxi=stalls[n-1]
    # mini=stalls[0]
    # ans=-float('inf')
    # for dist in range(1,maxi-mini+1):
    #     lastcow=stalls[0]
    #     cowcount=1
    #     for j in range(1,n):
    #         if stalls[j]-lastcow>=dist:
    #             cowcount+=1
    #             lastcow=stalls[j]
    #         if cowcount>=k:
    #             ans=max(dist,ans)
    # return ans
    # optimal:
    stalls.sort()
    n=len(stalls)
    maxi=stalls[n-1]
    mini=stalls[0]
    ans=-float('inf')
    s=1
    e=maxi-mini
    while s<=e:
        middist=(s+e)//2
        lastcow=stalls[0]
        cowcount=1
        for i in range(1,n):
            if stalls[i]-lastcow>=middist:
                cowcount+=1
                lastcow=stalls[i]
        if cowcount>=k:
            ans=max(ans,middist)
            s=middist+1
        else:
            e=middist-1
    return ans


# min(max) variation allocate books:
def findPages(arr: [int], n: int, m: int) -> int:

    # Write your code here
    # Return the minimum number of pages
    if m>n:
        return -1
    # for pages in range(max(arr),sum(arr)+1):
    #     countstudents=1
    #     sumpages=0
    #     for i in range(len(arr)):
    #         if sumpages+arr[i]>pages:
    #             countstudents+=1
    #             sumpages=arr[i]
    #         else:
    #             sumpages+=arr[i]    
    #     if countstudents==m:
    #         return pages
    # return -1
    s=max(arr)
    e=sum(arr)
    ans=float('inf')
    while s<=e:
        midpages=(s+e)//2
        countstudents=1
        sumpages=0
        for i in range(len(arr)):
            if sumpages+arr[i]>midpages:
                countstudents+=1
                sumpages=arr[i]
            else:
                sumpages+=arr[i]
        # if countstudents==m:
        #     ans=min(ans,midpages)
        #     e=midpages-1
        if countstudents>m:
            s=midpages+1
        else:
            e=midpages-1
    return s
    # oppposite polarity concept


# //////////////////////////////////////////////////////////
# largest subarray sum minimum:
def largestSubarraySumMinimized(a, k):
    # Write Your Code Here
    # for sumA in range(max(a),sum(a)+1):
    #     subacount=1
    #     sumsub=0
    #     for i in range(len(a)):
    #         if sumsub+a[i]>sumA:
    #             subacount+=1
    #             sumsub=a[i]
    #         else:
    #             sumsub+=a[i]
    #     if subacount==k:
    #         return sumA
    ans=float('inf')
    s=max(a)
    e=sum(a)
    while s<=e:
        midsum=(s+e)//2
        subacount=1
        sumsub=0
        for i in range(len(a)):
            if sumsub+a[i]>midsum:
                subacount+=1
                sumsub=a[i]
            else:
                sumsub+=a[i]
        if subacount<=k:
            e=midsum-1
        else:
            s=midsum+1
    return s


