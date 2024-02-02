
def purple(s: str) -> bool:
    # Write your code here.
    n=len(s)
    countB=0
    countR=0
    i=0
    j=0
    while i<n and j<n:
        if s[j]=="R":
            countR+=1
            print(countB,countR)

        elif s[j]=="B":
            countB+=1
            print(countB,countR)

        if countR==countB:
            print(countB,countR)
            return True
        elif countB>countR or countR>countB and countR>0 and countB>0:
            if s[i]=="B":
                countB-=1
            else:
                countR-=1
            i+=1
        j+=1
    return False

s="BRRBBB"
print(purple(s))