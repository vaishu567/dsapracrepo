# maximum points ninja can earn:
def recursive(arr,day,last):
    if day==0:
        maxi=0
        for i in range(0,3):
            if i!=last:
                maxi=max(maxi,arr[0][i])
        return maxi
    maxi=0
    for i in range(0,3):
        if i!=last:
            points=arr[day][i]+recursive(arr,day-1,i)
            maxi=max(maxi,points)
    return maxi
arr=[[10,50,1],[9,100,7]]
day=len(arr)-1
last=len(arr[0])
print(recursive(arr,day,last))


# we use 2d array for memoization also:
def memoization(arr,day,last,dp):
    if day==0:
        maxi=0
        for i in range(0,3):
            if i!=last:
                maxi=max(maxi,arr[0][i])
        return maxi
    if dp[day][last]!=-1:
        return dp[day][last]
    maxi=0
    for i in range(0,3):
        if i!=last:
            points=arr[day][i]+memoization(arr,day-1,i,dp)
            maxi=max(maxi,points)
    dp[day][last]=maxi
    return dp[day][last]
arr=[[1,2,5], [3 ,1 ,1] ,[3,3,3] ]
day=len(arr)-1
last=len(arr[0])
dp = [[-1 for _ in range(last + 1)] for _ in range(n)] 
# print(dp)
print(memoization(arr,day,last,dp))

# dp:
# since memoization is done top-down 
# tabulaton should be done bottom down:

def tabulation(arr,day,dp):
    dp[0][0]=max(arr[0][1],arr[0][2])
    dp[0][1]=max(arr[0][2],arr[0][0])
    dp[0][2]=max(arr[0][0],arr[0][1])
    dp[0][3]=max(arr[0][0],arr[0][1],arr[0][2])
    for day in range(1,len(arr)):
        for last in range(4):
            dp[day][last]=0
            for i in range(3):
                if i!=last:
                    points=arr[day][i]+dp[day-1][i]
                    dp[day][last]=max(dp[day][last],points)
    return dp[len(arr)-1][3]         
arr=[[1,2,5], [3 ,1 ,1] ,[3,3,3]]
day=len(arr)-1
n=len(arr)
dp = [[0 for _ in range(4)] for _ in range(n)] 
print(tabulation(arr,day,dp))



# space optimization:
# T.C=O(N*4*3)
# S.c=O(4)
def space(arr):
    prev=[0 for i in range(4)]
    prev[0]=max(arr[0][1],arr[0][2])
    prev[1]=max(arr[0][2],arr[0][0])
    prev[2]=max(arr[0][0],arr[0][1])
    prev[3]=max(arr[0][0],arr[0][1],arr[0][2])
    for day in range(1,len(arr)):
        temp=[0 for i in range(4)]
        for last in range(4):
            # creating temp array for changing prev array
            temp[last]=0
            for i in range(3):
                if i!=last:
                    points=arr[day][i]+prev[i]
                    temp[last]=max(temp[last],points)
        prev=temp
    return prev[3]  

arr=[[1,2,5], [3 ,1 ,1] ,[3,3,3]]
print(space(arr))