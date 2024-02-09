# when ever we have substring and a fixed window then we can use sliding window approach
# first we need to count frequency of s1 and store it in hash array 
# we can also maintain a varable totalchars i.e length of s1 string
# by maintaing window size we can use sliding window approach
# l1=len(s1) and l2=len(s2)
# Time complexity: O(l1+26l1(l2−l1))
# Space complexity: O(1).s1map and s2map of size 26 is used.

# https://leetcode.com/problems/permutation-in-string/description/
def matches(arr1,arr2):
    for i in range(26):
        if arr1[i] != arr2[i]:
            return False
    return True
def permutationinstr(s1,s2):
    # def permutationinstr(s1,s2):
    if len(s1)>len(s2):
        return False
    s1map=[0 for i in range(26)]
    for i in range(len(s1)):
        index=ord(s1[i])-ord('a')
        s1map[index]+=1
    window=len(s2)-len(s1)
    for i in range(window+1):
        s2map=[0 for _ in range(26)]
        for j in range(len(s1)):
            s2map[ord(s2[i+j])-ord('a')]+=1
        if self.matches(s1map,s2map):
            return True
    return False
s1="ab"
s2="eidbaooo"
print(permutationinstr(s1, s2))


# sliding window:
# here t.c=o(l1+26(l2-l1))
# S.C=O(1)+2*(26) which is constant
def matches(arr1,arr2):
    for i in range(26):
        if arr1[i] != arr2[i]:
            return False
    return True
def permutationinstr(s1,s2):
    # def permutationinstr(s1,s2):
    if len(s1)>len(s2):
        return False
    s1map=[0 for i in range(26)]
    s2map=[0 for _ in range(26)]
    for i in range(len(s1)):
        index=ord(s1[i])-ord('a')
        s1map[index]+=1
        s2map[ord(s2[i])-ord('a')]+=1
    window=len(s2)-len(s1)
    for i in range(window):
        if self.matches(s1map,s2map):
            return True
        s2map[ord(s2[i+len(s1)])-ord('a')]+=1
        s2map[ord(s2[i])-ord('a')]-=1
    return self.matches(s1map,s2map)
s1="ab"
s2="eidbaooo"
print(permutationinstr(s1, s2))