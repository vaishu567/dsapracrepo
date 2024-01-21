def subsetk(arr,k):
    n=len(arr)
    dp=[[False for i in range(k+1)] for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=k:
        dp[0][arr[0]]=True
    # return dp
    for index in range(1,n):
        for target in range(1,k+1):
            nottake=dp[index-1][target]
            take=False
            if target>=arr[index]:
                take=dp[index-1][target-arr[index]]
            dp[index][target]=(take or nottake)
    return dp[index][target]
arr=[1,2,3,1]
k=4
print(subsetk(arr,k))