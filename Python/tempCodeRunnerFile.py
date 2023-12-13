def staircase(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    x=staircase(n-1)
    y=staircase(n-2)
    z=staircase(n-3)
    return x+y+z
print(staircase(4))