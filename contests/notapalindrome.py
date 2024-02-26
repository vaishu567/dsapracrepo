def distributeCandies(arr, n):
    # code here
    arr.sort()
    count=0
    for i in range(n):
        if arr[i]==1 or arr[i]==0:
            continue
        else:
            divi=arr[i]
            break
    for i in range(n):
        if arr[i]%divi!=0:
            arr[i]+=1
            count+=1
    return count
# 8
# 7 8 7 1 2 1 9 2
arr=[7,8,7,1,2,1,9,2]
n=len(arr)
print(distributeCandies(arr, n))
