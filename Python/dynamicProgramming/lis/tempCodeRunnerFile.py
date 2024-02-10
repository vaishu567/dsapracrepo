
# lowerbound using binary search:
def lowerbbounnd(arr,t):
    s=0
    n=len(arr)
    e=n-1
    mid=(s+e)//2
    lowerb=n
    while s<=e:
        if arr[mid]>t:
            lowerb=min(lowerb,mid)
            e=mid-1
        elif arr[mid]<t:
            s=mid+1
        else:
            lowerb=min(lowerb,mid)
            e=mid-1
    return lowerb
# using binary search:
def longestincreasingsub(arr,n):
    # fist we declare dp[n]:
    final=[]
    final.append(arr[0])
    for i in range(1,n):
        if arr[i]>final[-1]:
            final.append(arr[i])
        else:
            ind=lowerbbounnd(arr,arr[i])
            final[ind]=arr[i]
    return len(final)


arr=[5,4,11,1,16,8]
n=len(arr)
print(longestincreasingsub(arr,n))