# to solve this problem first we need to find the longest common subsecquesnce from both a abd b and then subtract it from the sum of their lengths:
def shortestSupersequence(s1,s2):
    n=len(s1)
    m=len(s2)
    k=n+m
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for j in range(m+1):
        dp[0][j]=0
    for i1 in range(1,n+1):
        for i2 in range(1,m+1):               
            if s1[i1-1]==s2[i2-1]:
                dp[i1][i2]= 1+dp[i1-1][i2-1]
            else:
                dp[i1][i2]= 0+max(dp[i1-1][i2],dp[i1][i2-1])
    return k-dp[n][m]
s1="brute"
s2="groot"
print(shortestSupersequence(s1,s2))



# to print the shortest common supersequence:
def shortestSupersequence(s1,s2):
    n=len(s1)
    m=len(s2)
    k=n+m
    dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=0
    for j in range(m+1):
        dp[0][j]=0
    for i1 in range(1,n+1):
        for i2 in range(1,m+1):               
            if s1[i1-1]==s2[i2-1]:
                dp[i1][i2]= 1+dp[i1-1][i2-1]
            else:
                dp[i1][i2]= 0+max(dp[i1-1][i2],dp[i1][i2-1])
    # return k-dp[n][m]
    i=n
    j=m
    s=""
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            s+=s1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            s+=s1[i-1]
            i-=1
        else:
            s+=s2[j-1]
            j-=1
    while i>0:
        s+=s1[i-1]
        i-=1
    while j>0:
        s+=s2[j-1]
        j-=1
    return s[::-1]
s1="dingdingdingding"
s2="ing"
print(shortestSupersequence(s1,s2))


# another problem
# def purple(s: str) -> bool:
#     # Write your code here.
#     n=len(s)
#     countB=0
#     countR=0
#     i=0
#     j=0
#     while i<n and j<n:
#         if s[j]=="R":
#             countR+=1
#             print(countB,countR)

#         elif s[j]=="B":
#             countB+=1
#             print(countB,countR)

#         if countR==countB:
#             print(countB,countR)
#             return True
#         elif countB>countR or countR>countB and countR>0 and countB>0:
#             if s[i]=="B":
#                 countB-=1
#             else:
#                 countR-=1
#             i+=1
#         j+=1
#     return False

# s="BRRBBB"
# print(purple(s))