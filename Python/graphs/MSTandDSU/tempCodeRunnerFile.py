    maxi=float('-inf')
    n=len(nums)
    for edge in edges:
        for _ in range(n):
            temp=nums[:]
            u=edge[0]
            v=edge[1]
            temp[u]=(temp[u]^k)
            temp[v]=(temp[v]^k)
            sumi=sum(temp)
            maxi=max(maxi,sumi)
    if maxi==float('inf'):
        return sum(nums)
    ans=max(sum(nums),maxi)
    return ans