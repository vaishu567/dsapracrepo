def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp=[-1 for i in range(len(nums)+3)]
    dp[len(nums)]=0
    dp[len(nums)+1]=0
    dp[len(nums)+2]=0
    for i in range(len(nums)-1,-1,-1):
        pick=arr[i]+ dp[i+2]
        notpick=0+dp[i+1]
        dp[i]=max(notpick,pick)
    return dp[0]
arr=[2,1,4,9]
print(maximumNonAdjacentSum(arr))