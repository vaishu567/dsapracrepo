# longest common prefix:
def commonPrefix(arr: List[str], n: int) -> str:
    # Write your code here
    # bruteforce:
    pre=-1
    for i in range(len(arr[0])):
        prefix=arr[0][0:i+1]
        for j in range(1,n):
            if arr[j][0:i+1]!=prefix:
                return pre   
        pre=prefix
    return pre

print(26%7)
print((7*(8))//2)