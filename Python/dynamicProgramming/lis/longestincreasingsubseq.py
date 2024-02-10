def longestincreasingsub(arr,n,ind,prev):
    if ind==n:
        return 0
    nottake=0+longestincreasingsub(arr,n,ind+1,prev)
    take=float('-inf')
    if prev==-1 or arr[ind]>arr[prev]:
        take=1+longestincreasingsub(arr,n,ind+1,ind)
    return max(take,nottake)
arr=[5,4,11,1,16,8]
n=len(arr)
print(longestincreasingsub(arr,n,0,-1))
# time complexity:
# for every element we are taking or not taking so O(2^n)
# S.C=O(n) auxiliary stack space:

# memoization:
def longestincreasingsub(arr,n,ind,prev,dp):
    if ind==n:
        return 0
    if dp[ind][prev]!=-1:
        return dp[ind][prev]
    nottake=0+longestincreasingsub(arr,n,ind+1,prev,dp)
    take=float('-inf')
    if prev==-1 or arr[ind]>arr[prev]:
        take=1+longestincreasingsub(arr,n,ind+1,ind,dp)
    dp[ind][prev]= max(take,nottake)
    return dp[ind][prev]
arr=[5,4,11,1,16,8]
n=len(arr)
dp=[[-1 for i in range(n+1)] for i in range(n)]
print(longestincreasingsub(arr,n,0,-1,dp))

# tabulation:
def longestincreasingsub(arr,n):
    dp=[[0 for i in range(n+1)] for i in range(n+1)]
    for ind in range(n-1,-1,-1):
        for prev in range(ind-1,-2,-1):
            nottake=0+dp[ind+1][prev+1]
            take=float('-inf')
            if prev==-1 or arr[ind]>arr[prev]:
                take=1+dp[ind+1][ind+1]
            dp[ind][prev+1]= max(take,nottake)
    return dp[0][0]
arr=[5,4,11,1,16,8]
n=len(arr)
print(longestincreasingsub(arr,n))

# spaceoptimization:
def longestincreasingsub(arr,n):
    next=[0 for i in range(n+1)]
    curr=[0 for i in range(n+1)]
    for ind in range(n-1,-1,-1):
        for prev in range(ind-1,-2,-1):
            nottake=0+next[prev+1]
            take=float('-inf')
            if prev==-1 or arr[ind]>arr[prev]:
                take=1+next[ind+1]
            curr[prev+1]= max(take,nottake)
        next=curr
    return curr[0]
arr=[5,4,11,1,16,8]
n=len(arr)
print(longestincreasingsub(arr,n))


    
