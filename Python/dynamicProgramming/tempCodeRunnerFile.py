def tabulation(index,heights,left,right,dp):
    dp[0]=0
    for i in range(1,len(heights)):
        left= dp[i-1]+abs(heights[i]-heights[i-1])
        if i>1:
            right= dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i]=min(left,right)
    return dp[index]
heights=[30,10,60,10,60,50]
left=float('inf')
right=float('inf')
dp=[-1 for i in range(len(heights))]
print(tabulation(len(heights)-1,heights,left,right,dp))