def swapf(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]
    return arr
def permutations(index,nums,final,op):
    if index==len(nums):
        op=nums
        final.append(list(op))
        return final
    for i in range(index,len(nums)):
        nums=swapf(i,index,nums)
        final=permutations(index+1,nums,final,op)
        nums=swapf(i,index,nums)
    return final
final=[]
op=[]
nums=[1,2,3]
print(permutations(0,nums,final,op))