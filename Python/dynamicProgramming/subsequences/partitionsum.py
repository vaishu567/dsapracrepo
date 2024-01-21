# HERE WE HAVE TO DIVIDE THE ARRAY INTO 2 SUBSETS:
# here if we calculate total sum of array if sum is odd we cannot divide into 2 subsets with equal sum
# but if we have sum as even then we can divide it into 2 subsets with equal sum
# so S=sum(arr) ad we  take S//2 if S%2==0
# now our sum of subset should be equal to S//2 i.e our nnew target
def recurpartition(arr,index,S):
    if S==0:
        return True
    if index==0:
        return (arr[0]==S)
    nottake=recurpartition(arr,index-1,S)
    take=False
    if arr[index]<=S:
        take=recurpartition(arr,index-1,S-arr[index])
    return (take or nottake)
def canPartition(arr, n):
    # Write your code here.
    S=sum(arr)
    if  S%2!=0:
        return False
    else:
        S=S//2
        return recurpartition(arr,n-1,S)
arr=[2, 3, 3, 3, 4, 5]
n=len(arr)
print(canPartition(arr,n))

# memoization:
def recurpartition(arr,index,S,dp):
    if S==0:
        return True
    if index==0:
        return (arr[0]==S)
    if dp[index][S]!=-1:
        return dp[index][S]
    nottake=recurpartition(arr,index-1,S,dp)
    take=False
    if arr[index]<=S:
        take=recurpartition(arr,index-1,S-arr[index],dp)
    dp[index][S]=(take or nottake)
    return dp[index][S]
def canPartition(arr, n):
    # Write your code here.
    S=sum(arr)
    if  S%2!=0:
        return False
    else:
        S=S//2
        dp=[[-1 for i in range(S+1)] for j in range(n)]
        return recurpartition(arr,n-1,S,dp)



arr=[2, 3, 3, 3, 4, 5]
n=len(arr)
print(canPartition(arr,n))


# tabulation:

def canPartition(arr, n):
    # Write your code here.
    S=sum(arr)
    if  S%2!=0:
        return False
    else:
        target=S//2
        dp=[[0 for i in range(target+1)] for j in range(n)]
        for i in range(n):
            dp[i][0]=True
        if arr[0]<=target:
            dp[0][arr[0]]=True
        for index in range(1,n):
            for S in range(1,target+1):
                nottake=dp[index-1][S]
                take=False
                if arr[index]<=S:
                    take=dp[index-1][S-arr[index]]
                dp[index][S]=(take or nottake)
        return dp
arr=[2, 3, 3, 3, 4, 5]
n=len(arr)
print(canPartition(arr,n))
