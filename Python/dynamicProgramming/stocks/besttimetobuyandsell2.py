# in this we can buy and sell how many times we want but if we bought any thing then we have to sell it to buy another stock:
def bestTimeToBuyAndSell(values,n,ind,buy):
    if ind==n:
        return 0
    if buy:
        take=-values[ind]+bestTimeToBuyAndSell(values,n,ind+1,0)
        nottake=0+bestTimeToBuyAndSell(values,n,ind+1,1)
        return max(take,nottake)
    else:
        take=values[ind]+bestTimeToBuyAndSell(values,n,ind+1,1)
        nottake=0+bestTimeToBuyAndSell(values,n,ind+1,0)
        return max(take,nottake)
    
values=[1,2,3,4,5,6,7]
print(bestTimeToBuyAndSell(values,len(values),0,1))
    
# memoization:
# in this we can buy and sell how many times we want but if we bought any thing then we have to sell it to buy another stock:
def bestTimeToBuyAndSell(values,n,ind,buy,dp):
    if ind==n:
        return 0
    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    if buy:
        take=-values[ind]+bestTimeToBuyAndSell(values,n,ind+1,0,dp)
        nottake=0+bestTimeToBuyAndSell(values,n,ind+1,1,dp)
        dp[ind][buy] =max(take,nottake)
        return dp[ind][buy]
    else:
        take=values[ind]+bestTimeToBuyAndSell(values,n,ind+1,1,dp)
        nottake=0+bestTimeToBuyAndSell(values,n,ind+1,0,dp)
        dp[ind][buy]=max(take,nottake)
        return dp[ind][buy]
    
values=[1,2,3,4,5,6,7]
dp=[[-1 for i in range(2)] for i in range(len(values))]
print(bestTimeToBuyAndSell(values,len(values),0,1,dp))


# tabulation:
def bestTimeToBuyAndSell(values,n,ind,buy,dp):
    if ind==n:
        return 0
    if dp[ind][buy]!=-1:
        return dp[ind][buy]
    if buy:
        take=-values[ind]+bestTimeToBuyAndSell(values,n,ind+1,0,dp)
        nottake=0+bestTimeToBuyAndSell(values,n,ind+1,1,dp)
        dp[ind][buy] =max(take,nottake)
        return dp[ind][buy]
    else:
        take=values[ind]+bestTimeToBuyAndSell(values,n,ind+1,1,dp)
        nottake=0+bestTimeToBuyAndSell(values,n,ind+1,0,dp)
        dp[ind][buy]=max(take,nottake)
        return dp[ind][buy]
    
values=[1,2,3,4,5,6,7]
dp=[[-1 for i in range(2)] for i in range(len(values))]
print(bestTimeToBuyAndSell(values,len(values),0,1,dp))