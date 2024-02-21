def cutstick(cuts,i,j):
    if i>j:
        return 0
    mini=float('inf')
    for k in range(i,j+1):
        costs=(cuts[j+1]-cuts[i-1])+(cutstick(cuts,i,k-1)+cutstick(cuts,k+1,j))
        mini=min(mini,costs)
    return mini

def main(n,cuts):
    m=len(cuts)
    new=[0]+cuts+[n]
    new.sort()
    return cutstick(new,1,m)
cuts=[1,3]
n=4
print(main(n,cuts))

#memoization:
def cutstick(cuts,i,j,dp):
    if i>j:
        return 0
    mini=float('inf')
    if dp[i][j]!=-1:
        return dp[i][j]
    for k in range(i,j+1):
        costs=(cuts[j+1]-cuts[i-1])+(cutstick(cuts,i,k-1,dp)+cutstick(cuts,k+1,j,dp))
        mini=min(mini,costs)
    dp[i][j] =mini
    return dp[i][j]

def main(n,cuts):
    m=len(cuts)
    new=[0]+cuts+[n]
    new.sort()
    dp=[[-1 for i in range(n+1)]for i in range(n+1)]
    return cutstick(new,1,m,dp)
cuts=[1,3]
n=4
print(main(n,cuts))

# tabulation:
def main(n,cuts,c):
    cuts=[0]+cuts+[n]
    cuts.sort()
    dp=[[0 for i in range(c+2)]for i in range(c+2)]
    for i in range(c,0,-1):
        for j in range(1,c+1):
            if i>j:
                continue
            mini=float('inf')
            for k in range(i,j+1):
                costs=(cuts[j+1]-cuts[i-1])+(dp[i][k-1]+dp[k+1][j])
                mini=min(mini,costs)
            dp[i][j] =mini
    return dp[1][c]
cuts=[1,3]
n=4
print(main(n,cuts,2))