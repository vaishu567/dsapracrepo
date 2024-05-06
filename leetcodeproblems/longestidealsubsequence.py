# in this approach it is taking tle:
# recursion:
def reculongestsubideal(ind,s,k,n,last):
    if ind==n:
        return 0
    # take:
    take=0
    if last==-1 or abs(ord(s[ind])-ord(s[last]))<=k:
        take=1+reculongestsubideal(ind+1,s,k,n,ind)
    # not-take:
    nottake=0+reculongestsubideal(ind+1,s,k,n,last)
    return max(take,nottake)

def main(s,k):
    ind=0
    n=len(s)
    return reculongestsubideal(ind,s,k,n,-1)
print(main("jxhwaysa",14))

# dp (memoization):
def reculongestsubideal(ind,last, s, k, n,dp):
    if ind == n:
        return 0
    # take:
    if dp[ind][last]!=-1:
        return dp[ind][last]
    take = 0
    if last == -1 or abs(ord(s[ind])-ord(s[last])) <= k:
        take = 1+reculongestsubideal(ind+1,ind,s, k, n,dp)
    # not-take:
    nottake = 0+reculongestsubideal(ind+1,last, s, k, n,dp)
    dp[ind][last]= max(take, nottake)
    return dp[ind][last]


def main(s, k):
    ind = 0
    n = len(s)
    dp=[[-1 for _ in range(n+1)] for _ in range(n+1)]
    reculongestsubideal(ind,-1, s, k, n,dp)
    return dp[0][n]


print(main("jxhwaysa", 14))

# dp(tabulation):
# this approach is giving tle:
def reculongestsubideal(s,k):
    n=len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[n][i]=0
    for ind in range(n-1,-1,-1):
        for last in range(n-1,-1,-1):
            nottake = 0+dp[ind+1][last]
            take = 0
            if last == -1 or abs(ord(s[ind])-ord(s[last])) <= k:
                take = 1+dp[ind+1][ind]
            dp[ind][last] = max(take, nottake)
    return max(dp[0])
print(reculongestsubideal("pvjcci", 4))


def sumOfBeauty(s):
    # Write your code here.
    def freq(k):
        d={}
        for i in range(len(k)):
            if k[i] not in d:
                d[k[i]] =1
            else:
                d[k[i]]+=1
        maxi=max(d.values())
        mini=min(d.values())
        return maxi-mini
    count=0
    n=len(s)
    d=set()
    for i in range(n):
        for j in range(i+1,n):
            if s[i:j+1] not in d:
                d.add(s[i:j+1])
    for i in d:
        count+=freq(i)
    return count
print(sumOfBeauty("hello"))



