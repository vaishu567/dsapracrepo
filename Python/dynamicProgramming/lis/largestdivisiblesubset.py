def largestdivisiblest(arr,n,ind,prev):
    if ind==n:
        return 0
    nottake=0+largestdivisiblest(arr,n,ind+1,prev)
    take=0
    if prev==-1 or arr[ind]%arr[prev]==0:
        take=1+largestdivisiblest(arr,n,ind+1,ind)
    return max(take,nottake)
    
arr=[1,2,4,8]
arr.sort()
print(largestdivisiblest(arr,len(arr),0,-1))

# memoization:
def largestdivisiblest(arr,n,ind,prev,dp):
    if ind==n:
        return 0
    if  dp[ind][prev]!=-1:
        return dp[ind][prev]
    nottake=0+largestdivisiblest(arr,n,ind+1,prev,dp)
    take=0
    if prev==-1 or arr[ind]%arr[prev]==0:
        take=1+largestdivisiblest(arr,n,ind+1,ind,dp)
    dp[ind][prev]= max(take,nottake)
    return dp[ind][prev]

arr=[1,2,5]
arr.sort()
dp=[[-1 for i in range(len(arr))]for i in range(len(arr))]
print(largestdivisiblest(arr,len(arr),0,-1,dp))

# tabulation:
def largestdivisiblest(arr,n):
    dp=[[0 for i in range(n+1)]for i in range(n+1)]
    for ind in range(n-1,-1,-1):
        for prev in range(ind-1,-2,-1):
            nottake=0+dp[ind+1][prev+1]
            take=0
            if prev==-1 or arr[ind]%arr[prev]==0:
                take=1+dp[ind+1][ind+1]
            dp[ind][prev+1]= max(take,nottake)
    return dp[0][-1+1]

arr=[1,2,5]
arr.sort()
print(largestdivisiblest(arr,len(arr)))

# space optimization:
def largestdivisiblest(arr,n):
    next=[0 for i in range(n+1)]
    curr=[0 for i in range(n+1)]
    for ind in range(n-1,-1,-1):
        for prev in range(ind-1,-2,-1):
            nottake=0+next[prev+1]
            take=0
            if prev==-1 or arr[ind]%arr[prev]==0:
                take=1+next[ind+1]
            curr[prev+1]= max(take,nottake)
        next=curr
    return curr[-1+1]

arr=[1,2,5]
arr.sort()
print(largestdivisiblest(arr,len(arr)))

# how to prinnt  lis :
def largestdivisiblest(arr,n):
    dp=[1 for i in range(n)]
    for ind in range(0,n):
        for prev in range(0,ind):
            if arr[ind]%arr[prev]==0 and 1+dp[prev]>dp[ind]:
                dp[ind]=1+dp[prev]
    return max(dp)


arr=[1,2,5]
arr.sort()
print(largestdivisiblest(arr,len(arr)))





# using trace back:
def largestdivisiblest(arr,n):
    dp=[1 for i in range(n)]
    hasharr=[i for i in range(n)]
    maxi=-1
    lastind=-1
    for ind in range(0,n):
        for prev in range(0,ind):
            if arr[ind]%arr[prev]==0 and 1+dp[prev]>dp[ind]:
                dp[ind]=1+dp[prev]
                hasharr[ind]=prev
    
        if dp[ind]>maxi:
            maxi=dp[ind]
            lastind=ind
    final=[]
    final.append(arr[lastind])
    while lastind!=hasharr[lastind]:
        lastind=hasharr[lastind]
        final.append(arr[lastind])
    return final[::-1]


arr=[1,2,5]
arr.sort()
print(largestdivisiblest(arr,len(arr)))






# def modifiedMatrix(matrix):
#     m=len(matrix)
#     n=len(matrix[0])
#     maxcol=[max(matrix[i][j] for i in range(m)) for j in range(n)]
#     return maxcol
#     # for j in range(n):
#     #     maxi=float('-inf')
#     #     for i in range(m):
#     #         # print(i,j)
#     #         if matrix[i][j]>maxi:
#     #             maxi=matrix[i][j]
#     #         if matrix[i][j]==-1:
#     #             ind=i
#     #             ind2=j
#     #     print(maxi,ind,ind2)
#     #     new[ind][ind2]=maxi
#     # return new
# mat=[[1,2,-1],[4,-1,6],[7,8,9]]
# print(modifiedMatrix(mat))




# def distinctatevenforstr(s):
#     prev=-1
#     count=0
#     for i in range(len(s)):
#         if i%2==0:
#             if s[i]!=prev:
#                 count+=1
#                 prev=s[i]
#     return count
# def isprime(n):
#     if n==2:
#         return 1
#     if n==1:
#         return 0
#     for i in range(2,n//2+1):
#         if n%i==0:
#             return 0
#     return 1
        
            
# def findBots(usernames,n ):
#     # code here
#     final=[]
#     for i in range(n):
#         distinct=distinctatevenforstr(usernames[i])
#         print(distinct)
#         final.append(isprime(distinct))
#     return final
# usernames=["abcdef","pqrs","xyzuvabb","aaaaa"]
# print(findBots(usernames,len(usernames)))


# # def recursive(N,S,ind,op):
# #     if ind==N:
# #         count=0
# #         print(op)
# #         for i in op:
# #             if i=="1":
# #                 count+=1
# #         if count>(len(op)//2):
# #             return 1
# #         else:
# #             return 0
# #     # nottake:
# #     nottake=recursive(N,S,ind+1,op)
# #     op+=S[ind]
# #     take=recursive(N,S,ind+1,op)
# #     return take+nottake
    
    
    
# # def greatCount( N , S ):
# #     # code here
# #     return recursive(N,S,0,"")

# # S="010"
# # N=len(S)
# # print(greatCount(N,S))