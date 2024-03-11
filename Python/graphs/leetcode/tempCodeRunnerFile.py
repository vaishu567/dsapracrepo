 for edge in trust:
        u,v=edge[0],edge[1]
        adj[u].append(v)
    for i in range(1,n+1):
        if adj[i]==[]:
            return i
    return -1