def recursubseq(arr,i,op):
    if i==len(arr):
        xor=0
        for j in op:
            xor=xor^j
        if xor%2==0 and op:
            return 1
        else:
            return 0
    # taking s[0]
    op.append(arr[i])
    take=(recursubseq(arr,i+1,op))
    op.remove(arr[i])
    nottake=(recursubseq(arr,i+1,op))
    print(take,nottake)
    return take+nottake


def attractiveGroups(n, a):
    # Write your code here.
    op=[]
    # dp=[-1 for i in range(n+1)]
    if len(a)==1:
        if a[0]%2!=0:
            return 0
        else:
            return 1
    return (recursubseq(a,0,op))%(10**9+7)
arr=[1,1,2]
n=len(arr)
print(attractiveGroups(n,arr))


# memoization:
def recursubseq(arr,i,op):
    if i==len(arr):
        xor=0
        for j in op:
            xor=xor^j
        if xor%2==0 and op:
            return 1
        else:
            return 0
    # taking s[0]
    op.append(arr[i])
    take=recursubseq(arr,i+1,op)
    op.remove(arr[i])
    nottake=recursubseq(arr,i+1,op)
    print(take,nottake)
    return take+nottake


def attractiveGroups(n, a):
    # Write your code here.
    op=[]
    # dp=[-1 for i in range(n+1)]
    if len(a)==1:
        if a[0]%2!=0:
            return 0
        else:
            return 1
    return (recursubseq(a,0,op))%(10**9+7)
arr=[1,1,2]
n=len(arr)
print(attractiveGroups(n,arr))