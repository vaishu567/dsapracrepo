def inpmat():
    n,m=map(int,input("Enter n and m values separated by a space: ").split())
    mat=[[0  for i in range(m+1)] for  i in range(n+1)]
    for _ in range(m):
        u,v = map(int, input("Enter u and v values separated by a space: ").split())
        mat[u][v]=1
        mat[v][u]=1
    return mat
print(inpmat())