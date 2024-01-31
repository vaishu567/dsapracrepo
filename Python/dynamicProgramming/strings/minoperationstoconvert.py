# here we are finding longest common subsequence in two strings and then we are calculating no of deletions and no of insertions:
# no of deletions= length of s1- len of common subsequence 
# no of insertions= length of s2- len of common subsequence


def canYouMake(s1,s2):
    # write your code here
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
    noofdeletions=(n-dp[n][m])
    noofinsertions=(m-dp[n][m])
    return (noofdeletions+noofinsertions)
s1="abcd"
s2="anc"
print(canYouMake(s1,s2))
