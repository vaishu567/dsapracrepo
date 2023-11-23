def ninjaGram(str):

    # Write your Code Here.
    # Return a boolean variable 'True' or 'False' denoting the answer
    d={i:0 for i in range(26)}
    str=str.lower()
    for i in str:
        x=ord(i)-ord('a')
        print(x)
        if x not in d:
            d[x]=1
        d[x]+=1
    
    for k,v in d.items():
        if v==0:
            return 'NO'
    return 'YES'
print(ninjaGram('TheQuickBrownFoxJumpsOverTheLazyDog'))