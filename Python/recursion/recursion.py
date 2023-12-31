
# basic recursion function using base condition:
def countrec(count):
    if count==5:
        return 
    else:
        print(count)
        count+=1
        return countrec(count)
print(countrec(0))

# print names n times:
# def name(n):
#     while n>0:
#         print("vaishnavi")
#         return name(n-1)
#     return 
# print(name(5))

def name(n):
    if n==0:
        return
    print("vaishnavi")
    return name(n-1)
print(name(5))

# here we are calling n functions hence T.C=O(n)
# and S.C in recursion we assume stack space, here in stack every function call is waiting in stack space hence space complexity is O(n)
    
def onetoN(count,n):
    if count>n:
        return 
    print(count, end=" ")
    count+=1
    return onetoN(count,n)
onetoN(1,5)

# backtracking:
def onetoNBacktracking(count,n):
    if count==0:
        return
    onetoNBacktracking(count-1,n)
    print(count, end=" ")
onetoNBacktracking(5,5)

# /////////////////


def Ntoone(n):
    if n==0:
        return
    print(n, end=" ")
    return Ntoone(n-1)
Ntoone(5)

# backtracking:
def Ntooneback(i,n):
    if i>n:
        return
    Ntooneback(i+1,n)
    print(i, end=" ")
Ntooneback(1,5)

# /////////////////////////


# sum of first n numbers:

# parameterised:
def sumN(i,sum):
    if i<1:
        print(sum)
        return 
    sumN(i-1,sum+i)
sumN(3,0)

# functional:
def sumNf(n):
    if n==0:
        return 0
    return n+sumNf(n-1)
print(sumNf(3))


# factorial:
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(4))


# reverse:
def rev(arr,i,j):
    if i>=j:
        return arr
    arr[i],arr[j] = arr[j],arr[i]
    return rev(arr,i+1,j-1)
arr=[2,3,6,8,4]
n=len(arr)
print(rev(arr,0,n-1))

# check if string is palindrome:
def palindrome(s,i,j):
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    return palindrome(s,i+1,j-1)
s="madam"
n=len(s)
print(palindrome(s,0,n-1))

# fibonacci:
def fibonacci(n):
    if n==0 or n==1:
        return n
    last=fibonacci(n-1)
    seclast= fibonacci(n-2)
    
    return last+seclast
print(fibonacci(4))


# def has():
#     a=[0 for i in range(10000000)]
#     return a
# print(has())

# print(ord('b')-ord('a'))


# power of x:
def powern(x,n):
    if n==1:
        return x
    power=x*(powern(x,n-1))
    return power
print(powern(3,3))


# check if list is sorted or not:
def checklist(arr,n):
    if n==0:
        return True
    if arr[n]>=arr[n-1]:
        return checklist(arr,n-1)
    else:
        return False
    
arr=[1,2,3,4,5,10,7,8,9]
n=len(arr)-1
print(checklist(arr,n))

# sum of array using recursion:
def sumarray(arr,sum,n):
    if n==0:
        return arr[0]
    sum+=sumarray(arr,sum,n-1)
    sum+=arr[n]
    return sum
arr=[7,4,9,11,-3]
n=len(arr)-1
print(sumarray(arr,0,n))


# check if number is present in array:
def checknumber(arr,target,n):
    if n<0:
        return -1
    if arr[n]==target:
        return n
    return checknumber(arr,target,n-1)
arr=[2,8,-5,7,-9]
n=len(arr)-1
target=7
print(checknumber(arr,target,n-1))


# first occurance of number in array:
def firstocc(arr,x,n,i):
    if i==n:
        return -1
    if arr[i]==x:
        return i
    return firstocc(arr,x,n,i+1)
arr=[1,2,3,4,3,3,4,4,8]
n=len(arr)
x=8
print(firstocc(arr,x,n,0))

# sorted array:
# [1,2,3,3,3,4,4,4,5,6]
def firstoccarr(arr,x,s,e):
    if s>e:
        return s
    mid=(s+e)//2
    if arr[mid]>=x:
        e=mid-1
        return firstoccarr(arr,x,s,e)
    else:
        s=mid+1
        return firstoccarr(arr,x,s,e)
arr=[1,2,3,3,3,4,4,4,5,6]
x=4
s=0
e=len(arr)-1
print(firstoccarr(arr,x,s,e))


# recursion on strings:
def replaceab(s,n,i,sam):
    if i==n:
        return sam
    if s[i]=='p' and s[i+1]=="i":
        sam+='b'
        i+=1
        # continue
        # pass
    else:
        sam+=s[i]
    sam=replaceab(s,n,i+1,sam)
    return sam
s="pipipppippipicipcusa"
n=len(s)
sam=""
print(replaceab(s,n,0,sam))


# replace pi:
def replacepi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p' and s[1]=='i':
        smalloutput=replacepi(s[2:])
        return '3.14'+smalloutput
    else:
        smalloutput=replacepi(s[1:])
        return s[0]+smalloutput
s="ipipple"
print(replacepi(s))
    
    
# geometric sum:
# 1+ 1/2 + 1/4 + .....+ 1/(2^k)
def geometric(k,sum):
    if k==0:
        return 1
    sum+=geometric(k-1,sum)
    sum+=1/(2**k)
    return sum
print(geometric(4,0))

# check palindrome:
def palindromeS(s,i,j):
    if i>j:
        return True
    if s[i]==s[j]:
        return palindromeS(s,i+1,j-1)
    return False
s="racecar"
s1="ninja"
n=len(s1)
print(palindromeS(s1,0,n-1))

# sumofdigits:
def sumofdigits(num,sum):
    if num==0:
        return 0
    n=num%10
    num=num//10
    sum+=sumofdigits(num,sum) 
    sum+=n
    return sum
print(sumofdigits(9,0))


# multiplication recursion:
def multiplication(m,n,sum):
    if n==0:
        return sum
    sum+=multiplication(m,n-1,sum)
    sum+=m
    return sum
print(multiplication(3,5,0))




# tower of hanoi:
def tower_hanoi(n,a,b,c):
    if n==1:
        print("move first disk from",a,"to",c)
        return 
    tower_hanoi(n-1,a,c,b)
    print("move ",n,"th disk from",a,"to",c)
    tower_hanoi(n-1,b,a,c)
print(tower_hanoi(3,"s","h","d"))


# staircase:
def staircase(n):
    if n==0:
        return 1
    elif n<0:
        return 0
    x=staircase(n-1)
    y=staircase(n-2)
    z=staircase(n-3)
    return x+y+z
print(staircase(4))

# print keypad combinations:
# let us assume that 1,0 are not there in our combinations
def getString(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
def keyC(num):
    if num == 0:
        output=[]
        output.append(" ")
        return output
    
    smallnum=num//10
    rem=num%10
    smallop=keyC(smallnum)
    stringford=getString(rem)
    op=[]
    # j=len(stringford)-1
    for i in smallop:
        for j in stringford:
            op.append(i+j)
    return op
o=keyC(237)
print(len(o),o)

# PRINTING output instead of returning:
def fact(n):
    if n==0:
        return 1
    smallop=fact(n-1)
    op=n*(smallop)
    print(op)
    return op
# here we are printing while we are returning
# but that's not what we want so:

def factr(n):
    if n==0:
        return 1
    op=n*factr(n-1)
    return op
# the above fun will return 
# now then main function will print
def factp(k):
    op=factr(k)
    print(op)
factp(3)

# but the idea is the actual recurrsive function to do printing
def factorialPrint(n,ans):
    if n==0:
        print(ans)
        return 
    ans=ans*n
    factorialPrint(n-1,ans)
factorialPrint(5,1)
# print min in array:
# instead of returning print min:
def minarr(arr,mini):
    if len(arr)==0:
        print(mini)
        return 
    mini=min(arr[0],mini)
    minarr(arr[1:],mini)
arr=[2,3,-4,5,6,7,8,9,10]
mini=float('inf')
minarr(arr,mini)



def getString(d):
    if d==2:
        return "abc"
    if d==3:
        return "def"
    if d==4:
        return "ghi"
    if d==5:
        return "jkl"
    if d==6:
        return "mno"
    if d==7:
        return "pqrs"
    if d==8:
        return "tuv"
    if d==9:
        return "wxyz"
def printkeypad(num,op):
    if num==0:
        print(op)
        return 
    lastD=num%10
    num=num//10
    s=getString(lastD)
    for i in s:
        printkeypad(num,i+op)
printkeypad(234,"")


# good numbers:

def goods(sumn,temp,digit):
    if temp==0:
        return True
    rem=temp%10
    if rem>sumn and rem!=digit:
        sumn+=rem
        temp=temp//10
        return goods(sumn,temp,digit)
    return False 

def goodNumbers(a, b, digit):
    op=[]
    for num in range(a,b+1):
        temp=num
        sumn=temp%10
        if sumn==digit:
            continue
        temp=temp//10
        if goods(sumn,temp,digit)==True:
            op.append(num)
    return op



def callingrecu(s,i,maxi,mini,ans,sign):
    if i>=len(s) or s[i].isnumeric()==False:
        return sign*ans
    ans=ans*10+(ord(s[i])-ord('0'))
    if sign==1 and (sign*ans)>=maxi:
        return maxi
    if sign==-1 and (sign*ans)<=mini:
        return mini
    final=callingrecu(s,i+1,maxi,mini,ans,sign) 
    return final 

def createAtoi(s):
    # write your code here
    s=s.strip()
    sign=1
    if s[0]=="-":
        sign=-1
    if s[0]=="-" or s[0]=="+":
        i=1
    else:
        i=0
    maxi=(2**31)-1
    mini=-(2**31)
    ans=0
    final=callingrecu(s,i,maxi,mini,ans,sign)
    return final

        
    





    
# def rev(revarr,stack):
#     if len(stack)==0:
#         return revarr
#     rev(revarr,stack[1:])
#     revarr.append(stack[0])
#     return revarr


# def reverseStack(stack: List[int]) -> None:
#     # Write your code here.
#     revarr=[]
#     rev(revarr,stack)
#     for i in range(len(revarr)):
#         stack[i]=revarr[i]
#     return stack

def rev(stack: List[int],start,end) -> None:
    # Write your code here.'    
    if start >= end:
        return stack
    else:
        temp = stack[start]
        stack[start] = stack[end]
        stack[end] = temp
        return rev(stack, start + 1, end - 1)

def reverseStack(stack: List[int]) -> None:
    # Write your code here.'
    return rev(stack,0,len(stack)-1)  
    




# countzeroes:






    

    
    








d={'s':2,'r':4,'g':5,'b':1,'k':3}
l=sorted(d.values())
print(l)
d=dict(sorted(d.items(), key=lambda i:i[1] ,reverse=True))
print(d)



        
print(28%2)