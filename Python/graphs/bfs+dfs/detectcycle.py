# using bfs:

def helper(src,adj,vis):
    vis[src]=1
    to_visit=[(src,-1)]
    while to_visit:
        node,parent=to_visit.pop(0)
        for neighbor in adj[node]:
            if vis[neighbor]!=1:
                to_visit.append((neighbor,node))
                vis[neighbor]=1
            elif neighbor!=parent:
                return True
    return False

def detectcyclebfs(n,adjarr):
    vis=[0 for i in range(n+1)]
    for i in range(n):
        if vis[i]!=1:
            ans=helper(i,adjarr,vis)
            if ans==True:
                return True
    return False

# using dfs:
def helperdfs(adj,vis,src,parent):
    vis[src]=1
    for adjnode in adj[src]:
        if vis[adjnode]!=1:
            if helperdfs(adj,vis,adjnode,src)==True:
                return True
        elif adjnode!=parent:
            return True
    return False

def detectcyclebfs(n,adjarr):
    vis=[0 for _ in range(n+1)]
    for src in range(n):
        if vis[src]!=1:
            ans=helperdfs(adjarr,vis,src,-1)
            if ans==True:
                return True
    return False
