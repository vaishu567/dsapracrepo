# given an array of both +ve and -ve numbers we need to find the continuous subarray of min 1 element which has max sum and return its sum:
def kadanesalgo(arr):
    n=len(arr)
    sumi=0
    i=0
    maxi=float('-inf')
    while i<n:
        # if sumi<0:
        #     sumi=0
        # sumi+=arr[i]
        # if we write like this if the last element is negative we won't be able to check hence we need to fist add the value and then check for condition:
        sumi+=arr[i]
        if sumi<0:
            sumi=0
        maxi=max(maxi,sumi)
        i+=1
    return maxi
# arr=[2,4,-5,8,9,-3,-8,0,4]
arr=[2,4,-5,8,9,-18]
# arr=[9]
print(kadanesalgo(arr))
# here the subarray with max sum is [2,4,-5,8,9]
# one approach is to generate all sub-arrays using loops which will give n^3 time complexity
# we will use 2 pointers since we have terms continuous 

