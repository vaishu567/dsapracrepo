def main(n,cuts,c):
    new=[0]+cuts+[n]
    new.sort()
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