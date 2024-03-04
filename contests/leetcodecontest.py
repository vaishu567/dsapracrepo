# def numberofprovinces(adj,n):
#     adjlist=[[] for i in range(n)]
#     for u in range(n):
#         for v in range(i):
#             adjlist[u].append(v)
    
def maximumValueSum(nums, k, edges):
    maxi=float('-inf')
    n=len(nums)
    for edge in edges:
        temp=nums[:]
        for _ in range(n):
            u=edge[0]
            v=edge[1]
            temp[u]=(temp[u]^k)
            temp[v]=(temp[v]^k)
            sumi=sum(temp)
            print(temp,sumi)
            maxi=max(maxi,sumi)
    if maxi==float('inf'):
        return sum(nums)
    ans=max(sum(nums),maxi)
    return ans
# nums = [1,2,1]
# k = 3
# nums = [7,7,7,7,7,7]
# k = 3
# edges = [[0,1],[0,2],[0,3],[0,4],[0,5]]
# Output: 42
nums=[24,78,1,97,44]
k=6
edges=[[0,2],[1,2],[4,2],[3,4]]
# edges = [[0,1],[0,2]]
print(maximumValueSum(nums,k,edges))
print(6^24)