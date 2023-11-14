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
# movezeroesto end:
def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    j=0
    k=0
    for i in range(n):
        if a[i]==0:
            j=i
            k=j+1
            break
    while k<n and j<n:
        if a[k]!=0:
            a[k],a[j]=a[j],a[k]
            k+=1
            j+=1
        else:
            k+=1
    return a  

def findArrayIntersection(arr: list, n: int, brr: list, m: int):
    # Write your code here
    # Return a list containing all the common elements in arr and brr.
    i=0
    j=0
    new=[]
    while i<n and j<m:
        if arr[i]==brr[j]:
            new.append(arr[i])
            i+=1
            j+=1
        elif arr[i]<brr[j]:
            i+=1
        else:
            j+=1
    return new

# this missing letter can be done in 2 optimal approaches:
# XOR can be used when in array 0 is not included.
def missingNumber( nums):
    n=len(nums)
    # sumap=(n*(n+1))//2
    # sumi=sum(nums)
    # return sumap-sumi        
    xor1=0
    xor2=0
    for i in range(n):
        xor1=xor1^nums[i]
        xor2=xor2^(i+1)
    xor2=xor2^(n+1)
    return xor1^xor2
nums=[1,2,4,5]
print(missingNumber(nums))

print(1^2^4^5)
print(1^2^3^4^5)
print(1^2)


# find the single element optimal approach:
def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    n=len(arr)
    xor=0
    for i in range(n):
        xor=xor^arr[i]
    return xor
