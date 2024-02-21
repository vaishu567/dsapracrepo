# recursion:

def mcm(arr,i,j,mini):
    if i==j:
        return 0
    for k in range(i,j):
        steps=arr[i-1]*arr[k]*arr[j]+(mcm(arr,i,k,mini)+mcm(arr,k+1,j,mini))
        mini=min(mini,steps)
    return mini
arr=[10,15,20,25]
n=len(arr)
print(mcm(arr,1,n-1,float('inf')))


# memoization:

def mcmr(arr,i,j,dp):
    if i==j:
        return 0
    if  dp[i][j]!=-1:
        return dp[i][j]
    mini=float('inf')
    for k in range(i,j):
        steps=arr[i-1]*arr[k]*arr[j]+(mcmr(arr,i,k,dp)+mcmr(arr,k+1,j,dp))
        mini=min(mini,steps)
    dp[i][j]=mini
    return  dp[i][j]
arr=[10,15,20,25]

n=len(arr)
dp=[[-1 for i in range(n)]for i in range(n)]
print(mcmr(arr,1,n-1,dp))


# tabulationn:
def mcmr(arr):
    n=len(arr)
    dp=[[-1 for i in range(n+1)]for i in range(n+1)]
    for l in range(n):
        dp[l][l]=0
    for i in range(n-1,0,-1):
        for j in range(i+1,n):
            mini=float('inf')
            for k in range(i,j):
                steps=arr[i-1]*arr[k]*arr[j]+(dp[i][k]+dp[k+1][j])
                mini=min(mini,steps)
            dp[i][j]=mini
    return dp[1][n-1]
arr=[10,15,20,25]
print(mcmr(arr))



