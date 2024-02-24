def bipartitebooldfs(n,start,c,graph,color):
    color[start]=c
    for neighbour in graph[start]:
        if color[neighbour]==-1:
            if color[start]==0:
                c=1
            else:
                c=0
            bipartitebooldfs(n,neighbour,c,graph,color)
        elif color[neighbour]==c:
            return False
    return True
def isBipartite(graph):
    n=len(graph)
    color=[-1 for _ in range(n)]
    for i in range(n):
        if color[i]==-1:
            if bipartitebooldfs(n,i,0,graph,color)==False:
                return False
    return True




graph =[[1],[0,3],[3],[1,2]]
print(isBipartite(graph))