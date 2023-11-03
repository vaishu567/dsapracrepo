
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
    

