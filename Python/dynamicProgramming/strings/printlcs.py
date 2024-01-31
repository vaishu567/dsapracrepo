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
    # now we do work to get our string:
    s=""
    i=n
    j=m
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            s+=s1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    return s[::-1]
s1="abcde"
s2="bdgek"
print(recursive(s1,s2))

