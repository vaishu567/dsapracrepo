# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

# Example 1:

# Input: n = 2, trust = [[1,2]]
# Output: 2
# Example 2:

# Input: n = 3, trust = [[1,3],[2,3]]
# Output: 3
# Example 3:

# Input: n = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1


def townjudge(n,trust):
    # we have to solve this problem using indegree and outdegree:
    trusted=[0 for i in range(n+1)] #indegree
    trusting=[0 for i in range(n+1)] #outdegree
    for edge in trust:
        u,v=edge[0],edge[1]
        trusting[u]+=1
        trusted[v]+=1
    for i in range(1,n+1):
        if trusting[i]==0 and trusted[i]==n-1:
            return i
    return -1

n = 3
trust = [[1,2],[2,3]]
print(townjudge(n,trust))
    
