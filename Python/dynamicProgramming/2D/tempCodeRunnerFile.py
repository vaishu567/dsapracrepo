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