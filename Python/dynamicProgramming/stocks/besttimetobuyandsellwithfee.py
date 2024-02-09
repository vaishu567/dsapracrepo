def maxprofit(prices,buy,k,ind):
    if ind==len(prices):
        return 0
    if buy:
        take=-prices[ind]+maxprofit(prices,0,k,ind+1)
        nottake=0+maxprofit(prices,1,k,ind+1)
        return max(take,nottake)
    else:
        sell=prices[ind]-k+maxprofit(prices,1,k,ind+1)
        notsell=0+maxprofit(prices,0,k,ind+1)
        return max(sell,notsell)
prices=[1,2,3]
k=1
print(maxprofit(prices,1,k,0))

# memoization:
def maxprofit(prices,buy,k,ind,dp):
    if ind==len(prices):
        return 0
    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    if buy:
        take=-prices[ind]+maxprofit(prices,0,k,ind+1,dp)
        nottake=0+maxprofit(prices,1,k,ind+1,dp)
        dp[ind][buy]=max(take,nottake)
        return dp[ind][buy]
    else:
        sell=prices[ind]-k+maxprofit(prices,1,k,ind+1,dp)
        notsell=0+maxprofit(prices,0,k,ind+1,dp)
        dp[ind][buy]= max(sell,notsell)
        return dp[ind][buy]
prices=[1,2,3]
k=1
n=len(prices)
dp=[[-1 for _ in range(2)]for _ in range(n)]
print(maxprofit(prices,1,k,0,dp))

# tabulation:
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