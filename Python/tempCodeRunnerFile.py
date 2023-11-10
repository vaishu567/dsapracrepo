def mergeSort(arr,low,high):
    if low>=high:
        return arr
    mid=(low+high)//2
    mergeSort(arr,low,mid)
    mergeSort(arr,mid+1,high)
    return merger(arr,low,mid,high)

def merger(arr,low,mid,high):
    left=low
    right=mid+1
    temp=[]
    while (left<=mid and right<=high):
        if arr[left]<arr[right]:
            temp.append(arr[left])
            left+=1
        else:
            temp.append(arr[right])
            right+=1
    while left<=mid:
        temp.append(arr[left])
        left+=1
    while right<=high:
        temp.append(arr[right])
        right+=1
    for i in range(low,high+1):
        arr[i]=temp[i-low];
    return arr
arr=[3,1,2,4,1,5,2,6,4]
low=0
high=len(arr)-1
print(mergeSort(arr,low,high))