def knapsackrecur(wt,val,W,n):
    # if W==0 or ind==n:
    #     return 0
    dp=[[0 for i in range(W+1)] for j in range(n)]
    take=0
    for i in range(n):
        dp[i][0]=0
    for i in range(n):
        for j in range(1,W+1):
            if wt[i]<=j:
                take= val[i]+dp[i-1][j-wt[i]]
            nottake=0+dp[i-1][j]
            dp[i][j]= max(take,nottake)
    return dp[n-1][W]
wt=[1,2,4,5]
n=len(wt)
val=[5,4,8,6]
W=5
print(knapsackrecur(wt,val,W,n))