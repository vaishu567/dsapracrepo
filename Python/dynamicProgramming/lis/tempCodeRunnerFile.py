

def distinctatevenforstr(s):
    prev=-1
    count=0
    for i in range(len(s)):
        if i%2==0:
            if s[i]!=prev:
                count+=1
                prev=s[i]
    return count
def isprime(n):
    if n==2:
        return 1
    if n==1:
        return 0
    for i in range(2,n//2):
        if n%i==0:
            return 0
    return 1
        
            
def findBots(usernames,n ):
    # code here
    final=[]
    for i in range(n):
        distinct=distinctatevenforstr(usernames[i])
        final.append(isprime(distinct))
    return final
usernames=["abcdef","pqrs","xyzuvabb","aaaaa"]