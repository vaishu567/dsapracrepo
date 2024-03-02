# # function should return parent of x
# def find(parent, x):
#     # Code here
#     if x==parent[x-1]:
#         return x
#     # here we are not doing path compression:
#     parent[x-1]=find(parent,parent[x-1])
#     return parent[x-1]
        

# # function shouldn't return or print anything
# def unionSet(parent, x, z):
#     # rank=[0 for i in range(len(parent)+1)]
#     # Code here
#     # we will implement union by rank:
#     ulp_x=find(parent,x)
#     ulp_z=find(parent,z)
#     parent[ulp_x-1]=ulp_z
    