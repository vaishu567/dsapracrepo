# finding all subsequences of a string:
# a subsequence is a part of string that need not be continuous
# subsequence!=substring
# we are supposed to make an array of strings and add all the subsequences in array and return 
def subsequence(s):
    if len(s) == 0:
        output=[]
        output.append(" ")
        return output
    # l.append(s[i])
    smalls=s[1:]
    smallo=subsequence(smalls)
    l=[]
    for j in range(len(smallo)):
        l.append(smallo[j])
        l.append(s[0]+smallo[j])
    return l
print(subsequence("abc"))




# instead of returning the list we need to print them:
# print all subsequences of string:
def printsubseq(s,o):
    if len(s) == 0:
        print(o)
        return 
    # don't include 0th char
    printsubseq(s[1:],o)
    # include 0th character
    newo=o+s[0]
    printsubseq(s[1:],newo)
printsubseq("abc","")



# print all subsequences of array using recursion:
def subrec(arr,op):
    if len(arr)==0:
        # result.append(list(op))
        print(op)
        return
        # return result
    # not taking:
    op.append(arr[0])
    subrec(arr[1:],op)
    op.remove(arr[0])
    subrec(arr[1:],op)
arr=[1,1,2]
op=[]
# result=[]
print(subrec(arr,op))








# print all subsequences of array whose sum is k using recursion:
def subseqk(arr,op,k):
    if len(arr)==0:
        if sum(op)==k:
            print(op)
        return 
    # taking s[0]
    op.append(arr[0])
    subseqk(arr[1:],op,k)
    # not taking s[0]:
    op.remove(arr[0])
    subseqk(arr[1:],op,k)
arr=[1,2,1,3,4]
op=[]
k=5
subseqk(arr,op,k)



# /////subsequence or subset modification return boolean:

def subseqk(a,op,k,flag):
    if len(a)==0:
        if sum(op)==k and flag==False:
            flag=True
        return flag
        
    # taking s[0]:
    op.append(a[0])
    flag=subseqk(a[1:],op,k,flag)
    # not taking s[0]
    op.remove(a[0])
    flag=subseqk(a[1:],op,k,flag)
    return flag



def isSubsetPresent(n, k, a):
    # Write your code here.
    flag=False
    flag=subseqk(a,[],k,flag)
    return flag
a=[4,2,5,6,7]
print(isSubsetPresent(len(a),14,a))
    
    
        
# Technique to print one answer:
def subseqk(a,op,k):
    if len(a)==0:
        if sum(op)==k:
            return True
        else:
            return False   
    # taking s[0]:
    op.append(a[0])
    if subseqk(a[1:],op,k)==True:
        return True
    # not taking s[0]
    op.remove(a[0])
    if subseqk(a[1:],op,k)==True:
        return True
    return False

def isSubsetPresent(n, k, a):
    # Write your code here.
    flag=subseqk(a,[],k)
    return flag
a=[1,2,1]
print(isSubsetPresent(len(a),2,a))

# we don't want to print we want to count:
def subseqkcount(a,op,k):
    if sum(op)>k:
        return 0
    if len(a)==0:
        if sum(op)==k:
            return 1
        else:
            return 0  
    # taking s[0]:
    op.append(a[0])
    l=subseqkcount(a[1:],op,k)
    # not taking s[0]
    op.remove(a[0])
    r=subseqkcount(a[1:],op,k)
    return l+r
a=[4,2,5,6,7]
k=14
print(subseqkcount(a,[],k))




def subseqofs(s,opl,o):
    if len(s)==0:
        opl.append(o)
        return opl
    # not taking s[0]
    opl=subseqofs(s[1:],opl,o)
    # taking s[0]
    newo=o+s[0]
    opl=subseqofs(s[1:],opl,newo)
    return opl
s="abc"
opl=[]
o=" "
print(subseqofs(s,opl,o))



# all subsequences using powerset:
def subsets(nums):
    n=len(nums)
    final=[]
    for num in range(0,2**n):
        op=[]
        for i in range(0,n):
            if num&(1<<i)!=0:
                op.append(nums[i])
        final.append(list(op))
    return final

# combinationsum-I:
def recurscomb(indx,ARR,target,final,new):
	if indx==len(ARR):
		if target==0:
			final.append(list(new))
		return final
	if ARR[indx]<=target:
		new.append(ARR[indx])
		final=recurscomb(indx,ARR,target-ARR[indx],final,new)
		new.remove(ARR[indx])
	final=recurscomb(indx+1,ARR,target,final,new)
	return final

def combSum(ARR, B):
	# Write your code here
	final=[]
	new=[]
	fin=recurscomb(0,ARR,B,final,new)
	return fin
ARR=[1,2,3]
B=5
print(combSum(ARR, B))


# combinationsum-I modification:
def recurs(indx,arr,final,t,op):
    if indx==len(arr):
        if t==0 :
            # if len(final)==0 or op not in final:
            final.append(list(op))
        return final
    if arr[indx]<=t:
        op.append(arr[indx])
        final=recurs(indx,arr,final,t-arr[indx],op)
        op.remove(arr[indx])
    final=recurs(indx+1,arr,final,t,op)
    return final
def combinationalSum(A, B):
    A=sorted(list(set(A)))
    final=set()
    op=[]
    fin=recurs(0,A,final,B,op)
    fin=list(fin)
    return fin
A=[1,2,3]
B=5
print(combinationalSum(A, B))

# combination Sum-II:
# def helper(indx,arr,t,final,op):
#     # if indx==len(arr):
#     #     if t==0:
#     #         if len(final)==0 or op not in final:
#     #             final.append(list(op))
#     #     return final
#     # if arr[indx]<=t:
#     #     op.append(arr[indx])
#     #     final=helper(indx+1,arr,t-arr[indx],final,op)
#     #     op.remove(arr[indx])
#     # final=helper(indx+1,arr,t,final,op)
#     # return final
def helper(indx,arr,t,final,op):
    if t==0:
        final.append(list(op))
        return final
    for i in range(indx,len(arr)):
        if i>indx and arr[i]==arr[i-1]:
            continue
        if arr[i]>t:
            break
        op.append(arr[i])
        final=helper(i+1,arr,t-arr[i],final,op)
        op.remove(arr[i])
    return final

def combinationSum2(arr: List[int], n: int, target: int) -> List[List[int]]:
    # Write your code here.
    arr=sorted(arr)
    final=[]
    op=[]
    fin=helper(0,arr,target,final,op)
    return fin


# subset sum-I:
# T.C=O(2^n + 2^n(log2^n)) => 2^n for generating combinations i.e p/n and 2^nlog2^n is for final sort
def recursub(arr,final,sumi):
    if len(arr)==0:
        final.append(sumi)
        return final
    # adding s[0] into sum:
    sumi+=arr[0]
    final=recursub(arr[1:],final,sumi)
    # removing s[0] from sum:
    sumi-=arr[0]
    final=recursub(arr[1:],final,sumi)
    return final


def subsetSum(num: List[int]) -> List[int]:
    # Write your code here.
    final=[]
    sumi=0
    fin=recursub(num,final,sumi)
    fin=sorted(fin)
    return fin

# get all unique subsets:
# bruteforce:
def subsetsWithDup(nums):
    ans = []
    res = set()
    def fun(index, ds):
        if index == len(nums):
            ds.sort()
            res.add(tuple(ds))
            return
        ds.append(nums[index])
        fun(index + 1, ds)
        ds.pop()
        fun(index + 1, ds)
    fun(0, [])
    for it in res:
        ans.append(list(it))
    return ans

# optimal:
def recursi(indx,arr,final,op):
    final.append(list(op))
    for i in range(indx,len(arr)):
        if i>indx and arr[i]==arr[i-1]:
            continue
        op.append(arr[i])
        final=recursi(i+1,arr,final,op)
        op.remove(arr[i])
    return final

def subsetsWithDup(nums):
    # write the code  logic here !!! 
    final=[]
    op=[]
    fin=recursi(0,nums,final,op)
    return fin
nums=[12,15,20]
print(subsetsWithDup(nums))


# combinationsum-III:
def recursive(arr,final,n,op,k):
    if len(arr)==0:
        if sum(op)==n and len(op)==k:
            final.append(list(op))
        return final
    # taking:
    op.append(arr[0])
    final=recursive(arr[1:],final,n,op,k)
    op.remove(arr[0])
    final=recursive(arr[1:],final,n,op,k)
    return final
arr=[1,2,3,4,5,6,7,8,9]
n=5
k=2
final=[]
op=[]
print(recursive(arr,final,n,op,k))



# def binary(n,s):
#     if n == 0:
#         return s
#     rem=n%2
#     s.append(rem)
#     n=n//2
#     s=binary(n,s)
#     return s
# n=4
# s=[]
# print(binary(n,s))

# permutations:
# approach-1
def helper(self,arr,final,freq,op):
    if len(op)==len(arr):
        final.append(list(op))
        return final
    for i in range(0,len(arr)):
        if freq[i]==False:
            freq[i]=True
            op.append(arr[i])
            final=self.helper(arr,final,freq,op)
            op.remove(arr[i])
            freq[i]=False
    return final

def permute(self, nums: List[int]) -> List[List[int]]:
    freq=[False for i in range(len(nums))]
    final=[]
    op=[]
    fin=self.helper(nums,final,freq,op)
    return fin
# approach-2:
def swapf(i,j,arr):
    arr[i],arr[j] = arr[j],arr[i]
    return arr
def permutations(index,nums,final,op):
    if index==len(nums):
        op=nums
        final.append(list(op))
        return final
    for i in range(index,len(nums)):
        nums=swapf(i,index,nums)
        final=permutations(index+1,nums,final,op)
        nums=swapf(i,index,nums)
    return final
final=[]
op=[]
nums=[1,2,3]
print(permutations(0,nums,final,op))

    
# partition palindrome:
def ispalindrome(self,s,i,j):
    while i<j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    return True
        
def partitionhelper(self,s,index,final,op):
    if index==len(s):
        final.append(list(op))
        return final
    for i in range(index,len(s)):
        if self.ispalindrome(s,index,i):
            op.append(s[index:i+1])
            final=self.partitionhelper(s,i+1,final,op)
            op.pop()
    return final
def partition(self, s):
    final=[]
    op=[]
    fin=self.partitionhelper(s,0,final,op)
    return fin

