def subrec(arr,op):
    if len(arr)==0:
        # result.append(list(op))
        print(op)
        return
        # return result
    # not taking:
    op.append(arr[0])
    subrec(arr[1:],op)
    op.remove(arr[0])
    subrec(arr[1:],op)
arr=[1,2,1]
op=[]
# result=[]
print(subrec(arr,op))