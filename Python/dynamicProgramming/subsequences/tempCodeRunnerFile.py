def countSubsetsk(arr,k,index):
    if k==0:
        return 1
    if index==len(arr):
        if k==0:
            return 1
        else:
            return 0     
    if dp[index][k]!=-1:
        return dp[index][k]
    nottake=countSubsetsk(arr,k,index+1)
    take=0
    if arr[index]<=k:
        take=countSubsetsk(arr,k-arr[index],index+1)
    dp[index][k]=take+nottake
    return dp[index][k]



arr=[1,4,4,5]
k=5
dp=[[-1 for _ in range(k+1)] for _ in range(len(arr))]
print(countSubsetsk(arr,k,0))