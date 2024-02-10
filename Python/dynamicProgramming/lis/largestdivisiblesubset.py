def largestdivisiblest(arr,n,ind):
    if ind==n:
        return 0
    nottake=0+largestdivisiblest(arr,n,ind+1)
    take=0
    for i in range(ind):
        if arr[i]%arr[ind]==0 or arr[ind]%arr[i]==0:
            take=1+largestdivisiblest(arr,n,ind+1)
    return max(take,nottake)
arr=[1,2,4,8]
print(largestdivisiblest(arr,len(arr),0))







