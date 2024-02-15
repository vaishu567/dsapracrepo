def maxiperi(nums):
    nums.sort()
    # return nums
    if len(nums)<3:
        return -1
    sumi=0
    maxi=float('-inf')
    for i in range(len(nums)):
        if i<2:
            sumi+=nums[i]
        if i>=2 and sumi>nums[i]:
            maxi=max(sumi+nums[i],maxi)
        if i>=2:
            sumi+=nums[i]
    if maxi==float('-inf'):
        return -1
    return maxi
nums=[1,12,1,2,5,50,3]
#[1, 1, 2, 3, 5, 12, 50]
#[1,2,4,7,12,24,74]
print(maxiperi(nums))