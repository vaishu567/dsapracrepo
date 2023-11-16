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


def zeroMatrix(matrix, n, m):
    # Write your code here.

    # this is better solution:
    # row=[0 for i in range(n)]
    # col=[0 for i in range(m)]
    # for i in range(n):
    #     for j in range(m):
    #         if matrix[i][j]==0:
    #             row[i]=1
    #             col[j]=1
    # for i in range(n):
    #     for j in range(m):
    #         if row[i] or col[j]:
    #             matrix[i][j]=0
    # return matrix
    # optimal:
    col0=1
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                # mark i-th row
                matrix[i][0]=0
                # mark j-th col
                if j!=0:
                    matrix[0][j]=0
                else:
                    col0=0
    for i in range(1,n):
        for j in range(1,m):
            if matrix[i][j]!=0:
                # check for col and row
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(m):
            matrix[0][j]=0
    if col0==0:
        for i in range(n):
            matrix[i][0]=0
    return matrix