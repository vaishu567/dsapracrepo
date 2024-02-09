def largestsubset(nums):
    n=len(nums)
    ans=[]
    for i in range(1,n):
        if len(ans)!=0:
            for k in ans:
                if k%nums[i]==0 or nums[i]%k==0:
                    ans.append(nums[i])
        if len(ans)==0:
            if nums[i]%nums[i-1]==0 or nums[i-1]%nums[i]==0:
                ans.append(nums[i-1])
                ans.append(nums[i])

    return ans
nums=[1,2,3]
print(largestsubset(nums))