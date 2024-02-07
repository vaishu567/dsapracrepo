def wildcard(pattern, text,i,j):
    # Write your code here.
    # base cases:
    if i<0 and j<0:
        return True
    if i<0 and j>=0:
        return False
    if j<0 and i>=0:
    # if s1 is left it has to be all * only because only all * represent empty string:
        for k in range(0,i+1):
            if pattern[k]!="*":
                return False
        return True
    # actual code:
    if (pattern[i]==text[j] or pattern[i]=="?"):
        return wildcard(pattern,text,i-1,j-1)
    elif pattern[i]=="*":
        return (wildcard(pattern,text,i-1,j) or wildcard(pattern,text,i,j-1))
    return False

# pattern="ab*cd"
# text="abdefcd"
pattern="ab?d"
text="abcc"
n=len(pattern)
m=len(text)
print(wildcardMatching(pattern,text,n-1,m-1))

# memoization:
def wildcard(pattern, text,i,j,dp):
    # Write your code here.
    # base cases:
    if i<0 and j<0:
        return True
    if i<0 and j>=0:
        return False
    if j<0 and i>=0:
    # if s1 is left it has to be all * only because only all * represent empty string:
        for k in range(0,i+1):
            if pattern[k]!="*":
                return False
        return True
    # memoization check:
    if dp[i][j]!=-1:
        return dp[i][j]
    # actual code:
    if (pattern[i]==text[j] or pattern[i]=="?"):
        dp[i][j]= wildcard(pattern,text,i-1,j-1,dp)
    elif pattern[i]=="*":
        dp[i][j]=(wildcard(pattern,text,i-1,j,dp) or wildcard(pattern,text,i,j-1,dp))
    else:
        dp[i][j]=False
    return dp[i][j]

# pattern="ab*cd"
# text="abdefcd"
pattern="ab?d"
text="abcc"
n=len(pattern)
m=len(text)
dp=[[-1 for i in range(m)] for j in range(n)]
print(wildcard(pattern,text,n-1,m-1,dp))

# tabulation:
def isAllStars(S1, i):
    # Helper function to check if all characters up to index i in S1 are '*'
    for j in range(1, i + 1):
        if S1[j - 1] != '*':
            return False
    return True
def wildcard(pattern,text):
    # Write your code here.
    n=len(pattern)
    m=len(text)
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
    # base cases:
    dp[0][0]=True
    for j in range(1,m+1):
        dp[0][j]=False
    for i in range(1,n+1):
        dp[i][0]=isAllStars(pattern,i)
    for i in range(1,n+1):
        for j in range(1,m+1):
            # actual code:
            if (pattern[i-1]==text[j-1] or pattern[i-1]=="?"):
                dp[i][j]= dp[i-1][j-1]
            elif pattern[i-1]=="*":
                dp[i][j]=(dp[i-1][j] or dp[i][j-1])
            else:
                dp[i][j]=False
            return dp[i][j]

# pattern="ab*cd"
# text="abdefcd"
pattern="ab?d"
text="abcc"
print(wildcard(pattern,text))