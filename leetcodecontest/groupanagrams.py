# Time complexity:
# O(n∗k∗logk)O(n * k * log k)O(n∗k∗logk)
# (K is the length of the longest string)

# Space complexity:
# O(n∗k)O(n*k)O(n∗k)
# (K is the length of the longest string)

def groupAnagrams(strs):
    n=len(strs)
    d={}
    for i in range(n):
        s="".join(sorted(strs[i]))
        if s in d:
            d[s].append(strs[i])
        else:
            d[s]=[strs[i]]
    return d.values()