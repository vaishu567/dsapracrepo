# recursion:

def countSubsetsk(arr,k,index,sumk):
    if index==len(arr):
        if sumk==k:
            return 1
        else:
            return 0
    sumk=sumk+arr[index]
    take=countSubsetsk(arr,k,index+1,sumk)
    sumk=sumk-arr[index]
    nottake=countSubsetsk(arr,k,index+1,sumk)
    return take+nottake
arr=[1,4,4,5]
k=5
print(countSubsetsk(arr,k,0,0))


def countSubsetsk(arr,k,index):
    if index==len(arr):
        if k==0:
            return 1
        else:
            return 0     
    nottake=0+countSubsetsk(arr,k,index+1)
    take=0
    if arr[index]<=k:
        take=countSubsetsk(arr,k-arr[index],index+1)
    return take+nottake
arr=[1,4,4,5]
k=5
print(countSubsetsk(arr,k,0))

# memoization:
# here 1<=k<=1000
# 0<=arr[i]<=1000
# since arr[i] can be ==0 we should go till last index we should not write base case if k==0 return 1 coz we will miss cases where arr[i]=0 
def countSubsetsk(arr,k,index,dp):
    if index==len(arr):
        if k==0:
            return 1
        else:
            return 0     
    if dp[index][k]!=-1:
        return dp[index][k]
    nottake=countSubsetsk(arr,k,index+1,dp)
    take=0
    if arr[index]<=k:
        take=countSubsetsk(arr,k-arr[index],index+1,dp)
    dp[index][k]=take+nottake
    return dp[index][k]

def findWays(arr: List[int], k: int) -> int:
    # Write your code here.
    dp=[[-1 for _ in range(k+1)] for _ in range(len(arr))]
    mod=(10**9)+7

    return countSubsetsk(arr,k,0,dp)%mod

# tabulation:
# top-down:
def countSubsetsk(arr,k):
    mod=int(1e9+7)
    n=len(arr)
    dp=[[0 for _ in range(k+1)] for _ in range(len(arr))]
    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1
    if (arr[0]!=0 and arr[0]<=k):
        dp[0][arr[0]]=1 
    for i in range(1,n):
        for target in range(k+1):      
            nottake=dp[i-1][target]
            take=0
            if arr[i]<=target:
                take=dp[i-1][target-arr[i]]
            dp[i][target]=(take+nottake)
    return dp[n-1][k]%mod
arr=[1,1,1,1]
k=2
print(countSubsetsk(arr,k))



    
