def maxprofit(prices,buy,k,ind):
    if k==0:
        return 0
    if ind==len(prices):
        return 0
    if buy:
        take=-prices[ind]+maxprofit(prices,0,k,ind+1)
        nottake=0+maxprofit(prices,1,k,ind+1)
        return max(take,nottake)
    else:
        sell=prices[ind]+maxprofit(prices,1,k-1,ind+1)
        notsell=0+maxprofit(prices,0,k,ind+1)
        return max(sell,notsell)
prices=[3,2,6,5,0,3]
k=2
print(maxprofit(prices,1,k,0))


# memoization:
def maxprofit(prices,buy,k,ind):
    if k==0:
        return 0
    if ind==len(prices):
        return 0
    if dp[ind][buy][k]!=-1:
        return dp[ind][buy][k]
    if buy:
        take=-prices[ind]+maxprofit(prices,0,k,ind+1,dp)
        nottake=0+maxprofit(prices,1,k,ind+1,dp)
        dp[ind][buy][k]=max(take,nottake)
        return dp[ind][buy][k]
    else:
        sell=prices[ind]+maxprofit(prices,1,k-1,ind+1,dp)
        notsell=0+maxprofit(prices,0,k,ind+1,dp)
        dp[ind][buy][k]= max(sell,notsell)
        return dp[ind][buy][k]
prices=[3,2,6,5,0,3]
k=2
dp=[[[-1 for _ in range(k+1)] for _ in range(2)]for _ in range(len(prices))]
print(maxprofit(prices,1,k,0,dp))

# tabulation:
def maxprofit(prices,k):
    n=len(prices)
    dp=[[[0 for _ in range(k+1)] for _ in range(2)]for _ in range(n+1)]
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for k in range(1,k+1):
                if buy==0:
                    take=-prices[ind]+dp[ind+1][1][k]
                    nottake=0+dp[ind+1][0][k]
                    dp[ind][buy][k]=max(take,nottake)
                elif buy==1:
                    sell=prices[ind]+dp[ind+1][0][k-1]
                    notsell=0+dp[ind+1][1][k]
                    dp[ind][buy][k]= max(sell,notsell)
    return dp[0][0][2]
prices=[3,2,6,5,0,3]
k=2
print(maxprofit(prices,k))


