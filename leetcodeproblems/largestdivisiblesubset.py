def largestsubset(nums,n):
    for i in range(n):
        if len(ans)==0:
            ans.append(nums[i])
        else:
            while k>=0:
                if ans[k]%nums[i]==0 or nums[i]%ans[k]==0:
                    i+=1
                else:
                    break
            ans.append(nums[i])
    return ans
nums=[1,2,3]
n=len(nums)
print(largestsubset(nums,n))





