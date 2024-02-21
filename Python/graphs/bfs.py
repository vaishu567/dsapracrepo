
def bfs(adj,n):
    bfsa=[]
    visited=set()
    start=0
    to_visit=[start]
    visited.add(start)
    while to_visit:
        node=to_visit.pop(0)
        bfsa.append(node)
        for neighbor in adj[node]:
            if neighbor not in visited:
                to_visit.append(neighbor)
                visited.add(neighbor)
    return bfsa


graph = [[1,2,3], [4,7], [5], [6], [], [], [], []]
n=len(graph)
print(bfs(graph,n))

