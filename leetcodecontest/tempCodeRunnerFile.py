recursive(arr,ind,temp,n):
    if ind==n:
        print(temp)
        return len(temp)
    include=float('-inf')
    if havedup(temp,arr[ind]):
        exclude=recursive(arr,ind+1,temp,n)
    else:
        exclude=recursive(arr,ind+1,temp,n)
        include=recursive(arr,ind+1,temp+arr[ind],n)
    return max(include,exclude)

arr = ["un","iq","ue"]
print(recursive(arr,0,"",len(arr)))