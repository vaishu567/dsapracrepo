def missingNumber( nums):
    n=len(nums)
    # sumap=(n*(n+1))//2
    # sumi=sum(nums)
    # return sumap-sumi        
    xor1=0
    xor2=0
    for i in range(n):
        xor1=xor1^nums[i]
        xor2=xor2^(i+1)
    xor2=xor2^(n+1)
    return xor1^xor2
nums=[1,2,4,5]
print(missingNumber(nums))