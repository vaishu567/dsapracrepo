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
def countSubsetsk(arr,k,index):
    if k==0:
        return 1
    if index==len(arr):
        if k==0:
            return 1
        else:
            return 0  
    if dp[index][k]!=-1:
        return dp[index][k]
    nottake=countSubsetsk(arr,k,index+1)
    take=0
    if arr[index]<=k:
        take=countSubsetsk(arr,k-arr[index],index+1)
    dp[index][k]=take+nottake
    return dp[index][k]


arr=[1,4,4,5]
k=5
dp=[[-1 for _ in range(k+1)] for _ in range(len(arr))]
print(countSubsetsk(arr,k,0))

# tabulation:
# top-down:
def countSubsetsk(arr,k):
    dp=[[0 for _ in range(k+1)] for _ in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0]=1
    if arr[0]<=k:
        dp[0][arr[0]]=1 
    for i in range(1,len(arr)):
        for target in range(1,k+1):
                    
            nottake=dp[i-1][target]
            take=0
            if arr[i]<=target:
                take=dp[i-1][target-arr[i]]
            dp[i][target]=take+nottake
    return dp[n-1][k]



    
