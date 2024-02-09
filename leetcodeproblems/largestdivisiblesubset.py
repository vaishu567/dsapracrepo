def largestsubset(nums,n):
    ans=[]
    flag=False
    for i in range(n):
        if len(ans)==0:
            ans.append(nums[i])
        else:
            for k in ans:
                if k%nums[i]==0 or nums[i]%k==0:
                    flag = True
                else:
                    flag=False
            if flag:
                ans.append(nums[i])       
    return ans
nums=[1,2,3]
n=len(nums)
print(largestsubset(nums,n))

# since it is subset we have to try all combinations:






