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



def findLeastNumOfUniqueInts(arr, k):
    # first find frequency of each element
    # then for every elemnt with 1 frequency will be eliminated first
    d={}
    n=len(arr)
    count=len(set(arr))
    for i in range(n):
        if arr[i] not in d:
            d[arr[i]]=1
        else:
            d[arr[i]]+=1
    d=dict(sorted(d.items(), key=lambda x:x[1], reverse=False))
    print(d,count)
    for i in d:
        if d[i]==1:
            k-=1
            count-=1
        if k==0:
            return count
        elif k>0 and d[i]>1:
            if k<d[i]:
                k-=1
            elif k>=d[i]:
                k-=d[i]
                count-=1
    return count
arr=[1]
k = 0
print(findLeastNumOfUniqueInts(arr,k))
