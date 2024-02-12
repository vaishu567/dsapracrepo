# if we observe we can solve this as  longest increasing subsequence:
# we need to write compare function:
def compare(s1,s2):
    # here s1 is longest str:
    if len(s1)!=len(s2)+1:
        return False
    i=0
    j=0
    while i<len(s1):
        if j<len(s2) and s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            i+=1
    if i==len(s1) and j==len(s2):
        return True
    return False
    
def tracebackliscode(arr,n):
    arr.sort(key=len)
    dp=[1 for i in range(n)]
    maxi=-1
    for ind in range(0,n):
        for prev in range(0,ind):
            if compare(arr[ind],arr[prev]) and 1+dp[prev]>dp[ind]:
                dp[ind]=1+dp[prev]
        maxi=max(maxi,dp[ind])
    return maxi
arr=["x","xx","y","xyx"]
n=len(arr)
print(tracebackliscode(arr,n))
        