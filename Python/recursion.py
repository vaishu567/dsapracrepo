
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
    