# recursion:
# T.C=O(2*N)
# S.C=O(N)
def subsetk(arr,op,final,k):
    if len(arr) == 0:
        if sum(op)==k:
            final.append(list(op))
        return final
    # taking s[0]
    op.append(arr[0])
    final=subsetk(arr[1:],op,final,k)
    op.remove(arr[0])
    final=subsetk(arr[1:],op,final,k)
    return final
arr=[1,2,3,4]
k=4
op=[]
final=[]
print(subsetk(arr,op,final,k))


# boolean recursion:
def subsetk(arr,index,target):
    if target==0:
        return True
    if index==0:
        return (arr[0]==target)
    nottake=subsetk(arr,index-1,target)
    take=False
    if target>=arr[index]:
        take=subsetk(arr,index-1,target-arr[index])
    return (take or nottake)
    
arr=[1,2,3,4]
n=len(arr)
k=4
print(subsetk(arr,n-1,k))



# boolean memoization:
def subsetk(arr,index,target,dp):
    if target==0:
        return True
    if index==0:
        return (arr[0]==target)
    if dp[index][target]!=-1:
        return dp[index][target]
    nottake=subsetk(arr,index-1,target,dp)
    take=False
    if target>=arr[index]:
        take=subsetk(arr,index-1,target-arr[index],dp)
    dp[index][target]=(take or nottake)
    return dp[index][target]
    # return dp
arr=[1,2,3,1]
n=len(arr)
k=4
dp=[[-1 for i in range(k+1)] for i in range(n)]
print(subsetk(arr,n-1,k,dp))



# tabulation:
# T.C=O(N^K)
# S.C=O(N^K)
def subsetk(arr,k):
    n=len(arr)
    dp=[[False for i in range(k+1)] for i in range(n)]
    for i in range(n):
        dp[i][0]=True
    if arr[0]<=k:
        dp[0][arr[0]]=True
    # return dp
    for index in range(1,n):
        for target in range(1,k+1):
            nottake=dp[index-1][target]
            take=False
            if target>=arr[index]:
                take=dp[index-1][target-arr[index]]
            dp[index][target]=(take or nottake)
    return dp[index][target]
arr=[1,2,3,1]
k=4
print(subsetk(arr,k))