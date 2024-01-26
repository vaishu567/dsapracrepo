def knapsackrecur(wt,val,ind,W,n):
    if W==0 or ind==n:
        return 0
    take=0
    if wt[ind]<=W:
        take= val[ind]+knapsackrecur(wt,val,ind+1,W-wt[ind],n)
    nottake=0+knapsackrecur(wt,val,ind+1,W,n)
    return max(take,nottake)
n=3
wt=[3,4,5]
val=[30,50,60]
W=8
print(knapsackrecur(wt,val,0,W,n))

# memoization:
def knapsackrecur(wt,val,ind,W,n,dp):
    if W==0 or ind==n:
        return 0
    take=0
    if dp[ind][W]!=-1:
        return dp[ind][W]
    if wt[ind]<=W:
        take= val[ind]+knapsackrecur(wt,val,ind+1,W-wt[ind],n,dp)
    nottake=0+knapsackrecur(wt,val,ind+1,W,n,dp)
    dp[ind][W]= max(take,nottake)
    return dp[ind][W]
wt=[1,2,4,5]
n=len(wt)
val=[5,4,8,6]
W=5
dp=[[-1 for i in range(W+1)] for j in range(n)]
print(knapsackrecur(wt,val,0,W,n,dp))




# tabulation:
def knapsackrecur(wt,val,W,n):
    # if W==0 or ind==n:
    #     return 0
    dp=[[0 for i in range(W+1)] for j in range(n)]
    # for base case if wt[0]=5 and max W=4 can we steal it?
    # no hence we write base case as i->(wt[0],W+1): dp[0][i]=val[0]
    for i in range(wt[0],W+1):
        dp[0][i]=val[0]
    for i in range(1,n):
        for j in range(W+1):
            take=-float('inf')
            if wt[i]<=j:
                take= val[i]+dp[i-1][j-wt[i]]
            nottake=0+dp[i-1][j]
            dp[i][j]= max(take,nottake)
    return dp[n-1][W]
wt=[1,2,4,5]
n=len(wt)
val=[5,4,8,6]
W=5
print(knapsackrecur(wt,val,W,n))
