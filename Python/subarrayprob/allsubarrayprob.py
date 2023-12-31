# Longest subarray with given sum k (only +ve's)
def longestsub(arr,k):
    n=len(arr)
    i=0
    j=0
    sumk=0
    maxi=-10000000000
    while j<n:
        sumk+=arr[j]
        while sumk>k:
            sumk-=arr[i]
            i+=1
        if sumk==k:
            maxi=max(maxi,j-i+1) 
        j+=1
    return maxi
arr=[2,2,4,1,2]
print(longestsub(arr, 2))


# longest subarray with given sum k (pos, neg and 0's):
def longs(arr,k):
    n=len(arr)
    pref={}
    prefsum=0
    maxi=-190093902390
    for i in range(n):
        prefsum+=arr[i]
        rem=k-prefsum
        if rem in pref:
            maxi=max(maxi,i+1)
        if prefsum not in pref:
            pref[prefsum]=i
    return maxi

arr=[-50,0,52]
print(longs(arr,2))

# a=[1,2,3,2]
# b=2
# xor=0


# subarrays with sum 0:
def countsubarrays(arr):
    d={}
    count=0
    prefsum=0
    for i in range(n):
        prefsum+=arr[i]
        if prefsum==0:
            count+=1
        if prefsum in d:
            count+=d[prefsum]
            d[prefsum]+=1
        else:
            d[prefsum]=1  
    return count


# longest subarray with sum 0:
def getLongestZeroSumSubarrayLength(arr):
    # Write your code here.
    d={}
    n=len(arr)
    maxi=0
    sumi=0
    for i in range(n):
        sumi+=arr[i]
        if sumi==0:
            maxi=max(maxi,i+1)
        if sumi in d:
            leni=i-d[sumi]
            maxi=max(maxi,leni)
        else:
            d[sumi]=i
    return maxi








# count subarray with xor k:

def subarraysWithXorK(a, b):
    # Write your code here
    xor=0
    n=len(a)
    count=0
    d={0:1}
    for i in range(n):
        xor=xor^a[i]
        x=xor^b
        if x in d:
            count+=d[x]
        if xor not in d:
            d[xor]=1
        else:
            d[xor]+=1
    return count
# 1 2 3 3


# maxproduct subarray:
def subarrayWithMaxProduct(arr):
    # Write your code here.
    pref=1
    suf=1
    maxi=-100000000
    n=len(arr)
    for i in range(n):
        if pref==0:
            pref=1
        if suf==0:
            suf=1
        pref=pref*arr[i]
        suf=suf*arr[n-i-1]
        maxi=max(maxi,max(suf,pref))
    return maxi

# return subarrays list  with sum k:
def subarraysWithSumK( a:[int], k:int) ->[[int]]:
    # Write your code here
    i=0
    sumk=0
    n=len(a)
    fin=[]
    temp=[]
    for j in range(n):
        sumk+=a[j]
        temp.append(a[j])
        while i<j and sumk>k:
            sumk-=a[i]
            temp.remove(a[i])
            i+=1
        if sumk==k:
            fin.append(list(temp))
    return fin


# count the number of subarrays:
# Given an array A[] of N integers 
# and a range(L, R). The task is to 
# find the number of subarrays having 
# sum in the range L to R (inclusive).
def counti(A,k,N):
    i=0
    sumk=0
    count=0
    for j in range(N):
        sumk+=A[j]
        while i<j and sumk>k:
            sumk-=A[i]
            i+=1
        if sumk<=k:
            count+=j-i+1
    return count
    
def countSubarray(N, A, L, R):
    # code here
    count1=counti(A,R,N)
    count2=counti(A,(L-1),N)
    return count1-count2



