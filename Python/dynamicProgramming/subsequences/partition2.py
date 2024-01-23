# for this problem look into notes:
# tabulation of previous target subset sum:
def partition2(arr,k):
    dp=[[False for i in range(k+1)] for j in range(len(arr))]
    for i in range(len(arr)):
        dp[i][0]=True
    if arr[0]<=k:
        dp[0][arr[0]]=True
    for i in range(1,len(arr)):
        for target in range(1,k+1):
            nottake=dp[i-1][target]
            take=False
            if arr[i]<=target:
                take=dp[i-1][target-arr[i]]
            dp[i][target]=(take or nottake)
    return dp
    # this is target tabulation code:
    # now the actual problem:
def actual(arr,n):
    totalsum=sum(arr)
    dp=partition2(arr,totalsum)
    mini=float('inf')
    for i in range(totalsum//2):
        if dp[n-1][i]==True:
            s1=i
            s2=totalsum-i
            mini=min(mini,abs(s1-s2))
    return mini




