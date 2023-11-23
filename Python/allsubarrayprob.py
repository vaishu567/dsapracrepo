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

a=[1,2,3,2]
b=2
xor=0


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
def getLongestZeroSumSubarrayLength(arr) :
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

def subarraysWithXorK(a: [int], b: int) -> int:
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
def ninjaGram(str):

    # Write your Code Here.
    # Return a boolean variable 'True' or 'False' denoting the answer
    d={i:0 for i in range(26)}
    for i in str:
        x=ord('a')-ord(i)
        if x not in d:
            d[x]=1
        d[x]+=1
    
    # for k,v in d.items():
    #     if v==0:
    #         return 'NO'
    # return 'YES'
print(ninjaGram('toosmallword'))


