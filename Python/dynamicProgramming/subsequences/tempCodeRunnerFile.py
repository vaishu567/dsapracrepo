def minimumElements(num,x):
    # if index==0:
    #     if x%num[index]==0:
    #         return x//num[index]
    #     else:
    #         return 1e9
    n=len(num)
    dp=[[-1 for _ in range(x+1)] for _ in range(n)]
    for i in range(x+1):
        if i%num[0]==0:
            dp[0][i]=i//num[0]
        else:
            dp[0][i]=1e9
    # print(dp)
    for i in range(1,n):
        for j in range(x+1):
            nottake=0+dp[i-1][j]
            take=float('inf')
            if num[i]<=j:
                take=1+dp[i][j-num[i]]
            # print(take,nottake)
            dp[i][j]=min(take,nottake)
    print(dp)
    return dp[n-1][x]
num=[1,2,3]
x=7
print(minimumElements(num,x))