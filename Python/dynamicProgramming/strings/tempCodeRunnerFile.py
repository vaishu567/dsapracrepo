    n=len(s1)
    m=len(s2)
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for j in range(m+1):
        dp[0][j]=0
    for i1 in range(1,n+1):
        for i2 in range(1,m+1):               
            if s1[i1-1]==s2[i2-1]:
                dp[i1][i2]= 1+dp[i1-1][i2-1]
            else:
                dp[i1][i2]= 0
    maxi=float('-inf')
    for i in range(n+1):
        for j in range(m+1):
            maxi=max(maxi,dp[i][j])
    return maxi