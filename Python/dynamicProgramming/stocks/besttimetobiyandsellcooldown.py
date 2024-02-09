def maxprofit(prices,buy,ind):
    if ind==len(prices):
        return 0
    if buy:
        take=-prices[ind]
        if ind+1<len(prices):
            take+=maxprofit(prices,0,ind+1)
        nottake=0+maxprofit(prices,1,ind+1)
        return max(take,nottake)
    else:
        sell=prices[ind]
        if ind+2<len(prices):
            sell+=maxprofit(prices,1,ind+2)
        notsell=0+maxprofit(prices,0,ind+1)
        return max(sell,notsell)
prices=[4,9,0,4,10]
print(maxprofit(prices,1,0))

# memoization:
def maxprofit(prices,buy,ind,dp):
    if ind==len(prices):
        return 0
    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    if buy:
        take=-prices[ind]
        if ind+1<len(prices):
            take+=maxprofit(prices,0,ind+1,dp)
        nottake=0+maxprofit(prices,1,ind+1,dp)
        dp[ind][buy]=max(take,nottake)
        return dp[ind][buy]
    else:
        sell=prices[ind]
        if ind+2<len(prices):
            sell+=maxprofit(prices,1,ind+2,dp)
        notsell=0+maxprofit(prices,0,ind+1,dp)
        dp[ind][buy]= max(sell,notsell)
        return dp[ind][buy]
prices=[4,9,0,4,10]
dp=[[-1 for i in range(2)]for i in range(len(prices))]
print(maxprofit(prices,1,0,dp))

# tabulation:
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

