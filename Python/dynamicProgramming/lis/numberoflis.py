# with these we are missing subsequences with similar length while filling dp array:
# we will compute count array along with dp array:
def numberoflis(arr,n):
    dp=[1 for i in range(n)]
    countarr=[1 for i in range(n)]
    maxi=float('-inf')
    for ind in range(n):
        for prev in range(0,ind):
            if arr[prev]<arr[ind] and 1+dp[prev]>dp[ind]:
                dp[ind]=1+dp[prev]
                countarr[ind]=countarr[prev]
            elif arr[prev]<arr[ind] and 1+dp[prev]==dp[ind]:
                countarr[ind]+=countarr[prev]
        maxi=max(maxi,dp[ind])
    
    count=0
    for i in range(n):
        if dp[i]==maxi and maxi!=float('-inf'):
            count+=countarr[i]
    return count
arr=[3 ,18 ,14 ,25 ,1 ,5 ,17 ,2]
n=len(arr)
print(numberoflis(arr,n))
