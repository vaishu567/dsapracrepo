# S.C=O(N) only for array no recurssion stack space
def tabfib(n,dp):
    dp[0]=0
    dp[1]=1
    for i in range(2,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
n=0
dp=[-1 for i in range(n+1)]
print(tabfib(n,dp))