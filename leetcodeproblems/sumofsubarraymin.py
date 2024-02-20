# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

# Example 1:

# Input: arr = [3,1,2,4]
# Output: 17
# Explanation: 
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:

# Input: arr = [11,81,94,43,3]
# Output: 444
 
# bruteforce:
def subarraymin(arr):
    # op=[]
    sumi=0
    for i in range(len(arr)):
        sumi+=arr[i]
        for j in range(i+1,len(arr)):
            sumi+=min(arr[i:j+1])
    return sumi
arr=[3,1,2,4]
# print(min(arr))
print(subarraymin(arr))


# recursive:
# def subarraymin(arr,ind,prev,take,nottake):

# arr=[3,1,2,4]
# print(subarraymin(arr,0,-1,0,0))

