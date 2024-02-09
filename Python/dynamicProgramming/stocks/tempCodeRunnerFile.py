def maxprofit(prices):
    n=len(prices)
    dp=[[0 for i in range(2)]for i in range(n+1)]

    for ind in range(n-1,-1,-1):
        for buy in range(2):
            if buy==0:
                take=-prices[ind]
                if ind+1<len(prices):
                    take+=dp[ind+1][1]
                nottake=0+dp[ind+1][0]
                dp[ind][buy]=max(take,nottake)
            elif buy==1:
                sell=prices[ind]
                if ind+2<len(prices):
                    sell+=dp[ind+2][0]
                notsell=0+dp[ind+1][1]
                dp[ind][buy]= max(sell,notsell)
    return dp[0][0]
prices=[4,9,0,4,10]
print(maxprofit(prices))