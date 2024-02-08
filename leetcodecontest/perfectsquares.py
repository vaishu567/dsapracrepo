def issquare(i):
    if i==1:
        return True
    for k in range(2,(i//2)+1):
        if k*k==i:
            return True
    return False
print(issquare(9))
# print(12/4)
# recursion:
def perfectsquares(n):
    if n==0:
        return 0
    mini=float('inf')
    i=1
    while i*i<=n:
        ps=i*i
        ans=1+perfectsquares(n-ps)
        mini=min(mini,ans)
        i+=1
    return mini

print(perfectsquares(12))
# memoization:
def perfectsquares(n,dp):
    if n==0:
        return 0
    mini=float('inf')
    if dp[n]!=-1:
        return dp[n]
    i=1
    while i*i<=n:
        ps=i*i
        ans=1+perfectsquares(n-ps,dp)
        mini=min(mini,ans)
        i+=1
    dp[n]=mini
    print(dp)
    return dp[n]

n=12
dp=[-1 for i in range(n+1)]
print(perfectsquares(n,dp))

# tabulation:
def perfectsquares(n):
    dp=[float('inf') for i in range(n+1)]
    dp[0]=0
    for ind in range(1,n+1):
        mini=float('inf')
        i=1
        while i*i<=ind:
            ps=i*i
            ans=1+dp[ind-ps]
            mini=min(mini,ans)
            i+=1
        dp[ind]=mini
        print(dp)
    return dp[n]

n=12
print(perfectsquares(n))

    


    
        
