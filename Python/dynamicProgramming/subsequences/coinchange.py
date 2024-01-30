def countWaysToMakeChange(arr,value,index) :
    if index== 0:
        return 1 if value % arr[0] == 0 else 0
        # if arr[0]==value:
        #     return 2
        # elif value==0:
        #     return 1
        # else:
        #     return 0
    nottake=countWaysToMakeChange(arr,value,index-1)
    take=0
    if arr[index]<=value:
        take=countWaysToMakeChange(arr,value-arr[index],index)
    return nottake+take

arr=[1,2,3]
value=4
print(countWaysToMakeChange(arr,value,len(arr)-1))




# memoization:
def countWaysToMake(arr,value,index,dp) :
    if index== 0:
        return 1 if value % arr[0] == 0 else 0
    if dp[index][value]!=-1:
        return dp[index][value]
    nottake=countWaysToMake(arr,value,index-1,dp)
    take=0
    if arr[index]<=value:
        take=countWaysToMake(arr,value-arr[index],index,dp)
    dp[index][value]=nottake+take
    return dp[index][value]

def countWaysToMakeChange(denominations, value):
	# Your code goes here
    n=len(denominations)
    dp=[[-1 for i in range(value+1)] for j in range(n)]
    return countWaysToMake(denominations,value,n-1,dp)

# tabulation:


def countWaysToMakeChange(arr, value):
	# Your code goes here
    n=len(arr)
    dp=[[0 for i in range(value+1)] for j in range(n)]
    for i in range(value+1):
        if i % arr[0] == 0:
            dp[0][i]=1 
    # if index== 0:
    #     return 1 if value % arr[0] == 0 else 0
    # if dp[index][value]!=-1:
    #     return dp[index][value]
    for i in range(1,n):
        for k in range(value+1):
            nottake=dp[i-1][k]
            take=0
            if arr[i]<=k:
                take=dp[i][k-arr[i]]
            dp[i][k]=nottake+take
    print(dp)
    return dp[n-1][value]
arr=[2,5]
value=5
print(countWaysToMakeChange(arr,value))

