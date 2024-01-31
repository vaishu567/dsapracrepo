# Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

# 739. Daily Temperatures

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:

# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# Constraints:

# 1 <= temperatures.length <= 105
# 30 <= temperatures[i] <= 100

def dailyTemperatures(temperatures):
    n=len(temperatures)
    arr=[0 for i in range(n)]
    for ind in range(n-1):
        i=ind+1
        while i<n:
            if temperatures[ind]<temperatures[i]:
                print(i,ind)
                arr[ind]=i-ind
                break
            i+=1
    return arr
# accepted version:
def dailyTemperatures(temperatures):
    n=len(temperatures)
    arr=[0 for i in range(n)]
    stack=[]
    for ind in range(n):
        while stack and temperatures[ind]>temperatures[stack[-1]]:
            i=stack.pop()
            arr[i]=ind-i
        stack.append(ind)
    return arr
temperatures = [73,74,75,71,69,72,76,73]
print(dailyTemperatures(temperatures))
        





