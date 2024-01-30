# here the problem is approached as the partition subarray into two arrays with sum diff as d:
def countSubsetsk(arr,k):
    n=len(arr)
    dp=[[0 for _ in range(k+1)] for _ in range(n)]
    if arr[0]==0:
        dp[0][0]=2
    else:
        dp[0][0]=1
    if arr[0]!=0 and arr[0]<=k:
        dp[0][arr[0]]=1
    # return dp
    for i in range(1,n):
        for target in range(k+1):
            nottake=dp[i-1][target]
            take=0
            if arr[i]<=k:
                take=dp[i-1][target-arr[i]]
            dp[i][target]=(take+nottake)
    return dp[n-1][k]


def countPartitions(n, d, arr):
    # write your code here
    totalsum=sum(arr)
    if d>=0:
        k=(totalsum+d)
        if k>0 and k%2==0:
            count=countSubsetsk(arr,k//2)
            return count
        else:
            return 0
    else:
        k=(totalsum-d)
        if k>0 and k%2==0:
            count=countSubsetsk(arr,k//2)
            return count
        else:
            return 0



def targetSum(arr,target):
    n=len(arr)
    count=countPartitions(n,target,arr)
    return count


# 9 -33

arr=[18, 8, 19 ,15, 3 ,24 ,15 ,12 ,1]
print((sum(arr)+33)//2)
target=-33
print(targetSum(arr,target))


