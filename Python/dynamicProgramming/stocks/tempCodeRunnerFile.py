def bestTimeToBuyAndSell(values):
    n=len(values)
    dp=[[0 for _ in range(2)] for _ in range(len(values)+1)]
    dp[n][0]=dp[n][1]=0
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            if buy:
                take=-values[ind]+dp[ind+1][0]
                nottake=0+dp[ind+1][1]
                dp[ind][buy] =max(take,nottake)
            else:
                take=values[ind]+dp[ind+1][1]
                nottake=0+dp[ind+1][0]
                dp[ind][buy]=max(take,nottake)
    return dp[0][1]
    
values=[1,2,3,4,5,6,7]
print(bestTimeToBuyAndSell(values))