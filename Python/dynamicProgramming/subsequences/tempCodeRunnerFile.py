arr=[3,9,7,3]
k=sum(arr)
dp=[[False for i in range(k+1)] for j in range(len(arr))]
print(dp)