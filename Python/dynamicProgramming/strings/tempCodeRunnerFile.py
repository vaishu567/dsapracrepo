def distinctSub(s,sub,i,j,dp):
    if j<0:
        return 1
    if i<0:
        return 0
    if dp[i][j]!=-1:
        return dp[i][j]
    if s[i]==sub[j]:
        dp[i][j]=distinctSub(s,sub,i-1,j-1,dp)+distinctSub(s,sub,i-1,j,dp)
        return dp[i][j]

    else:
        dp[i][j]=distinctSub(s,sub,i-1,j,dp)
        return dp[i][j]
    
s= "brootgroot"
sub= "brt"
n=len(s)
m=len(sub)
dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
print(distinctSub(s,sub,n-1,m-1,dp))  