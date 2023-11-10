def secondlargest(arr):
    n=len(arr)
    largest=arr[0]
    slargest=-1000000
    for i in range(1,n):
        if arr[i]>largest:
            slargest=largest
            largest=arr[i]
        elif arr[i]<largest:
            if arr[i]>slargest:
                slargest=arr[i]
    return largest,slargest
arr=[8,-9,0,5,45,34,23,-89]
arr1=[1,4,4,4,4,4,4,4,4,4,4,4,4]

print(secondlargest(arr1))