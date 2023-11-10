# selectionsort:
def selectionSort(arr):
    n=len(arr)
    for i in range(n-1):
        mini=i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini=j
        arr[i],arr[mini]=arr[mini],arr[i]
    return arr


arr=[7,23,8,2,90,45,0]
print(selectionSort(arr))

# bubblesort:
def bubbleSort(arr):
    n=len(arr)
    swapb=False
    for _ in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                swapb=True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if swapb==False:
            break
    return arr,swapb
arr=[7,23,8,2,90,45,0]
arr1=[1,2,3,4,5,6,7]
print(bubbleSort(arr))
print(bubbleSort(arr1))

# here variable is used in order for best case to get timecomplexity as O(n)


# insertion sort:
def insertionSort(arr):
    n=len(arr)
    for i in range(n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1
    return arr
arr=[7,23,8,2,90,45,0]
arr1=[14,9,15,12,6,8,13]
print(insertionSort(arr))
print(insertionSort(arr1))

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
