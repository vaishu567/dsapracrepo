def countSubsetsk(arr,k):
    n=len(arr)
    dp=[[0 for _ in range(k+1)] for _ in range(n)]
    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1
    if arr[0]!=0 and arr[0]<=k:
        dp[0][arr[0]]=1
    # return dp
    for i in range(1,n):
        for target in range(k+1):
            nottake=dp[i-1][target]
            take=0
            if arr[i]<=k:
                take=dp[i-1][target-arr[i]]
            dp[i][target]=take+nottake
    return dp[n-1][k]


def countPartitions(n, d, arr):
    # write your code here
    totalsum=sum(arr)
    k=(totalsum+d)
    if k%2==0:
        count=countSubsetsk(arr,k//2)
        return count
    else:
        return 0
arr=[1,1,1,1]
n=len(arr)
d=0
print(countPartitions(n,d,arr))