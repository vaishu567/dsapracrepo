# You are given an array of ‘N’ distinct integers and an integer ‘X’ representing the target sum. You have to tell the minimum number of elements you have to take to reach the target sum ‘X’.

# Note:
# You have an infinite number of elements of each type.
# For example
# If N=3 and X=7 and array elements are [1,2,3]. 
# Way 1 - You can take 4 elements  [2, 2, 2, 1] as 2 + 2 + 2 + 1 = 7.
# Way 2 - You can take 3 elements  [3, 3, 1] as 3 + 3 + 1 = 7.
# Here, you can see in Way 2 we have used 3 coins to reach the target sum of 7.
# Hence the output is 3.
def minimumElements(num, x, index):
    if index==0:
        if x%num[index]==0:
            return x//num[index]
        else:
            return 1e9
    nottake=0+minimumElements(num,x,index-1)
    take=float('inf')
    if num[index]<=x:
        take=1+minimumElements(num,x-num[index],index)
    print(take,nottake)
    return min(take,nottake)
num=[1,2,3]
x=7
n=len(num)
index=n-1
print(minimumElements(num,x,index))


# memoization:
def minimumElements(num, x, index,dp):
    if index==0:
        if x%num[index]==0:
            return x//num[index]
        else:
            return 1e9
    if dp[index][x]!=-1:
        return dp[index][x]
    nottake=0+minimumElements(num,x,index-1,dp)
    take=float('inf')
    if num[index]<=x:
        take=1+minimumElements(num,x-num[index],index,dp)
    # print(take,nottake)
    dp[index][x]=min(take,nottake)
    print(dp)
    return dp[index][x]
num=[1,2,3]
x=7
n=len(num)
index=n-1
dp=[[-1 for _ in range(x+1)] for _ in range(n)]
print(minimumElements(num,x,index,dp))


# tabulation:
def minimumElements(num,x):
    # if index==0:
    #     if x%num[index]==0:
    #         return x//num[index]
    #     else:
    #         return 1e9
    n=len(num)
    dp=[[0 for _ in range(x+1)] for _ in range(n)]
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


    
