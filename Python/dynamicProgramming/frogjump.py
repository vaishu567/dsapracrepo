# here we they are asking to find min energy required to move from 0th stair to nth stair:
# we need to find all possible ways using recursion becoz using greedy we will miss out in some cases:
# recursive code:
def frogjump(index,heights,left,right):
    if index==0:
        return 0
    left=(frogjump(index-1,heights,left,right))+abs(heights[index]-heights[index-1])
    if index>1:
        right=(frogjump(index-2,heights,left,right))+abs(heights[index]-heights[index-2])
    return min(left,right)
heights=[30,10,60,10,60,50]
left=float('inf')
right=float('inf')
print(frogjump(len(heights)-1,heights,left,right))
# intoducinng dp:
# memoization:
# instead of calling subfunctions we are using memoization:
# top-down:
def memoization(index,heights,left,right,dp):
    dp[0]=0
    if dp[index]!=-1:
        return dp[index]
    left=memoization(index-1,heights,left,right,dp)+abs(heights[index]-heights[index-1])
    if index>1:
        right=memoization(index-2,heights,left,right,dp)+abs(heights[index]-heights[index-2])
    dp[index]=min(left,right)
    return dp[index]
heights=[30,10,60,10,60,50]
left=float('inf')
right=float('inf')
dp=[-1 for i in range(len(heights))]
print(memoization(len(heights)-1,heights,left,right,dp))

# tabulation:
# bottom-up:
# here we are converting recursion call into loops:so that we can avoid S.C(N) for recursion stack space:
# and we are lopping from the bottom to top:
def tabulation(index,heights,left,right,dp):
    dp[0]=0
    for i in range(1,len(heights)):
        left= dp[i-1]+abs(heights[i]-heights[i-1])
        if i>1:
            right= dp[i-2]+abs(heights[i]-heights[i-2])
        dp[i]=min(left,right)
    return dp[index]
heights=[30,10,60,10,60,50]
left=float('inf')
right=float('inf')
dp=[-1 for i in range(len(heights))]
print(tabulation(len(heights)-1,heights,left,right,dp))



# if in question its like index-1 or index-2 then ther's alwasys be a space optimization technique-Thumb rule:
# space optimization:
def frogJump(n, heights):
    # Write your code here.
    right=float('inf')
    left=float('inf')
    prev=0
    prev2=0
    for i in range(1,n):
        left=prev+abs(heights[i]-heights[i-1])
        if i>1:
            right=prev2+abs(heights[i]-heights[i-2])
        curr=min(right,left)
        prev2=prev
        prev=curr
    return prev
heights=[30,10,60,10,60,50]
left=float('inf')
right=float('inf')
n=len(heights)
print(frogJump(n,heights))



