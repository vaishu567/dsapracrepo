# array bruteforce:
def bestTimeToBuyAndSellStock(prices):
    # Write your code here.
    maxprofit=-1
    n=len(prices)
    for i in range(n):
        for j in range(i+1,n):
            if prices[j]>prices[i]:
                maxprofit=max((prices[j]-prices[i]),maxprofit)
    if maxprofit==-1:
        return 0
    return maxprofit

prices=[7,1,5,4,3,6]
print(bestTimeToBuyAndSellStock(prices))

# recursion:
def bestTimeToBuyAndSell(n,prices,ind,maxprofit):
    # Write your code here.
    if ind==n-1:
        return maxprofit
    buy=prices[ind]
    for i in range(ind+1,n):
        if prices[i]>buy:
            maxprofit=max((prices[i]-buy),maxprofit)
    notbuy=bestTimeToBuyAndSell(n,prices,ind+1,maxprofit)
    return max(maxprofit,notbuy)

def bestTimeToBuyAndSellStock(prices):
    # Write your code here.
    n=len(prices)
    ind=0
    maxprofit=float('-inf')
    if bestTimeToBuyAndSell(n,prices,ind,maxprofit)==float('-inf'):
        return 0
    return bestTimeToBuyAndSell(n,prices,ind,maxprofit)



# but dp on this problem is simple:
def bestTimeToBuyAndSellStock(prices):
    buy=prices[0]
    maxprofit=0
    n = len(prices)
    for i in range(1,n):
        cost=prices[i]-buy
        maxprofit=max(maxprofit,cost)
        # here we are remembering previous buy hence this comes under dp:
        buy=min(buy,prices[i])
    return maxprofit

    




        
    
    



    

        


    