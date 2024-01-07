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
def getSingleElement(arr ):
    # Write your code here.
    n=len(arr)
    xor=0
    for i in range(n):
        xor=xor^arr[i]
    return xor

def longestSubarrayWithSumK(arr, k):
    # Write your code here
    sum=0
    n=len(arr)
    i=0
    maxi=0
    for j in range(n):
        sum+=arr[j]
        if sum>k:
            sum-=arr[i]
            i+=1
        if sum==k:
            maxi=max(maxi,(j-i+1))      
    return maxi
arr=[38289 ,33170 ,1859 ,23863, 45658, 24408, 38353 ,21761, 46411, 41237 ,46956, 33613, 49349, 26026, 11031, 19190 ,45358 ,32843, 7054, 14184, 46050, 19610 ,12625 ,14179 ,4066 ,6866, 9996, 34864, 26222, 1262 ,27512 ,40674 ,9793, 14583 ,34325, 23768, 40373, 10787, 23397, 2298, 42342 ,26340, 19552, 1612 ,7014, 44006, 18885 ,14427 ,3821, 41595, 40575 ,26085, 34594, 49448, 41457, 37147, 15003, 18172 ,6585 ,29405 ,11315, 29488 ,26525, 40889 ,27485, 31122, 29281, 8787, 3008 ,41470, 34402, 9184, 25736]
k=526314
print(longestSubarrayWithSumK(arr,k))


def getLongestSubarray(nums, k):
    # Write your code here
    sum=0
    maxi=0
    n=len(nums)
    i=0
    for j in range(n):
        sum+=nums[j]
        if k>0:
            while sum>k and i<n and nums[i]!=0:

                sum-=nums[i]
                i+=1
            if sum==k:
                maxi=max(maxi,j-i+1)
        else:
            if sum==k:
                maxi=max(maxi,j-i+1)

    return maxi
k= -2
nums=[-10, 8 ,2, -2]
print(getLongestSubarray(nums,k))

# subarray with sum=k containing 0,-ve's and +ve's:
def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    n = len(nums) # size of the array.

    preSumMap = {}
    Sum = 0
    maxLen = 0
    for i in range(n):
        # calculate the prefix sum till index i:
        Sum += nums[i]

        # if the sum = k, update the maxLen:
        if Sum == k:
            maxLen = max(maxLen, i + 1)

        # calculate the sum of remaining part i.e. x-k:
        rem = Sum - k

        # Calculate the length and update maxLen:
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        # Finally, update the map checking the conditions:
        if Sum not in preSumMap:
            preSumMap[Sum] = i

    return int(maxLen)

