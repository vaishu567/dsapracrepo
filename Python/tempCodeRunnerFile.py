# we don't want to print we want to count:
def subseqkcount(a,op,k):
    if len(a)==0:
        if sum(op)==k:
            return 1
        else:
            return 0  
    # taking s[0]:
    op.append(a[0])
    l=subseqkcount(a[1:],op,k)
    # not taking s[0]
    op.remove(a[0])
    r=subseqkcount(a[1:],op,k)
    return l+r
a=[4,2,5,6,7]

k=14
print(subseqkcount(a,[],k))