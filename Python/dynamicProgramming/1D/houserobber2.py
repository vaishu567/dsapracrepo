# here all houses along the street are arranged in a circle:
# recursion:
def houserob2(arr,index,n):
    if index>=n:
        return 0
    pick=arr[index]+houserob2(arr,index+2,n)
    notpick=0+houserob2(arr,index+1,n)
    return max(pick,notpick)
def main(arr):
    n=len(arr)
    first=houserob2(arr,1,n)
    last=houserob2(arr,0,n-1)
    return max(first,last)
arr=[1,2,3,1,2,3]
print(main(arr))

# using memoization:
def memoization(arr,index,n,dp):
    if index>=n:
        return 0
    if dp[index]!=-1:
        return dp[index]
    pick=arr[index]+memoization(arr,index+2,n,dp)
    notpick=0+memoization(arr,index+1,n,dp)
    dp[index]=max(pick,notpick)
    return dp[index]

def main(arr):
    n=len(arr)
    dp=[-1 for i in range(n+2)]
    first=memoization(arr,1,n,dp)
    dp=[-1 for i in range(n+2)]
    last=memoization(arr,0,n-1,dp)
    return max(first,last)

arr=[1,2,3,1,2,3]
print(main(arr))


# using tabulation:
def tabulation(arr):
    n=len(arr)
    if n==1:
        return arr[0]
    dp=[-1 for i in range(n+3)]
    dp[n]=0
    dp[n+1]=0
    dp[n+2]=0
    # from last to 1
    for i in range(n-1,0,-1):
        pick=arr[i]+dp[i+2]
        notpick=0+dp[i+1]
        dp[i]=max(pick,notpick)
    # from n-2 to 0
    dp2=[-1 for i in range(n+2)]
    dp2[n-1]=0
    dp2[n]=0
    dp2[n+1]=0
    for i in range(n-2,-1,-1):
        pick=arr[i]+dp2[i+2]
        notpick=0+dp2[i+1]
        dp2[i]=max(pick,notpick)
    return max(dp[1],dp2[0])
    # return (dp,dp2)
arr=[200,3,140,20,10]
print(tabulation(arr))
    
    
    

    
    


