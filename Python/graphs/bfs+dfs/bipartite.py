def bipartite(edges,n):
    m=len(edges[0])
    adjarr=[ [] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if edges[i][j]==1:
                adjarr[i].append(j)
                adjarr[j].append(i)
    color=[-1 for _ in range(n)]
    to_visit=[0]
    while to_visit:
        node=to_visit.pop(0)
        color[0]=0
        for neighbour in adjarr[node]:
            if color[neighbour]==-1:
                to_visit.append(neighbour)
                color[neighbour]=( 1 if color[node]==0 else 0)
            elif color[node]==color[neighbour]:
                return False
    for i in range(1,n):
        if color[i]==color[i-1]:
            return True
    return False

    
n= 3
edges = [[0, 1, 1], [0, 0, 1], [0,0,0]]
print(bipartite(edges,n))
def bipartitebool(n,start,graph,color):
    to_visit=[start]
    while to_visit:
        node=to_visit.pop(0)
        color[start]=0
        for neighbour in graph[node]:
            if color[neighbour]==-1:
                to_visit.append(neighbour)
                if color[node]==0:
                    color[neighbour]=1
                else:
                    color[neighbour]=0
            elif color[neighbour]==color[node]:
                return False
    return True

def isBipartite(graph):
    n=len(graph)
    color=[-1 for _ in range(n)]
    for i in range(n):
        if color[i]==-1:
            if bipartitebool(n,i,graph,color)==False:
                return False
    return True




graph =[[1],[0,3],[3],[1,2]]
print(isBipartite(graph))



# bipartite dfs:
def bipartitebooldfs(n,start,c,graph,color):
    color[start]=c
    for neighbour in graph[start]:
        if color[neighbour]==-1:
            if c==0:
                if bipartitebooldfs(n,neighbour,1,graph,color)==False:
                    return False
            else:
                if bipartitebooldfs(n,neighbour,0,graph,color)==False:
                    return False
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