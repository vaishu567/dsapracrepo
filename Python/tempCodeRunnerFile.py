def firstoccarr(arr,x,s,e,n):
    if s>e and s!=n:
        return s
    mid=(s+e)//2
    if arr[mid]>=x:
        e=mid-1
        return firstoccarr(arr,x,s,e,n)
    else:
        s=mid+1
        return firstoccarr(arr,x,s,e,n)
arr=[1,2,3,3,3,4,4,4,5,6]
x=8
s=0
e=len(arr)-1
n=len(arr)
print(firstoccarr(arr,x,s,e,n))