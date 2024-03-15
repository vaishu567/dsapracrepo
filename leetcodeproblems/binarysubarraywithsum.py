def recursub(array,goal,ind,n,op):
    if ind==n:
        if sum(op)==goal:
            return 1
        return 0
    # take:
    op.append(array[ind])
    take=recursub(array,goal,ind+1,n,op)
    # nottake:
    op.remove(array[ind])
    nottake=recursub(array,goal,ind+1,n,op)
    return take+nottake
nums = [1,0,1,0,1]
n=len(nums)
goal=2
print(recursub(nums,goal,0,n,[]))

