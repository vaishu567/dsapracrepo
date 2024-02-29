def minmul(start,end,arr):
    mod=10**(5)
    dist=[float('inf') for i in range(10**(5))]
    to_visit=[(0,start)]
    while to_visit:
        steps,node=to_visit.pop(0)
        for i in arr:
            mul=node*i
            mul=mul%mod
            if mul==end:
                return steps+1
            if steps+1<dist[mul]:
                dist[mul]=steps+1
                to_visit.append((steps+1,mul))
    return -1
