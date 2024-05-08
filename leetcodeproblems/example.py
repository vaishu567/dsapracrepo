from collections import deque

def the_order(n):
    if n <= 1:
        return [1]
    q = deque()
    i = 1
    while i <= n:
        q.append(i)
        i += 1
    ans = []
    while q:
        k = q.popleft()
        q.append(k)
        front = q.popleft()
        ans.append(front)
    return ans
print(the_order(5))

def findRelativeRanks(score):
    new = sorted(score, reverse=True)
    l = []
    d = {}
    print(new)
    for i in range(len(new)):
        if i == 0:
            d[new[i]] = "Gold Medal"
        elif i == 1:
            d[new[i]] = "Silver Medal"
        elif i == 2:
            d[new[i]] = "Bronze Medal"
        else:
            d[new[i]] = str(i+1)
    l = [d[i] for i in score]
    return d


score=[5, 4, 3, 2, 1]
print(findRelativeRanks(score))




