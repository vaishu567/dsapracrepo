# here we are solving this problem using DP:
# ///memoization:
# we need to initialize dp array for memoization
# T.C=O(N)
# S.C=O(N) for recursion stack space+ O(N) for array used for memoization
def fibonaci(n,dpA):
    if n==0 or n==1:
        return n
    if dpA[n]!=-1:
        return dpA[n]
    dpA[n] =fibonaci(n-1,dpA)+fibonaci(n-2,dpA)
    return dpA[n]
n=0
dpA=[-1 for i in range(n+1)]
print(fibonaci(n,dpA))

# ///tabulation:
# T.C=O(N)
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

# space optimization:
# for optimizion space:
def spaceop(n):
    prev2=0
    prev=1
    for i in range(2,n+1):
        curri=prev2+prev
        prev2=prev
        prev=curri
    return prev
print(spaceop(8))


