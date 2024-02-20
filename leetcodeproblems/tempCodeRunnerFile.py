# recursive:
def subarraymin(arr,ind,prev):
    if ind==len(arr):
        return 0
    take=0
    if take==0:
        nottake=0+subarraymin(arr,ind+1,prev)
    if take>=0:
        if take==0:
            prev=ind
        take=min(arr[prev:ind+1])+subarraymin(arr,ind+1,prev)
    return take+nottake
arr=[3,1,2,4]
print(subarraymin(arr,0,-1))