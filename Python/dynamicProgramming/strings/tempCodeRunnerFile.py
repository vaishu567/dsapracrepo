def editdistance(s1,s2):
    n=len(s1)
    m=len(s2)
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=i
    for j in range(m+1):
        dp[0][j]=j
    # return dp
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j]=0+dp[i-1][j-1]
            else:
                # s1="horse" s2="ros"
                # when we are in inserting character we hypothetically assume that a character i.e s2[j] is inserted in string and we move j to  j-1
                insert=1+dp[i][j-1]
                # when we delete a character we hypothetically assume that a character is being deleted from s1 and move i to i-1
                delete=1+dp[i-1][j]
                # when we replace a character in s1 we assume that the character is s2[j] and then we move j to j-1 and i to i-1
                replace=1+dp[i-1][j-1]
                dp[i][j]=min(insert, delete, replace)
    return dp[n][m]
s1="intention"
s2="execution"
print(editdistance(s1,s2))