def factr(n):
    if n==0:
        return 1
    op=n*factr(n-1)
    return op
# the above fun will return 
# now then main function will print
def factp(k):
    op=factr(k)
    print(op)
factp(3)