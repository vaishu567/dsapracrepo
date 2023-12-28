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
def subrec(arr,op,result):
    if len(arr)==0:
        result.append(list(op))
        # print(op)
        return result
    # not taking:
    op.append(arr[0])
    result=subrec(arr[1:],op,result)
    op.remove(arr[0])
    result=subrec(arr[1:],op,result)
    return result
arr=[1,2,1]
op=[]
result=[]
print(subrec(arr,op,result))




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