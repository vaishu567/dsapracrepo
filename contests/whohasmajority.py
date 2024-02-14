# gfg:
# given an array of size n and two elemnts x,y and find the element which is occuring more number of times than other.
# we should solve t.C=O(N) and space comp=O(1)
# def majorityWins(self, arr, n, x, y):
#     # code here
#     d={}
#     frex=0
#     frey=0
#     for i in range(n):
#         if arr[i] not in d:
#             d[arr[i]]=1
#         else:
#             d[arr[i]]+=1
#     if x in d:
#         frex=d[x]
#     if y in d:
#         frey=d[y]
#     if frex>frey:
#         return x
#     elif frey>frex:
#         return y
#     else:
#         return min(x,y)
def majorityWins(arr, n, x, y):
    # code here
    frex=0
    frey=0
    for i in range(n):
        if arr[i]==x:
            frex+=1
        elif arr[i]==y:
            frey+=1
    if frex>frey:
        return x
    elif frey>frex:
        return y
    else:
        return min(x,y)