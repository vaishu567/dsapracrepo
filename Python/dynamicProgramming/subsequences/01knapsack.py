def knapsackrecur(wt,val,ind,W,n):
    if W==0 or ind==n:
        return 0
    take=0
    if wt[ind]<=W:
        take= val[ind]+knapsackrecur(wt,val,ind+1,W-wt[ind],n)
    nottake=0+knapsackrecur(wt,val,ind+1,W,n)
    return max(take,nottake)
n=3
wt=[3,4,5]
val=[30,50,60]
W=8
print(knapsackrecur(wt,val,0,W,n))
