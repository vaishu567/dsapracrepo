# recursion:

def mcm(arr,i,j,mini):
    if i==j:
        return 0
    for k in range(i,j):
        steps=arr[i-1]*arr[k]*arr[j]+(mcm(arr,i,k,mini)+mcm(arr,k+1,j,mini))
        mini=min(mini,steps)
    return mini
arr=[10,15,20,25]
n=len(arr)
print(mcm(arr,1,n-1,float('inf')))

