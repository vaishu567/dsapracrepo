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
dp=[[-1 for i in range(len(values))] for i in range(len(values))]
print(bestTimeToBuyAndSell(values,len(values),0,1,dp))