
def isBipartite(graph):
    n=len(graph)
    color=[-1 for _ in range(n)]
    to_visit=[0]
    while to_visit:
        node=to_visit.pop(0)
        color[0]=0
        for neighbour in graph[node]:
            if color[neighbour]==-1:
                to_visit.append(neighbour)
                if color[node]==0:
                    color[neighbour]=1
                else:
                    color[neighbour]=0
            elif color[neighbour]==color[node]:
                return False
    for i in range(1,n):
        if color[i]==color[i-1]:
            return False
    return True

graph =[[1],[0,3],[3],[1,2]]
print(isBipartite(graph))