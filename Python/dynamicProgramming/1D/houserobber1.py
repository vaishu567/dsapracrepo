# maxsum of non-adjacent subseq:
# generating non-adjacent subse:
def maxsum(index,arr,maxisum,op,final):
    if index>=len(arr):
        final.append(list(op))
        return final
    # taking s[0]
    op.append(arr[index])
    final=maxsum(index+2,arr,maxisum,op,final)
    op.remove(arr[index])
    final=maxsum(index+1,arr,maxisum,op,final)
    return final
arr=[2,1,4,9]
index=0
maxisum=0
op=[]
final=[]
print(maxsum(index,arr,maxisum,op,final))


# maxisum:recursive:
def maxsum(index,arr,maxisum,op):
    if index>=len(arr):
        maxisum=max(sum(op),maxisum)
        return maxisum
    # taking s[0]
    op.append(arr[index])
    maxisum=maxsum(index+2,arr,maxisum,op)
    op.remove(arr[index])
    maxisum=maxsum(index+1,arr,maxisum,op)
    return maxisum
arr=[2,1,4,9]
index=0
maxisum=0
op=[]
print(maxsum(index,arr,maxisum,op))

# in case of dp:
def maxsum(index,arr):
    if index >= len(arr):
        return 0
    # taking s[0]
    pick=arr[index]+ maxsum(index+2,arr)
    notpick=0+maxsum(index+1,arr)
    return max(notpick,pick)
arr=[2,1,4,9]
index=0
print(maxsum(index,arr))



# memoization:
def maxsum(index,arr,dp):
    if index >= len(arr):
        dp[index]=0
        return dp[index]
    # taking s[0]
    if dp[index]!=-1:
        return dp[index]
    pick=arr[index]+ maxsum(index+2,arr,dp)
    notpick=0+maxsum(index+1,arr,dp)
    dp[index]=max(notpick,pick)
    return dp[index]

def maximumNonAdjacentSum(nums):    
    # Write your code here.
    index=0
    dp=[-1 for i in range(len(nums)+2)]
    return maxsum(index,arr,dp)


# tabulation:
def maximumNonAdjacentSum(nums):    
    # Write your code here.
    dp=[-1 for i in range(len(nums)+3)]
    dp[len(nums)]=0
    dp[len(nums)+1]=0
    dp[len(nums)+2]=0
    for i in range(len(nums)-1,-1,-1):
        pick=arr[i]+ dp[i+2]
        notpick=0+dp[i+1]
        dp[i]=max(notpick,pick)
    return dp[0]
arr=[2,1,4,9]
print(maximumNonAdjacentSum(arr))


    


    
# space optimization:



    