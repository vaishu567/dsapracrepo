# to determine the longest bitonic we  have to find lis from front and back:
# using dp table from lis we can add and subtract 1 from every lis index:
def longestbitonic(arr,n):
     # fist we declare dp[n]:
    dp=[1 for i in range(n)]
    dp2=[1 for i in range(n)]
    for ind in range(n):
        for prev in range(0,ind):
            if arr[prev]<arr[ind]:
                dp[ind]=max(1+dp[prev],dp[ind])
    for ind in range(n-1,-1,-1):
        for prev in range(n-1,ind-1,-1):
            if arr[prev]<arr[ind]:
                dp2[ind]=max(1+dp2[prev],dp2[ind])
    maxi=float('-inf')
    for i in range(n):
        maxi=max(maxi,(dp[i]+dp2[i]-1))
    return maxi