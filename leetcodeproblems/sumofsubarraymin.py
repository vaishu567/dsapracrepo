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
 
# recursive:
def subminssum(arr,index,op):
    if index==len(arr):
        if op:
            print(op)
            return min(op)
        else:
            return 0
    op.append(arr[index])
    sumpick=subminssum(arr,index+1,op)
    op.remove(arr[index])
    sumnot=subminssum(arr,index+1,op)
    return sumnot+sumpick


arr=[3,1,2,4]
# print(min(arr))
print(subminssum(arr,0,[]))
