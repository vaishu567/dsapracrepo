def reversed(n):
    temp=n
    rev=""
    while temp>0:
        rem=str(temp%10)
        rev+=rem
        temp=temp//10
    if rev==str(n):
        return True
    return False
print(reversed(12321))