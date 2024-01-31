def recursive(s1,s2,i1,i2):
    if i1<0 or i2<0:
        return 0
    if s1[i1]==s2[i2]:
        return 1+recursive(s1,s2,i1-1,i2-1)
    else:
        return 0+max(recursive(s1,s2,i1-1,i2),recursive(s1,s2,i1,i2-1))

s1="abc"
s2="abaa"
print(recursive(s1,s2,len(s1)-1,len(s2)-1))

# memoization:
def recursive(s1,s2,i1,i2,dp):
    if i1<0 or i2<0:
        return 0
    if dp[i1][i2]!=-1:
        return dp[i1][i2]
    if s1[i1]==s2[i2]:
        dp[i1][i2]= 1+recursive(s1,s2,i1-1,i2-1,dp)
    else:
        dp[i1][i2]= 0+max(recursive(s1,s2,i1-1,i2,dp),recursive(s1,s2,i1,i2-1,dp))
    return dp[i1][i2]

s1="abc"
s2="abaa"
dp=[[-1 for i in range(len(s2))] for j in range(len(s1))]
print(recursive(s1,s2,len(s1)-1,len(s2)-1,dp))

# tabulation:
def recursive(s1,s2):
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
                dp[i1][i2]= 0+max(dp[i1-1][i2],dp[i1][i2-1])
    return dp[n][m]

s1="abc"
s2="abaa"
print(recursive(s1,s2))



