# this is the modification question for frog jump:
# recursive code:
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
heights=[10,40,50,20,60]
k=3
n=5
index=n-1
minj=float('inf')
jump=float('inf')
dp=[-1 for i in range(n+1)]
print(dpmemoization(index,k,heights,minj,jump,dp))



        



    
