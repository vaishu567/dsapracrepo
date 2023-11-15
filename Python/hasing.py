# for any character:
def noofchars(s,t):
    d=[0 for i in range(256)]
    for i in s:
        d[ord(i)]+=1
    return d[ord(t)]
s="vaishnavi$%%$@%%$^"
t='%'
print(noofchars(s,t))

# for lower case characters:
def nofchars(s,t):
    d=[0 for i in range(26)]
    for i in s:
        d[ord(i)-ord('a')]+=1
    return d[ord(t)-ord('a')]
s="vaishnavi"
t='v'
print(nofchars(s,t))

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