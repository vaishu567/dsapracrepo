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

# nextpermutations:

def nextGreaterPermutation(a):
    # Write your code here.
    n=len(a)
    index=-1
    for i in range(n-2,-1,-1):
        if a[i]<a[i+1]:
            index=i
            break
    if index==-1:
        return rev(a,0,n-1)
    for i in range(n-1,index,-1):
        if a[i]>a[index]:
            a[i],a[index]=a[index],a[i]
            break
    a=rev(a,index+1,n-1)
    return a
def rev(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr


arr=[1, 6, 11, 16, 21, 31]
xor=0
for i in range(len(arr)):
    xor=xor^arr[i]
    print(xor)
print(xor)



arr=[1,3,4,6,8,7,5,2]
arr=[1,3,4,7,8,6,5,2]


def majorityElement(v):
    # Write your code here
    # bruteforce approach:
    # t.c=O(n^2)
    # n=len(v)
    # mal=[]
    # for i in range(n):
    #     curcount=1
    #     curel=v[i]
    #     if curel!=mal[-1] or len(mal)==0:
    #         for j in range(i+1,n):
    #             if v[j]==curel:
    #                 curcount+=1
    #         if curcount>(n//3):
    #             mal.append(curel)
    # return mal
    # better approach:
    # d={}
    # for i in range(n):
    #     if v[i] in d:
    #         d[v[i]]+=1
    #     else:
    #         d[v[i]]=1
    # for i,k in d.items():
    #     if k>(n//3):
    #         mal.append(i)
    # return mal
    pass
v=[1,1,1,2,2,2]
print(majorityElement(v))

print(3>(6//3))

# set doesn't take lists as values coz set takes unique values and if lists are taken as values they can be mutable but tupels are taken as values since tuples are immutable

# 13
# -18 -1 -44 -48 -9 -16 -36 -13 29 17 -12 9 -49 






