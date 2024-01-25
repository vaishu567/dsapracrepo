# You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

# Return the maximum possible length of s.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# def recursive(arr,index,maxi,op):
#     if index==len(arr):
#         print(op)
#         maxi=max(maxi,len(op))
#         return maxi
#     op.append(arr[index])
#     maxi=recursive(arr,index+1,maxi,op)
#     op.remove(arr[index])
#     maxi=recursive(arr,index+1,maxi,op)
#     return maxi
# arr=["un","iq","ue"]
# index=0
# maxi=float("-inf")
# op=[]
# print(recursive(arr,index,maxi,op))


# print(ord(' ')-ord('a'))

def havedup(s1,s2):
    d1={}
    d2={}
    for i in s1:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
    for i in s2:
        if i not in d2:
            d2[i]=1
        else:
            d2[i]+=1
    for i in d2:
        if i in d1:
            return True
        if d2[i]>1:
            return True
    return False

# print(havedup("","un"))

def recursive(arr,ind,temp,n):
    if ind==n:
        print(temp)
        return len(temp)
    include=float('-inf')
    if havedup(temp,arr[ind]):
        exclude=recursive(arr,ind+1,temp,n)
    else:
        exclude=recursive(arr,ind+1,temp,n)
        include=recursive(arr,ind+1,temp+arr[ind],n)
    return max(include,exclude)


arr = ["un","iq","ue"]
print(recursive(arr,0,"",len(arr)))


