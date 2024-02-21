def burstballoon(arr,i,j):
    if i>j:
        return 0
    maxi=float('-inf')
    for ind in range(i,j+1):
        cost=(arr[i-1]*arr[ind]*arr[j+1])+(burstballoon(arr,i,ind-1)+burstballoon(arr,ind+1,j))
        maxi=max(maxi,cost)
    return maxi
arr=[1,5,2,6,9,1]
i=1
j=len(arr)-2
print(burstballoon(arr,i,j))

# memoization:
def burstballoon(arr,i,j,dp):
    if i>j:
        return 0
    maxi=float('-inf')
    if dp[i][j]!=-1:
        return dp[i][j]
    for ind in range(i,j+1):
        cost=(arr[i-1]*arr[ind]*arr[j+1])+(burstballoon(arr,i,ind-1,dp)+burstballoon(arr,ind+1,j,dp))
        maxi=max(maxi,cost)
    dp[i][j]=maxi
    return dp[i][j]
arr=[5,2,6,9]
arr=[1]+arr+[1]
n=len(arr)
i=1
j=n-2
dp=[[-1 for i  in range(n)]for i in range(n)]
print(burstballoon(arr,i,j,dp))

# tabulation:
def burstballoon(arr):
    n=len(arr)
    arr=[1]+arr+[1]
    dp=[[0 for i  in range(n+2)]for i in range(n+2)]
    for i in range(n,0,-1):
        for j in range(1,n+1):
            if i>j:
                continue
            maxi=float('-inf')
            for ind in range(i,j+1):
                cost=(arr[i-1]*arr[ind]*arr[j+1])+(dp[i][ind-1]+dp[ind+1][j])
                maxi=max(maxi,cost)
            dp[i][j]=maxi
    return dp[1][n]
arr=[5,2,6,9]
print(burstballoon(arr))

