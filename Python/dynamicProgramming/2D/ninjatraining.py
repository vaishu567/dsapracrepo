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
arr=[[10,50,1],[9,100,7]]
day=len(arr)-1
last=len(arr[0])
dp=[[-1 for i in range(last+1)]]*(day+1)
# print(dp)
print(memoization(arr,day,last,dp))

