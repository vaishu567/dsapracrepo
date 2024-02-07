def wildcard(pattern, text,i,j):
    # Write your code here.
    n=len(pattern)
    m=len(text)
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
    # base cases:
    dp[0][0]=True
    for j in range(1,m+1):
        dp[0][j]=False
    return dp
    # if j<0 and i>=0:
    # # if s1 is left it has to be all * only because only all * represent empty string:
    #     for k in range(0,i+1):
    #         if pattern[k]!="*":
    #             return False
    #     return True
    # # actual code:
    # if (pattern[i]==text[j] or pattern[i]=="?"):
    #     dp[i][j]= wildcard(pattern,text,i-1,j-1,dp)
    # elif pattern[i]=="*":
    #     dp[i][j]=(wildcard(pattern,text,i-1,j,dp) or wildcard(pattern,text,i,j-1,dp))
    # else:
    #     dp[i][j]=False
    # return dp[i][j]

# pattern="ab*cd"
# text="abdefcd"
pattern="ab?d"
text="abcc"
n=len(pattern)
m=len(text)
print(wildcard(pattern,text,n-1,m-1))