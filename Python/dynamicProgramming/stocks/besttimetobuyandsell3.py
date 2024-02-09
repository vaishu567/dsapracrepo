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




# O(n) time complexity, O(1) space solution using State Machine and DP

# This approach can be used for all the problems based on stock prices.

# The idea is to design a state machine that correctly describes the problem statement.

# image

# Intuition behind the state diagram:
# We begin at state 0, where we can either rest (i.e. do nothing) or buy stock at a given price.

# If we choose to rest, we remain in state 0
# If we buy, we spend some money (price of the stock on that day) and go to state 1
# From state 1, we can once again choose to do nothing or we can sell our stock.

# If we choose to rest, we remain in state 1
# If we sell, we earn some money (price of the stock on that day) and go to state 2
# This completes one transaction for us. Remember, we can only do atmost 2 transactions.

# From state 2, we can choose to do nothing or buy more stock.

# If we choose to rest, we remain in state 2
# If we buy, we go to state 3
# From state 3, we can once again choose to do nothing or we can sell our stock for the last time.

# If we choose to rest, we remain in state 3
# If we sell, we have utilized our allowed transactions and reach the final state 4
# Going from the state diagram to code

# // Assume we are in state S
# // If we buy, we are spending money but we can also choose to do nothing
# // Doing nothing means going from S->S
# // Buying means going from some state X->S, losing some money in the process
# S = max(S, X-prices[i])

# // Similarly, for selling a stock
# S = max(S, X+prices[i])
# Code:

# int maxProfit(vector<int>& prices) {
# 	if(prices.empty()) return 0;
# 	int s1=-prices[0],s2=INT_MIN,s3=INT_MIN,s4=INT_MIN;
        
# 	for(int i=1;i<prices.size();++i) {            
# 		s1 = max(s1, -prices[i]);
# 		s2 = max(s2, s1+prices[i]);
# 		s3 = max(s3, s2-prices[i]);
# 		s4 = max(s4, s3+prices[i]);
# 	}
# 	return max(0,s4);
# }
# We can create 4 variables, one for each state excluding the initial state since that's always 0, initializing s1 to -prices[0] and the rest to INT_MIN since they will get overwritten later.

# To reach s1, we either stay in s1 or we buy stock for the first time.
# To reach s2, we either stay in s2 or we sell from s1 and come to s2
# Similarly for s3 and s4.

# In the end, we return s4 or more accurately, max(0,s4) since we initialize s4 to INT_MIN.

# This idea works for all problems on stocks, as long as our state diagram is correct, we can code it up like this.

# Side Note: Technically, this is a dynammic programming approach and we should actually be doing s2[i] = max(s2[i-1], s1[i-1]+prices[i]) but we can be rest assured that the overwritten value of s1 will always be better than the previous one and hence we do not need temporary variables.

