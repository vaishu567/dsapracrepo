def majorityElement(v):
    # Write your code here
    # bruteforce approach:
    n=len(v)
    mal=[]
    maxel=0
    for i in range(n):
        curcount=1
        maxi=-1000000
        curel=v[i]
        for j in range(i+1,n):
            if v[j]==curel:
                curcount+=1
        maxi=max(maxi,curcount)
        maxel=v[i]
        if maxi>(n//3):
            mal.append(maxel)

    return mal
v=[1,1,1,2,2,2]
print(majorityElement(v))