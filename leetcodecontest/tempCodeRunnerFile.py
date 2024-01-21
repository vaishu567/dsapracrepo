def recursivefun(arr,index,op,final):
    if index==len(arr):
        final.append(list(op))
        return final
    op.append(arr[index])
    final=recursivefun(arr,index+1,op,final)
    op.remove(arr[index])
    final=recursivefun(arr,index+1,op,final)
    # print(take,nottake)
    return final
arr = [1,2,3,12]
index=0
print(recursivefun(arr,index,[],[]))