def recursive(price,n,index,a):
    if n==0 or index==len(price):
        return 0
    nottake=recursive(price,n,index+1,a)
    take=float('-inf')
    if a[index]<=n:
        take=price[index]+recursive(price,n-a[index],index,a)
    # print(take,nottake)
    return max(take,nottake)
# if we consider n as 1,2,3,----n as pieces of rod and we need to collect them to make len n 
# then this problem will be similar to knapsack
price=[2,5,7,8,10]
n=len(price)
a=[i+1 for i in range(n)]
print(recursive(price,n,0,a))

# memoization:
def recursive(price,n,index,a,dp):
    if n==0 or index==len(price):
        return 0
    if dp[index][n]!=-1:
        return dp[index][n]
    nottake=recursive(price,n,index+1,a,dp)
    take=float('-inf')
    if a[index]<=n:
        take=price[index]+recursive(price,n-a[index],index,a,dp)
    # print(take,nottake)
    dp[index][n]=max(take,nottake)
    return dp[index][n]
# if we consider n as 1,2,3,----n as pieces of rod and we need to collect them to make len n 
# then this problem will be similar to knapsack
price=[2,5,7,8,10]
n=len(price)
a=[i+1 for i in range(n)]
dp=[[-1 for i in range(n+1)] for j in range(n)]
print(recursive(price,n,0,a))

    