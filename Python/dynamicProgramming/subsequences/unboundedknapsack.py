def recursiive(index,n,profit,wt,W):
    if  W==0 or index==n:
        return 0
    nottake=recursiive(index+1,n,profit,wt,W)
    take=0
    if wt[index]<=W:
        take=profit[index]+recursiive(index,n,profit,wt,W-wt[index])
    return max(take,nottake)

profit=[5,11,13]
wt=[2,4,6]
W=10
n=3
print(recursiive(0,n,profit,wt,W))


# memoization:
def recursiive(index,n,profit,wt,W):
    if  W==0 or index==n:
        return 0
    if dp[index][W]!=-1:
        return dp[index][W]
    nottake=recursiive(index+1,n,profit,wt,W)
    take=0
    if wt[index]<=W:
        take=profit[index]+recursiive(index,n,profit,wt,W-wt[index])
    dp[index][W]=max(take,nottake)
    return dp[index][W]

profit=[5,11,13]
wt=[2,4,6]
W=10
n=3
print(recursiive(0,n,profit,wt,W))



# tabulation:
def recursiive(n,profit,wt,W):
    for i in range(wt[0],W+1):
        dp[0][i]=(i//wt[0])*profit[0]
    for i in range(1,n):
        for j in range(W+1):
            take=float('-inf')
            nottake=dp[i-1][W]
            if wt[i]<=W:
                take=profit[i]+dp[i][W-wt[i]]
            dp[i][W]=max(take,nottake)
    return dp[n-1][W]

profit=[5,11,13]
wt=[2,4,6]
W=10
n=3
print(recursiive(0,n,profit,wt,W))