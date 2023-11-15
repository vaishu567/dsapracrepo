def getLongestSubarray(nums, k):
    # Write your code here
    sum=0
    maxi=0
    n=len(nums)
    i=0
    for j in range(n):
        sum+=nums[j]
        if k>0:
            while sum>k and i<n and nums[i]!=0:

                sum-=nums[i]
                i+=1
            if sum==k:
                maxi=max(maxi,j-i+1)
        else:
            if sum==k:
                maxi=max(maxi,j-i+1)

    return maxi
k= -2
nums=[-10, 8 ,2, -2]
print(getLongestSubarray(nums,k))