def spaceop(n):
    prev2=0
    prev=1
    for i in range(2,n+1):
        curri=prev2+prev
        prev2=prev
        prev=curri
    return prev
print(spaceop(8))