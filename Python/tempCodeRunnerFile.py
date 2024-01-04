def recurs(indx,arr,final,t,op):
    if indx==len(arr):
        if t==0 :
            # if len(final)==0 or op not in final:
            final.add(op)
        return final
    if arr[indx]<=t:
        op.append(arr[indx])
        final=recurs(indx,arr,final,t-arr[indx],op)
        op.remove(arr[indx])
    final=recurs(indx+1,arr,final,t,op)
    return final
def combinationalSum(A, B):
    A=sorted(A)
    final=set()
    op=[]
    fin=recurs(0,A,final,B,op)
    fin=list(fin)
    return fin
A=[1,2,3]
B=5
print(combinationalSum(A, B))