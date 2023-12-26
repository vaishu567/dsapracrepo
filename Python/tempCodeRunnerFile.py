def subrec(arr,op):
    if len(arr)==0:
        print(op)
        return 
    # not taking:
    op.append(arr[0])
    subrec(arr[1:],op)
    op.remove(arr[0])
    subrec(arr[1:],op)
arr=[5,6,7,8,9,10]
op=[]
print(subrec(arr,op))