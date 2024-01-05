def recursi(indx,arr,final,op):
    final.append(list(op))
    for i in range(indx,len(arr)):
        if i>indx and arr[i]==arr[i-1]:
            continue
        op.append(arr[i])
        final=recursi(i+1,arr,final,op)
        op.remove(arr[i])
    return final

def subsetsWithDup(nums):
    # write the code  logic here !!! 
    final=[]
    op=[]
    fin=recursi(0,nums,final,op)
    return fin
nums=[12,15,20]
print(subsetsWithDup(nums))