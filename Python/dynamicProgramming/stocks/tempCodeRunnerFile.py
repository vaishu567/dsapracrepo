def maxPro(prices,ind,buy,cap,dp):
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