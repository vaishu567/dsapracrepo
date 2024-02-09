def maxprofit(prices,k):
    dp=[[0 for _ in range(2)]for _ in range(n+1)]
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            if buy==0:
                take=-prices[ind]+dp[ind+1][1]
                nottake=0+dp[ind+1][0]
                dp[ind][buy]=max(take,nottake)
            elif buy==1:
                sell=prices[ind]-k+dp[ind+1][0]
                notsell=0+dp[ind+1][1]
                dp[ind][buy]= max(sell,notsell)
    return dp[0][0]
prices=[1,2,3]
k=1
n=len(prices)
print(maxprofit(prices,k))