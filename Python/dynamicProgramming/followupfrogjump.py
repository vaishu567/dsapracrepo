# this is the modification question for frog jump:
# recursive code:
# T.C=O(N*k)
# S.C=O(N+N)
def stones(index,k,heights,minj,jump):
    if index==0:
        return 0
    for j in range(1,k+1):
        if (index-j)>=0:
            jump=stones(index-j,k,heights,minj,jump)+abs(heights[index]-heights[index-j])
            minj=min(minj,jump)
    return minj
heights=[10,40,50,20,60]
k=3
n=5
index=n-1
minj=float('inf')
jump=float('inf')
print(stones(index,k,heights,minj,jump))

# memoization:
def dpmemoization(index,k,heights,minj,jump,dp):
    dp[0]=0
    if dp[index]!=-1:
        return dp[index]
    for j in range(1,k+1):
        if index-j>=0:
            jump=dpmemoization(index-j,k,heights,minj,jump,dp)+abs(heights[index]-heights[index-j])
            minj=min(minj,jump)
        dp[index]=minj
    return dp[index]
heights=[10,40,50,20]
k=3
n=4
index=n-1
minj=float('inf')
jump=float('inf')
dp=[-1 for i in range(n+1)]
print(dpmemoization(index,k,heights,minj,jump,dp))


# tabulation:
def tabulation(index,k,heights,minj,jump,dp):
    dp[0]=0
    for i in range(1,index+1):
        minj=float('inf')
        for j in range(1,k+1):
            if i-j>=0:
                jump=dp[i-j]+abs(heights[i]-heights[i-j])
                minj=min(minj,jump)
        dp[i]=minj
    return dp[index]
heights=[10,40,50,20,60]
k=3
n=5
index=n-1
minj=float('inf')
jump=float('inf')
dp=[-1 for i in range(n)]
print(tabulation(index,k,heights,minj,jump,dp))

# spaceoptimizaton:
# here we will not be doing spaceoptimization becpz in worst case secenario we need to carry n variables if k=n
# hence there is no use for space optimizing it.
        



    
