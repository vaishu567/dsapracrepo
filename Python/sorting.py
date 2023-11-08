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