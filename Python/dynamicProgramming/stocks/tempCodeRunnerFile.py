# tabulation:
def maxPro(prices):
    n=len(prices)
    dp=[[[0  for i in range(3)] for i in range(2)]for i in range(n+1)]
 
    for ind in range(n-1,-1,-1):
        for buy in range(2):
            for cap in range(1,3):
                if buy==0:
                    take=-prices[ind]+dp[ind+1][1][cap]
                    nottake=0+dp[ind+1][0][cap]
                    dp[ind][buy][cap]= max(nottake,take)
                elif buy==1:
                    take=prices[ind]+dp[ind+1][0][cap-1]
                    nottake=0+dp[ind+1][1][cap]
                    dp[ind][buy][cap]= max(nottake,take)
    return dp[0][0][2]
prices=[3,3,5,0,3,1,4]
print(maxPro(prices))