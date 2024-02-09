def perfectsquares(n,dp):
    if n==0:
        return 0
    mini=float('inf')
    if dp[n]!=-1:
        return dp[n]
    for i in range(1,n):
        if i*i<=n:
            ps=i*i
            ans=1+perfectsquares(n-ps,dp)
            mini=min(mini,ans)
        else:
            break
    dp[n]=mini
    return dp[n]
dp=[-1 for i in range(n)]
print(perfectsquares(12,dp))