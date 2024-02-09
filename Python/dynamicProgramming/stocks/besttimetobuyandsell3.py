def maxProfit(prices,ind,buy,cap):
    if cap==0:
        return 0
    if ind==len(prices):
        return 0
    if buy:
        take=-prices[ind]+maxProfit(prices,ind+1,0,cap)
        nottake=0+maxProfit(prices,ind+1,1,cap)
        return max(nottake,take)
    else:
        take=prices[ind]+maxProfit(prices,ind+1,1,cap-1)
        nottake=0+maxProfit(prices,ind+1,0,cap)
        return max(nottake,take)

prices=[3,3,5,0,3,1,4]
print(maxProfit(prices,0,1,2))

# memoization:
# def maxPro(prices,ind,buy,cap,dp):
#     if cap==0:
#         return 0
#     if ind==len(prices):
#         return 0
#     if dp[ind][buy][cap]!=-1:
#         return dp[ind][buy][cap]
#     if buy:
#         take=-prices[ind]+maxPro(prices,ind+1,0,cap,dp)
#         nottake=0+maxPro(prices,ind+1,1,cap,dp)
#         dp[ind][buy][cap]= max(nottake,take)
#         return dp[ind][buy][cap]
#     else:
#         take=prices[ind]+maxPro(prices,ind+1,1,cap-1,dp)
#         nottake=0+maxPro(prices,ind+1,0,cap,dp)
#         dp[ind][buy][cap]= max(nottake,take)
#         return dp[ind][buy][cap]
# prices=[3,3,5,0,3,1,4]
# dp=[[[-1  for i in range(3)] for i in range(2)]for i in range(len(prices))]
# print(dp)
# print(maxProfit(prices,0,1,2,dp))


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






