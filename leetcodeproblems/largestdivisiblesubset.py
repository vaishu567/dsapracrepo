def largestsubset(nums,n,ind,op):
    if ind==n:
        return len(op)
    # nottaking:
    nottake=largestsubset(nums,n,ind+1,op)
    # taking:
    if len(op)!=0:
        for i in op:
            if nums[ind]%i==0 or i%nums[ind]==0: 
                op.append(nums[ind])
    else:
        op.append(nums[ind])
    take=largestsubset(nums,n,ind+1,op)
    return max(take,nottake)
nums=[1,2,3]
n=len(nums)
print(largestsubset(nums,n,0,[]))




