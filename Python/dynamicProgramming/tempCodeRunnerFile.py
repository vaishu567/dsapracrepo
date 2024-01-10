# using tabulation:
def tabulation(arr):
    n=len(arr)
    dp=[-1 for i in range(n+3)]
    dp[n]=0
    dp[n+1]=0
    dp[n+2]=0
    # from last to 1
    for i in range(n-1,0,-1):
        pick=arr[i]+dp[i+2]
        notpick=0+dp[i+1]
        dp[i]=max(pick,notpick)
    # from n-2 to 0
    dp2=[-1 for i in range(n+2)]
    dp2[n-1]=0
    dp2[n]=0
    dp2[n+1]=0
    for i in range(n-2,-1,-1):
        pick=arr[i]+dp2[i+2]
        notpick=0+dp2[i+1]
        dp2[i]=max(pick,notpick)
    # return max(dp[1],dp2[0])
    return (dp,dp2)
arr=[200,3,140,20,10]
print(tabulation(arr))