def distinctSub(s,t,sub,ind):
    if ind==len(s):
        if t==sub:
            return 1
        else:
            return 0
    # nottake:
    nottake=distinctSub(s,t,sub,ind+1)
    # take:
    t+=s[ind]
    take=distinctSub(s,t,sub,ind+1)
    return take+nottake
s= "brootgroot"
sub= "brt"
t=""
ind=0
print(distinctSub(s,t,sub,ind))

# another way :
def distinctSub(s,sub,i,j):
    if j<0:
        return 1
    if i<0:
        return 0
    if s[i]==sub[j]:
        return distinctSub(s,sub,i-1,j-1)+distinctSub(s,sub,i-1,j)
    else:
        return distinctSub(s,sub,i-1,j)
    
s= "brootgroot"
sub= "brt"
print(distinctSub(s,sub,len(s)-1,len(sub)-1))  

# memoization:
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

# tabulation:
def distinctSub(s,sub):
    n=len(s)
    m=len(sub)
    dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=1
    # we have to start from j>0 because we have already written for j=0 condition
    for j in range(1,m+1):
        dp[0][j]=0   
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s[i-1]==sub[j-1]:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][m]
    