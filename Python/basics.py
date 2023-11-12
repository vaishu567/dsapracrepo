def reversed(n):
    temp=n
    rev=""
    while temp>0:
        rem=str(temp%10)
        rev+=rem
        temp=temp//10
    if rev==str(n):
        return True
    return False
print(reversed(12321))

# arrays:
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

# frequency of most frequent element:
# here the array should be sorted first and then using sliding window we calculate current sum of array
# and then simultaneously we check if the cursum + k == arr[end-1]*end-start
def maxFrequency(nums, k):
    i=0
    j=0
    res=1
    n=len(nums)
    nums=sorted(nums)
    curs=0
    while j<n:
        curs+=nums[j]
        j+=1
        if (curs+k<nums[j-1]*(j-i)):
            curs-=nums[i]
            i+=1
        res=max(res,j-i)
    return res
