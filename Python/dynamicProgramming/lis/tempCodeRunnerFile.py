def longestincreasingsub(arr,n,ind,prev,dp):
    if ind==n:
        return 0
    if dp[ind][prev]!=-1:
        return dp[ind][prev]
    nottake=0+longestincreasingsub(arr,n,ind+1,prev,dp)
    take=float('-inf')
    if prev==-1 or arr[ind]>arr[prev]:
        take=1+longestincreasingsub(arr,n,ind+1,ind,dp)
    dp[ind][prev]= max(take,nottake)
    return dp
arr=[5,4,11,1,16,8]
n=len(arr)
dp=[[-1 for i in range(n+1)] for i in range(n)]
print(longestincreasingsub(arr,n,0,-1,dp))