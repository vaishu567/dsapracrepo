# longest common prefix:
def commonPrefix(arr: List[str], n: int) -> str:
    # Write your code here
    # bruteforce:
    pre=-1
    for i in range(len(arr[0])):
        prefix=arr[0][0:i+1]
        for j in range(1,n):
            if arr[j][0:i+1]!=prefix:
                return pre   
        pre=prefix
    return pre
# cyclical rotated string same or not:
# use new string which is concatenation of 1st string 2times:
# and check if second string is substring of new string or not:
def isCyclicRotation(p: str, q: str) -> int:
    # Write your code here.
    news=p+p
    n=len(q)
    k=len(news)
    for i in range(n):
        if news[i:i+n]==q:
            return 1
    return 0

# find if strings or anagram or not:
def isAnagram(str1, str2) :
	# write your code here.
	# d={}
	# p={}
	n=len(str1)
	m=len(str2)
	if n!=m:
		return False
	# for i in range(n):
	# 	if str1[i] not in d:
	# 		d[str1[i]]=1
	# 	else:
	# 		d[str1[i]]+=1
	# 	if str2[i] not in p:
	# 		p[str2[i]]=1
	# 	else:
	# 		p[str2[i]]+=1
	# if p==d:
	# 	return True
	# return False
	xor=0
	for i in range(n):
		xor=xor^ord(str1[i])^ord(str2[i])
	if xor==0:
		return True
	return False